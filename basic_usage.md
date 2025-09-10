# Tutorial: Basic AOW Usage

## Introduction

This tutorial will guide you through the basic usage of the AOW primitive. You'll learn how to:

1. Set up AOW parameters
2. Perform polynomial iteration
3. Verify temporal binding
4. Create simple event chains

## Prerequisites

- Python 3.8+
- AOW installed (see [Installation Guide](../user-guide/installation.md))

## Step 1: Import Required Modules

```python
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters
from src.temporal.chain import EventChain

Step 2: Initialize Parameters
python

# Create a finite field (using a small prime for demonstration)
field = FiniteField(1000003)

# Set polynomial parameters
alpha = 5  # Quadratic non-residue
iterations = 1000

# Set temporal binding parameters
temporal_params = TemporalBindingParameters(
    field_size=1000003,
    alpha=alpha,
    max_iterations=10000,
    security_param=128
)

Step 3: Perform AOW Iteration
python

# Generate a random input value
x = field.random_element()
print(f"Input value: {x}")

# Compute AOW function
result = iterate_polynomial(x, alpha, iterations, field)
print(f"Result after {iterations} iterations: {result}")

Step 4: Verify Temporal Binding
python

# Verify the computation
is_valid = verify_temporal_binding(x, result, iterations, temporal_params, field)
print(f"Temporal binding verified: {is_valid}")

# Try with incorrect result (should fail)
is_valid_fake = verify_temporal_binding(x, result + 1, iterations, temporal_params, field)
print(f"Fake temporal binding verified: {is_valid_fake}")  # Should be False

Step 5: Create an Event Chain
python

# Create an event chain
chain = EventChain(field, alpha)

# Add events to the chain
event1_hash = chain.add_event(b"Transaction: Alice -> Bob, 10 BTC")
event2_hash = chain.add_event(b"Transaction: Bob -> Charlie, 5 BTC")
event3_hash = chain.add_event(b"Transaction: Charlie -> Dave, 3 BTC")

print(f"Event 1 hash: {event1_hash}")
print(f"Event 2 hash: {event2_hash}")
print(f"Event 3 hash: {event3_hash}")

# Verify chain integrity
is_chain_valid = chain.verify_chain()
print(f"Event chain valid: {is_chain_valid}")

Step 6: Test Tamper Resistance
python

# Attempt to tamper with the chain
original_data = chain.chain[1].data
chain.chain[1].data = b"Transaction: MALICIOUS -> Attack, 1000 BTC"

# Verify chain integrity (should fail)
is_chain_valid_after_tamper = chain.verify_chain()
print(f"Chain valid after tampering: {is_chain_valid_after_tamper}")  # Should be False

# Restore original data
chain.chain[1].data = original_data
is_chain_valid_after_restore = chain.verify_chain()
print(f"Chain valid after restoration: {is_chain_valid_after_restore}")  # Should be True

Step 7: Batch Processing
python

# Process multiple inputs
inputs = [field.random_element() for _ in range(5)]
results = []

for i, x in enumerate(inputs):
    result = iterate_polynomial(x, alpha, iterations, field)
    results.append(result)
    print(f"Input {i+1}: {x} -> {result}")

# Verify all results
for i, (x, result) in enumerate(zip(inputs, results)):
    is_valid = verify_temporal_binding(x, result, iterations, temporal_params, field)
    print(f"Verification {i+1}: {is_valid}")

Step 8: Error Handling
python

# Test error cases
try:
    # Too many iterations
    invalid_result = iterate_polynomial(x, alpha, 20000, field)
except ValueError as e:
    print(f"Error: {e}")

try:
    # Invalid temporal binding verification
    verify_temporal_binding(x, result, 20000, temporal_params, field)
except ValueError as e:
    print(f"Error: {e}")

Complete Example

Here's the complete code from this tutorial:
python

# tutorial_basic_usage.py
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters
from src.temporal.chain import EventChain

# Initialize parameters
field = FiniteField(1000003)
alpha = 5
iterations = 1000

temporal_params = TemporalBindingParameters(
    field_size=1000003,
    alpha=alpha,
    max_iterations=10000,
    security_param=128
)

# Perform AOW iteration
x = field.random_element()
result = iterate_polynomial(x, alpha, iterations, field)

# Verify temporal binding
is_valid = verify_temporal_binding(x, result, iterations, temporal_params, field)
print(f"Temporal binding verified: {is_valid}")

# Create event chain
chain = EventChain(field, alpha)
chain.add_event(b"Transaction: Alice -> Bob, 10 BTC")
chain.add_event(b"Transaction: Bob -> Charlie, 5 BTC")
chain.add_event(b"Transaction: Charlie -> Dave, 3 BTC")

# Verify chain
is_chain_valid = chain.verify_chain()
print(f"Event chain valid: {is_chain_valid}")

Next Steps

Now that you've completed the basic usage tutorial:

    Explore the event chain tutorial for more advanced usage

    Learn about STARK proofs for verifiable computation

    Read about distributed synchronization for multi-party applications

    Check the API reference for detailed documentation

Troubleshooting

If you encounter issues:

    Ensure AOW is properly installed

    Check that you're using a valid quadratic non-residue for your field

    Verify that iteration counts don't exceed the maximum allowed

    Check the error messages for specific issues

Further Reading

    Theory Overview

    User Guide

    API Reference
