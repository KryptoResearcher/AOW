"""
Unit tests for AIIP implementation.
"""

import pytest
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial, compute_iteration_trace, AIIPParameters

class TestAIIP:
    """Test cases for AIIP functions."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def params(self):
        """Create AIIP parameters for testing."""
        return AIIPParameters(
            field_size=1000003,
            alpha=5,
            iterations=10,
            security_param=128
        )
    
    def test_iterate_polynomial(self, field, params):
        """Test polynomial iteration."""
        result = iterate_polynomial(123, params.alpha, params.iterations, field)
        
        # Should be different from input
        assert result != 123
        
        # Should be deterministic
        result2 = iterate_polynomial(123, params.alpha, params.iterations, field)
        assert result == result2
    
    def test_compute_iteration_trace(self, field, params):
        """Test iteration trace computation."""
        trace = compute_iteration_trace(123, params.alpha, params.iterations, field)
        
        # Trace should have correct length
        assert len(trace) == params.iterations + 1  # Includes initial value
        
        # First element should be input
        assert trace[0] == 123
        
        # Each element should be f(previous)
        for i in range(params.iterations):
            expected = field.add(field.sqr(trace[i]), params.alpha)
            assert trace[i+1] == expected
    
    def test_zero_iterations(self, field, params):
        """Test with zero iterations."""
        result = iterate_polynomial(123, params.alpha, 0, field)
        assert result == 123
        
        trace = compute_iteration_trace(123, params.alpha, 0, field)
        assert trace == [123]
    
    def test_single_iteration(self, field, params):
        """Test with single iteration."""
        result = iterate_polynomial(123, params.alpha, 1, field)
        expected = field.add(field.sqr(123), params.alpha)
        assert result == expected
        
        trace = compute_iteration_trace(123, params.alpha, 1, field)
        assert trace == [123, expected]