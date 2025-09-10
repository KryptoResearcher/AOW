"""
Temporal binding verification for AOW.
"""

from dataclasses import dataclass
from typing import Tuple
from ..core.fields import FiniteField
from ..core.aiip import iterate_polynomial

@dataclass
class TemporalBindingParameters:
    """Parameters for temporal binding verification."""
    field_size: int
    alpha: int
    max_iterations: int
    security_param: int = 128

def verify_temporal_binding(
    x: int, 
    y: int, 
    iterations: int, 
    params: TemporalBindingParameters,
    field: FiniteField
) -> bool:
    """
    Verify that y = f^{(n)}(x) for the given parameters.
    
    Args:
        x: Input value
        y: Claimed output value
        iterations: Number of iterations
        params: Temporal binding parameters
        field: Finite field instance
        
    Returns:
        True if verification succeeds, False otherwise
    """
    if iterations > params.max_iterations:
        return False
    
    computed_y = iterate_polynomial(x, params.alpha, iterations, field)
    return computed_y == y

def depth_uniqueness_probability(
    n: int, 
    m: int, 
    params: TemporalBindingParameters
) -> float:
    """
    Compute the probability that f^{(n)}(x) = f^{(m)}(x) for random x.
    
    Args:
        n: First iteration count
        m: Second iteration count
        params: Temporal binding parameters
        
    Returns:
        Probability of collision
    """
    if n == m:
        return 1.0
    
    # Upper bound from Theorem 2 in paper
    diff = abs(n - m)
    numerator = diff * (2 ** diff)
    denominator = params.field_size
    return numerator / denominator