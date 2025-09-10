"""
Type definitions for AOW.
"""

from dataclasses import dataclass
from typing import Union

@dataclass
class AOWParameters:
    """Parameters for AOW computation."""
    field_size: int
    alpha: int
    iterations: int
    security_param: int = 128

@dataclass
class TemporalClaim:
    """A temporal claim with proof."""
    input_value: int
    output_value: int
    iterations: int
    proof: Union[dict, None] = None

@dataclass
class EventOrdering:
    """Event ordering with temporal guarantees."""
    events: list
    temporal_proofs: list
    chain_hash: bytes