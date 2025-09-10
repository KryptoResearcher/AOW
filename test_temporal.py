"""
Unit tests for temporal binding implementation.
"""

import pytest
from src.core.fields import FiniteField
from src.temporal.binding import verify_temporal_binding, depth_uniqueness_probability, TemporalBindingParameters

class TestTemporalBinding:
    """Test cases for temporal binding functions."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def params(self):
        """Create temporal binding parameters for testing."""
        return TemporalBindingParameters(
            field_size=1000003,
            alpha=5,
            max_iterations=1000,
            security_param=128
        )
    
    def test_verify_temporal_binding(self, field, params):
        """Test temporal binding verification."""
        # Test valid binding
        x = 123
        iterations = 10
        y = iterate_polynomial(x, params.alpha, iterations, field)
        
        assert verify_temporal_binding(x, y, iterations, params, field)
        
        # Test invalid binding (wrong y)
        assert not verify_temporal_binding(x, y + 1, iterations, params, field)
        
        # Test invalid binding (too many iterations)
        assert not verify_temporal_binding(x, y, params.max_iterations + 1, params, field)
    
    def test_depth_uniqueness_probability(self, params):
        """Test depth uniqueness probability calculation."""
        # Same depth should have probability 1
        assert depth_uniqueness_probability(10, 10, params) == 1.0
        
        # Different depths should have probability < 1
        prob = depth_uniqueness_probability(10, 20, params)
        assert 0 < prob < 1
        
        # Probability should be symmetric
        prob2 = depth_uniqueness_probability(20, 10, params)
        assert prob == prob2
        
        # Probability should decrease with larger field size
        large_params = TemporalBindingParameters(
            field_size=2**256,
            alpha=5,
            max_iterations=1000,
            security_param=128
        )
        small_prob = depth_uniqueness_probability(10, 20, large_params)
        assert small_prob < prob