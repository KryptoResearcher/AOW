# API Reference - Temporal Module

## Overview

The temporal module provides functionality for temporal binding verification and event chain construction.

## Temporal Binding

### verify_temporal_binding(x, y, iterations, params, field)
Verify that y = f^{(n)}(x) for the given parameters.

**Parameters**:
- `x` (int): Input value
- `y` (int): Claimed output value
- `iterations` (int): Number of iterations
- `params` (TemporalBindingParameters): Temporal binding parameters
- `field` (FiniteField): Finite field instance

**Returns**: (bool) True if verification succeeds, False otherwise

**Example**:
```python
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters

params = TemporalBindingParameters(
    field_size=1000003,
    alpha=5,
    max_iterations=1000,
    security_param=128
)

is_valid = verify_temporal_binding(x, y, iterations, params, field)

depth_uniqueness_probability(n, m, params)

Compute the probability that f^{(n)}(x) = f^{(m)}(x) for random x.

Parameters:

    n (int): First iteration count

    m (int): Second iteration count

    params (TemporalBindingParameters): Temporal binding parameters

Returns: (float) Probability of collision

Example:
python

from src.temporal.binding import depth_uniqueness_probability

prob = depth_uniqueness_probability(10, 20, params)
print(f"Collision probability: {prob}")

Event Chain
Event Class

Dataclass representing a temporal event.

Attributes:

    data (bytes): Event data

    timestamp (int): Event timestamp

    previous_hash (bytes or None): Hash of previous event

EventChain Class
Constructor
python

EventChain(field, alpha)

Creates an empty event chain.

Parameters:

    field (FiniteField): Finite field instance

    alpha (int): Constant for polynomial f(x) = x² + α

Returns: EventChain instance
Methods
add_event(event_data, iterations=1000)

Add an event to the chain.

Parameters:

    event_data (bytes): Event data to add

    iterations (int): Number of AOW iterations (default: 1000)

Returns: (bytes) Hash of the new event
verify_chain()

Verify the integrity of the entire event chain.

Returns: (bool) True if chain is valid, False otherwise
Properties
chain

List of events in the chain.
genesis

Genesis value for the chain.
create_event_chain(events, field, alpha)

Create an event chain from a list of events.

Parameters:

    events (list): List of event data (bytes)

    field (FiniteField): Finite field instance

    alpha (int): Constant for polynomial

Returns: (EventChain) Event chain instance

Example:
python

from src.temporal.chain import create_event_chain

events = [b"Event 1", b"Event 2", b"Event 3"]
chain = create_event_chain(events, field, alpha)

Data Classes
TemporalBindingParameters

Dataclass for temporal binding parameters.

Attributes:

    field_size (int): Size of finite field

    alpha (int): Constant term

    max_iterations (int): Maximum number of iterations allowed

    security_param (int): Security parameter (default: 128)

Examples
Basic Temporal Binding
python

from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters

# Set up parameters
params = TemporalBindingParameters(
    field_size=1000003,
    alpha=5,
    max_iterations=1000,
    security_param=128
)

# Verify temporal binding
is_valid = verify_temporal_binding(x, y, iterations, params, field)

Event Chain Usage
python

from src.temporal.chain import EventChain

# Create event chain
chain = EventChain(field, alpha)

# Add events
hash1 = chain.add_event(b"Event 1")
hash2 = chain.add_event(b"Event 2")

# Verify chain
is_valid = chain.verify_chain()

Batch Verification
python

def batch_verify(claims, params, field):
    """Verify multiple temporal binding claims."""
    results = []
    for x, y, iterations in claims:
        is_valid = verify_temporal_binding(x, y, iterations, params, field)
        results.append(is_valid)
    return results

Error Handling

    ValueError: For invalid parameters (e.g., iterations > max_iterations)

    TypeError: For incorrect argument types

    ChainIntegrityError: For invalid event chains (custom exception)

Performance Notes

    Temporal binding verification is O(1) after computation

    Event chain operations are O(n) for chain length n

    Verification uses precomputed values where possible

See Also

    Core Module

    Proofs Module

    Utils Module

