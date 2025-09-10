"""
Finite field implementation for AOW.
"""

import random
from typing import Optional

class FiniteField:
    """Implementation of finite field arithmetic for AOW."""
    
    def __init__(self, modulus: int):
        """
        Initialize finite field with given modulus.
        
        Args:
            modulus: Prime modulus for the field
        """
        self.modulus = modulus
        self.size = modulus
    
    def add(self, a: int, b: int) -> int:
        """Add two field elements."""
        return (a + b) % self.modulus
    
    def sub(self, a: int, b: int) -> int:
        """Subtract two field elements."""
        return (a - b) % self.modulus
    
    def mul(self, a: int, b: int) -> int:
        """Multiply two field elements."""
        return (a * b) % self.modulus
    
    def sqr(self, a: int) -> int:
        """Square a field element."""
        return (a * a) % self.modulus
    
    def inv(self, a: int) -> int:
        """Compute multiplicative inverse of a field element."""
        if a == 0:
            raise ValueError("Cannot invert zero")
        return pow(a, self.modulus - 2, self.modulus)
    
    def random_element(self) -> int:
        """Generate a random field element."""
        return random.randint(0, self.modulus - 1)
    
    def is_quadratic_residue(self, a: int) -> bool:
        """Check if a field element is a quadratic residue."""
        if a == 0:
            return True
        # Euler's criterion
        return pow(a, (self.modulus - 1) // 2, self.modulus) == 1
    
    def sqrt(self, a: int) -> Optional[int]:
        """Compute square root of a field element if it exists."""
        if not self.is_quadratic_residue(a):
            return None
        
        # Tonelli-Shanks algorithm for prime fields
        # Implementation omitted for brevity
        # For now, return a simple implementation for primes ≡ 3 mod 4
        if self.modulus % 4 == 3:
            return pow(a, (self.modulus + 1) // 4, self.modulus)
        
        # General case implementation would go here
        raise NotImplementedError("Square root for primes not ≡ 3 mod 4 not implemented")