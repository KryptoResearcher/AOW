"""
Integration tests for complete AOW workflow.
"""

import pytest
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters
from src.temporal.chain import create_event_chain
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters

class TestAOWWorkflow:
    """Integration tests for complete AOW workflow."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def temporal_params(self):
        """Create temporal binding parameters for testing."""
        return TemporalBindingParameters(
            field_size=1000003,
            alpha=5,
            max_iterations=100,
            security_param=128
        )
    
    @pytest.fixture
    def stark_params(self):
        """Create STARK parameters for testing."""
        return STARKParameters(
            blowup_factor=4,
            security_param=128,
            fri_folding_factor=2
        )
    
    def test_complete_workflow(self, field, temporal_params, stark_params):
        """Test complete AOW workflow."""
        # Step 1: Create a temporal claim
        x = 123
        iterations = 10
        y = iterate_polynomial(x, temporal_params.alpha, iterations, field)
        
        # Step 2: Verify temporal binding
        assert verify_temporal_binding(x, y, iterations, temporal_params, field)
        
        # Step 3: Generate STARK proof
        proof, public_inputs = generate_stark_proof(
            x=x,
            alpha=temporal_params.alpha,
            iterations=iterations,
            field=field,
            params=stark_params
        )
        
        # Step 4: Verify STARK proof
        assert verify_stark_proof(proof, public_inputs, field, stark_params)
        
        # Step 5: Create event chain
        events = [b"Event 1", b"Event 2", b"Event 3"]
        chain = create_event_chain(events, field, temporal_params.alpha)
        
        # Step 6: Verify chain integrity
        assert chain.verify_chain()
    
    def test_cross_component_interaction(self, field, temporal_params):
        """Test interaction between different AOW components."""
        # Create values using AIIP
        x = 123
        y1 = iterate_polynomial(x, temporal_params.alpha, 10, field)
        y2 = iterate_polynomial(x, temporal_params.alpha, 20, field)
        
        # Verify temporal binding
        assert verify_temporal_binding(x, y1, 10, temporal_params, field)
        assert verify_temporal_binding(x, y2, 20, temporal_params, field)
        
        # Values should be different
        assert y1 != y2
        
        # Create event chain
        events = [b"Event 1", b"Event 2"]
        chain = create_event_chain(events, field, temporal_params.alpha)
        
        # Chain should be valid
        assert chain.verify_chain()