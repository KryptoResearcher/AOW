"""
Implementation of the Affine Iterated Inversion Problem (AIIP).
"""

from dataclasses import dataclass
from typing import List
from .fields import FiniteField

@dataclass
class AIIPParameters:
    """Parameters for AIIP computation."""
    field_size: int
    alpha: int
    iterations: int
    security_param: int = 128

def iterate_polynomial(x: int, alpha: int, iterations: int, field: FiniteField) -> int:
    """
    Compute f^{(n)}(x) where f(x) = x² + α.
    
    Args:
        x: Initial value
        alpha: Constant term in polynomial
        iterations: Number of iterations
        field: Finite field instance
        
    Returns:
        Result of polynomial iteration
    """
    current = x
    for _ in range(iterations):
        current = field.add(field.sqr(current), alpha)
    return current

def compute_iteration_trace(x: int, alpha: int, iterations: int, field: FiniteField) -> List[int]:
    """
    Compute the full trace of polynomial iteration.
    
    Args:
        x: Initial value
        alpha: Constant term in polynomial
        iterations: Number of iterations
        field: Finite field instance
        
    Returns:
        List of all intermediate values
    """
    trace = [x]
    current = x
    for _ in range(iterations):
        current = field.add(field.sqr(current), alpha)
        trace.append(current)
    return trace