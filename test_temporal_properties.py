"""
Property-based tests for temporal properties.
"""

import pytest
from hypothesis import given, strategies as st
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import TemporalBindingParameters, verify_temporal_binding

class TestTemporalProperties:
    """Property-based tests for temporal properties."""
    
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
    
    @given(st.integers(min_value=0, max_value=1000002))
    def test_iteration_determinism(self, field, params, x):
        """Test that iteration is deterministic."""
        result1 = iterate_polynomial(x, params.alpha, params.iterations, field)
        result2 = iterate_polynomial(x, params.alpha, params.iterations, field)
        assert result1 == result2
    
    @given(st.integers(min_value=0, max_value=1000002), st.integers(min_value=1, max_value=10))
    def test_temporal_binding_verification(self, field, params, x, iterations):
        """Test that correct temporal bindings verify successfully."""
        if iterations > params.max_iterations:
            # Skip tests that exceed max iterations
            return
            
        y = iterate_polynomial(x, params.alpha, iterations, field)
        assert verify_temporal_binding(x, y, iterations, params, field)
    
    @given(st.integers(min_value=0, max_value=1000002), st.integers(min_value=1, max_value=10))
    def test_temporal_binding_rejection(self, field, params, x, iterations):
        """Test that incorrect temporal bindings are rejected."""
        if iterations > params.max_iterations:
            # Skip tests that exceed max iterations
            return
            
        y = iterate_polynomial(x, params.alpha, iterations, field)
        # Test with wrong y value
        assert not verify_temporal_binding(x, y + 1, iterations, params, field)