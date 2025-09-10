"""
Configuration and fixtures for tests.
"""

import pytest
from src.core.fields import FiniteField
from src.core.aiip import AIIPParameters
from src.temporal.binding import TemporalBindingParameters
from src.proofs.stark import STARKParameters

@pytest.fixture(scope="session")
def test_field():
    """Create a test finite field."""
    return FiniteField(1000003)  # Prime field

@pytest.fixture(scope="session")
def test_aiip_params():
    """Create test AIIP parameters."""
    return AIIPParameters(
        field_size=1000003,
        alpha=5,
        iterations=10,
        security_param=128
    )

@pytest.fixture(scope="session")
def test_temporal_params():
    """Create test temporal binding parameters."""
    return TemporalBindingParameters(
        field_size=1000003,
        alpha=5,
        max_iterations=100,
        security_param=128
    )

@pytest.fixture(scope="session")
def test_stark_params():
    """Create test STARK parameters."""
    return STARKParameters(
        blowup_factor=4,
        security_param=128,
        fri_folding_factor=2
    )