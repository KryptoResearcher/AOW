# Quick Start Guide

## Introduction

This guide will help you get started with AOW in minutes. We'll cover:

1. Basic AOW iteration
2. Temporal binding verification
3. Event chain creation
4. STARK proof generation

## Prerequisites

- Python 3.8+
- AOW installed (see [Installation Guide](installation.md))

## Basic Usage

### 1. Import AOW Modules

```python
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters

2. Initialize Parameters
python

# Use recommended parameters for 128-bit security
field = FiniteField(2**256)
alpha = 5  # Quadratic non-residue
iterations = 1000

3. Perform AOW Iteration
python

# Generate random input
x = field.random_element()

# Compute AOW function
result = iterate_polynomial(x, alpha, iterations, field)

print(f"Input: {x}")
print(f"Result after {iterations} iterations: {result}")

4. Verify Temporal Binding
python

# Set up temporal binding parameters
params = TemporalBindingParameters(
    field_size=2**256,
    alpha=alpha,
    max_iterations=10000,
    security_param=128
)

# Verify the computation
is_valid = verify_temporal_binding(x, result, iterations, params, field)
print(f"Temporal binding verified: {is_valid}")

Event Chain Example
1. Create an Event Chain
python

from src.temporal.chain import create_event_chain

# Create sample events
events = [
    b"Transaction: Alice -> Bob, 10 BTC",
    b"Transaction: Bob -> Charlie, 5 BTC",
    b"Transaction: Charlie -> Dave, 3 BTC"
]

# Create event chain
chain = create_event_chain(events, field, alpha)

# Verify chain integrity
is_valid = chain.verify_chain()
print(f"Event chain valid: {is_valid}")

2. Add Events to Chain
python

# Add new event
new_event_hash = chain.add_event(b"Transaction: Dave -> Eve, 2 BTC")
print(f"New event hash: {new_event_hash}")

# Verify chain again
is_valid = chain.verify_chain()
print(f"Event chain still valid: {is_valid}")

STARK Proof Example
1. Generate STARK Proof
python

from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters

# Set up STARK parameters
stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

# Generate proof
proof, public_inputs = generate_stark_proof(
    x, alpha, iterations, field, stark_params
)

print(f"Proof generated: {len(str(proof))} characters")

2. Verify STARK Proof
python

# Verify proof
is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)
print(f"STARK proof valid: {is_valid}")

Running Examples

The repository includes several examples:
bash

# Run basic iteration example
python examples/basic_iteration.py

# Run event ordering example
python examples/event_ordering.py

# Run STARK proofs example
python examples/stark_proofs.py

# Run distributed synchronization example
python examples/distributed_sync.py

Next Steps

Now that you've completed the quick start guide:

    Explore the API Reference for detailed documentation

    Read about advanced usage for more complex scenarios

    Learn about parameter selection for different security levels

    Check out the tutorials for step-by-step guides

Getting Help

If you have questions or encounter issues:

    Check the FAQ

    Review the examples

    Open an issue on GitHub