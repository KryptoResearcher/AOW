"""
Unit tests for polynomial implementation.
"""

import pytest
from src.core.fields import FiniteField
from src.core.polynomials import QuadraticPolynomial

class TestQuadraticPolynomial:
    """Test cases for QuadraticPolynomial class."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def polynomial(self, field):
        """Create a quadratic polynomial for testing."""
        return QuadraticPolynomial(alpha=5, field=field)
    
    def test_evaluation(self, polynomial):
        """Test polynomial evaluation."""
        result = polynomial.evaluate(10)
        expected = polynomial.field.add(polynomial.field.sqr(10), 5)
        assert result == expected
    
    def test_iteration(self, polynomial):
        """Test polynomial iteration."""
        result = polynomial.iterate(10, 3)
        
        # Manual calculation
        x0 = 10
        x1 = polynomial.evaluate(x0)
        x2 = polynomial.evaluate(x1)
        x3 = polynomial.evaluate(x2)
        
        assert result == x3
    
    def test_trace(self, polynomial):
        """Test trace computation."""
        trace = polynomial.trace(10, 3)
        
        # Should have correct length
        assert len(trace) == 4  # 3 iterations + initial
        
        # Should match manual calculation
        x0 = 10
        x1 = polynomial.evaluate(x0)
        x2 = polynomial.evaluate(x1)
        x3 = polynomial.evaluate(x2)
        
        assert trace == [x0, x1, x2, x3]