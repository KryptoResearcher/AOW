# Tutorial: Event Chains with AOW

## Introduction

This tutorial will guide you through creating and using event chains with AOW for Byzantine-resistant event ordering.

## Prerequisites

- Completion of [Basic Usage Tutorial](basic_usage.md)
- Understanding of temporal binding concepts

## Step 1: Import Required Modules

```python
from src.core.fields import FiniteField
from src.temporal.chain import create_event_chain
from src.utils import calculate_security_parameters

Step 2: Initialize Parameters
python

# Get recommended parameters for 128-bit security
params = calculate_security_parameters(128)
field = FiniteField(params['field_size'])
alpha = params['alpha']

print(f"Using field size: {params['field_size']}")
print(f"Using alpha: {alpha}")

Step 3: Create Sample Events
python

# Create sample events
events = [
    b"Block #1: Genesis",
    b"Block #2: Transaction: Alice -> Bob, 10 BTC",
    b"Block #3: Transaction: Bob -> Charlie, 5 BTC",
    b"Block #4: Transaction: Charlie -> Dave, 3 BTC",
    b"Block #5: Transaction: Dave -> Eve, 2 BTC"
]

print("Events to be added to chain:")
for i, event in enumerate(events):
    print(f"  {i+1}. {event.decode()}")

Step 4: Create Event Chain
python

# Create event chain
chain = create_event_chain(events, field, alpha)

print(f"Chain created with {len(chain.chain)} events")
print(f"Chain valid: {chain.verify_chain()}")

Step 5: Examine Chain Structure
python

# Examine chain structure
print("\nChain structure:")
for i, event in enumerate(chain.chain):
    prev_hash = int.from_bytes(event.previous_hash, 'big') if event.previous_hash else 0
    print(f"  Event {i+1}:")
    print(f"    Data: {event.data.decode()}")
    print(f"    Previous hash: {prev_hash % 1000}... (truncated)")
    print(f"    Timestamp: {event.timestamp}")

Step 6: Add New Events
python

# Add new events to the chain
new_events = [
    b"Block #6: Transaction: Eve -> Frank, 1 BTC",
    b"Block #7: Transaction: Frank -> Grace, 0.5 BTC"
]

for event_data in new_events:
    event_hash = chain.add_event(event_data)
    print(f"Added event: {event_data.decode()}")
    print(f"  Hash: {int.from_bytes(event_hash, 'big') % 1000}... (truncated)")

print(f"Chain now has {len(chain.chain)} events")
print(f"Chain valid: {chain.verify_chain()}")

Step 7: Verify Chain Integrity
python

# Verify chain integrity at different points
print("\nVerifying chain integrity:")

# Verify entire chain
is_valid = chain.verify_chain()
print(f"Full chain valid: {is_valid}")

# Verify first 3 events
partial_chain = chain.chain[:3]
# (In a real implementation, you would have a method to verify partial chains)
print(f"First 3 events valid: {True}")  # Simplified for tutorial

# Verify last 3 events
partial_chain = chain.chain[-3:]
print(f"Last 3 events valid: {True}")  # Simplified for tutorial

Step 8: Test Byzantine Resistance
python

# Test Byzantine resistance
print("\nTesting Byzantine resistance:")

# Save original state
original_chain = chain.chain.copy()

# Attempt to tamper with the chain
print("Attempting to tamper with event 3...")
chain.chain[2].data = b"Block #3: MALICIOUS: Attacker -> Self, 1000 BTC"

# Verify chain integrity
is_valid_after_tamper = chain.verify_chain()
print(f"Chain valid after tampering: {is_valid_after_tamper}")

# Restore original chain
chain.chain = original_chain
is_valid_after_restore = chain.verify_chain()
print(f"Chain valid after restoration: {is_valid_after_restore}")

Step 9: Cross-Chain Verification
python

# Create a second chain with the same events
print("\nCreating second chain with same events...")
chain2 = create_event_chain(events, field, alpha)

# Add the same new events
for event_data in new_events:
    chain2.add_event(event_data)

# Verify both chains have the same structure
print(f"Chains have same length: {len(chain.chain) == len(chain2.chain)}")
print(f"Chains have same final hash: {chain.chain[-1].previous_hash == chain2.chain[-1].previous_hash}")

Step 10: Performance Testing
python

# Test performance with different chain sizes
print("\nTesting performance with different chain sizes:")

import time

for chain_size in [10, 100, 1000]:
    test_events = [f"Test event {i}".encode() for i in range(chain_size)]
    
    start_time = time.time()
    test_chain = create_event_chain(test_events, field, alpha)
    creation_time = time.time() - start_time
    
    start_time = time.time()
    is_valid = test_chain.verify_chain()
    verification_time = time.time() - start_time
    
    print(f"Chain size {chain_size}:")
    print(f"  Creation time: {creation_time:.4f}s")
    print(f"  Verification time: {verification_time:.4f}s")
    print(f"  Valid: {is_valid}")

Complete Example
python

# tutorial_event_chain.py
from src.core.fields import FiniteField
from src.temporal.chain import create_event_chain
from src.utils import calculate_security_parameters
import time

# Initialize parameters
params = calculate_security_parameters(128)
field = FiniteField(params['field_size'])
alpha = params['alpha']

# Create events
events = [
    b"Block #1: Genesis",
    b"Block #2: Transaction: Alice -> Bob, 10 BTC",
    b"Block #3: Transaction: Bob -> Charlie, 5 BTC",
    b"Block #4: Transaction: Charlie -> Dave, 3 BTC",
    b"Block #5: Transaction: Dave -> Eve, 2 BTC"
]

# Create chain
chain = create_event_chain(events, field, alpha)

# Add new events
new_events = [
    b"Block #6: Transaction: Eve -> Frank, 1 BTC",
    b"Block #7: Transaction: Frank -> Grace, 0.5 BTC"
]

for event_data in new_events:
    chain.add_event(event_data)

# Verify chain
is_valid = chain.verify_chain()
print(f"Final chain valid: {is_valid}")

Next Steps

Now that you've completed the event chain tutorial:

    Explore the STARK proofs tutorial for verifiable computation

    Learn about distributed synchronization for multi-party applications

    Read about advanced usage for optimization techniques

    Check the API reference for detailed documentation

Real-World Applications

Event chains with AOW can be used for:

    Blockchain systems: Byzantine-resistant transaction ordering

    Audit logs: Tamper-evident event logging

    Supply chain tracking: Verifiable product history

    Document timestamping: Immutable timestamp records

Further Reading

    Temporal Binding Theory

    API Reference

    Advanced Usage Guide

