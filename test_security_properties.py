"""
Property-based tests for security properties.
"""

import pytest
from hypothesis import given, strategies as st
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import depth_uniqueness_probability, TemporalBindingParameters

class TestSecurityProperties:
    """Property-based tests for security properties."""
    
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
            max_iterations=100,
            security_param=128
        )
    
    @given(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100))
    def test_depth_uniqueness_bounds(self, params, n, m):
        """Test that depth uniqueness probability is properly bounded."""
        prob = depth_uniqueness_probability(n, m, params)
        
        # Probability should be between 0 and 1
        assert 0 <= prob <= 1
        
        # For different n and m, probability should be less than 1
        if n != m:
            assert prob < 1
    
    @given(st.integers(min_value=0, max_value=1000002))
    def test_collision_resistance(self, field, params, x):
        """Test that different inputs produce different outputs with high probability."""
        # Test with two different iteration counts
        y1 = iterate_polynomial(x, params.alpha, 10, field)
        y2 = iterate_polynomial(x, params.alpha, 20, field)
        
        # With high probability, these should be different
        # (This is a probabilistic test, but the probability of collision is very low)
        assert y1 != y2 or x == 0  # Allow for fixed points