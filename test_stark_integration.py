"""
Integration tests for STARK proof integration.
"""

import pytest
from src.core.fields import FiniteField
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters

class TestSTARKIntegration:
    """Integration tests for STARK proof system."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def params(self):
        """Create STARK parameters for testing."""
        return STARKParameters(
            blowup_factor=4,
            security_param=128,
            fri_folding_factor=2
        )
    
    def test_stark_proof_generation(self, field, params):
        """Test STARK proof generation."""
        proof, public_inputs = generate_stark_proof(
            x=123,
            alpha=5,
            iterations=10,
            field=field,
            params=params
        )
        
        # Proof should have expected structure
        assert 'trace_length' in proof
        assert 'trace_commitment' in proof
        assert 'fri_layers' in proof
        assert 'queries' in proof
        
        # Public inputs should have expected structure
        assert 'input' in public_inputs
        assert 'output' in public_inputs
        assert 'iterations' in public_inputs
    
    def test_stark_proof_verification(self, field, params):
        """Test STARK proof verification."""
        proof, public_inputs = generate_stark_proof(
            x=123,
            alpha=5,
            iterations=10,
            field=field,
            params=params
        )
        
        # Proof should verify successfully
        assert verify_stark_proof(proof, public_inputs, field, params)
        
        # Tampered proof should not verify
        proof['trace_length'] += 1
        assert not verify_stark_proof(proof, public_inputs, field, params)