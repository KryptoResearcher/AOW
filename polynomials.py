"""
Polynomial implementations for AOW.
"""

from dataclasses import dataclass
from .fields import FiniteField

@dataclass
class QuadraticPolynomial:
    """Quadratic polynomial f(x) = x² + α."""
    alpha: int
    field: FiniteField
    
    def evaluate(self, x: int) -> int:
        """Evaluate polynomial at point x."""
        return self.field.add(self.field.sqr(x), self.alpha)
    
    def iterate(self, x: int, n: int) -> int:
        """Compute n-th iteration of polynomial."""
        current = x
        for _ in range(n):
            current = self.evaluate(current)
        return current
    
    def trace(self, x: int, n: int) -> list:
        """Compute full trace of n iterations."""
        trace = [x]
        current = x
        for _ in range(n):
            current = self.evaluate(current)
            trace.append(current)
        return trace