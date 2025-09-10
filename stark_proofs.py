#!/usr/bin/env python3
"""
Example of STARK proof generation and verification for AOW.
"""

import time
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters

def main():
    """Demonstrate STARK proof generation and verification."""
    print("=== AOW STARK Proof Example ===\n")
    
    # Get recommended parameters
    params = calculate_security_parameters(128)
    field = FiniteField(params['field_size'])
    
    # Use a smaller iteration count for demonstration
    iterations = 100
    x = field.random_element()
    
    print(f"Using field size: {params['field_size']}")
    print(f"Using alpha: {params['alpha']}")
    print(f"Using iterations: {iterations}")
    print(f"Input value: {x}")
    
    # Compute the result
    result = iterate_polynomial(x, params['alpha'], iterations, field)
    print(f"Result: {result}")
    
    # Generate STARK proof
    stark_params = STARKParameters(
        blowup_factor=4,
        security_param=128,
        fri_folding_factor=2
    )
    
    print("\nGenerating STARK proof...")
    start_time = time.time()
    proof, public_inputs = generate_stark_proof(
        x, params['alpha'], iterations, field, stark_params
    )
    proof_time = time.time() - start_time
    
    print(f"Proof generated in {proof_time:.4f} seconds")
    print(f"Proof size: {len(str(proof))} characters (simulated)")
    print(f"Public inputs: {public_inputs}")
    
    # Verify STARK proof
    print("\nVerifying STARK proof...")
    start_time = time.time()
    is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)
    verify_time = time.time() - start_time
    
    print(f"Proof verified in {verify_time:.4f} seconds")
    print(f"Proof valid: {is_valid}")
    
    # Demonstrate proof tampering detection
    print("\n=== Testing Proof Tampering Detection ===")
    
    # Tamper with the proof
    tampered_proof = proof.copy()
    tampered_proof['trace_length'] += 1  # Modify a proof attribute
    
    # Attempt to verify the tampered proof
    is_tampered_valid = verify_stark_proof(tampered_proof, public_inputs, field, stark_params)
    print(f"Tampered proof valid: {is_tampered_valid}")

if __name__ == "__main__":
    main()