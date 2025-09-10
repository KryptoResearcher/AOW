
# Tutorial: STARK Proofs with AOW

## Introduction

This tutorial will guide you through generating and verifying STARK proofs for AOW computations.

## Prerequisites

- Completion of [Basic Usage Tutorial](basic_usage.md)
- Understanding of zero-knowledge proof concepts

## Step 1: Import Required Modules

```python
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters

Step 2: Initialize Parameters
python

# Get recommended parameters
params = calculate_security_parameters(128)
field = FiniteField(params['field_size'])
alpha = params['alpha']
iterations = 1000  # Use smaller iterations for demonstration

# Set up STARK parameters
stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

print(f"Using field size: {params['field_size']}")
print(f"Using iterations: {iterations}")

Step 3: Perform AOW Computation
python

# Generate input and compute result
x = field.random_element()
result = iterate_polynomial(x, alpha, iterations, field)

print(f"Input: {x}")
print(f"Result: {result}")
print(f"Iterations: {iterations}")

Step 4: Generate STARK Proof
python

# Generate STARK proof
print("Generating STARK proof...")
proof, public_inputs = generate_stark_proof(
    x, alpha, iterations, field, stark_params
)

print(f"Proof generated successfully")
print(f"Proof keys: {list(proof.keys())}")
print(f"Public inputs: {public_inputs}")

Step 5: Verify STARK Proof
python

# Verify STARK proof
print("Verifying STARK proof...")
is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)

print(f"Proof valid: {is_valid}")

Step 6: Examine Proof Structure
python

# Examine proof structure
print("\nProof structure:")
print(f"Trace length: {proof.get('trace_length', 'N/A')}")
print(f"Trace commitment: {proof.get('trace_commitment', 'N/A')[:20]}... (truncated)")
print(f"FRI layers: {proof.get('fri_layers', 'N/A')}")
print(f"Queries: {proof.get('queries', 'N/A')}")

print("\nPublic inputs:")
print(f"Input: {public_inputs.get('input', 'N/A')}")
print(f"Output: {public_inputs.get('output', 'N/A')}")
print(f"Iterations: {public_inputs.get('iterations', 'N/A')}")

Step 7: Test Proof Verification
python

# Test with tampered proof
print("\nTesting with tampered proof...")

# Tamper with the proof
tampered_proof = proof.copy()
tampered_proof['trace_length'] = proof['trace_length'] + 1

# Verify tampered proof
is_tampered_valid = verify_stark_proof(tampered_proof, public_inputs, field, stark_params)
print(f"Tampered proof valid: {is_tampered_valid}")  # Should be False

# Test with tampered public inputs
print("Testing with tampered public inputs...")
tampered_public_inputs = public_inputs.copy()
tampered_public_inputs['output'] = public_inputs['output'] + 1

is_tampered_inputs_valid = verify_stark_proof(proof, tampered_public_inputs, field, stark_params)
print(f"Proof with tampered inputs valid: {is_tampered_inputs_valid}")  # Should be False

Step 8: Performance Testing
python

# Test performance with different iteration counts
print("\nTesting performance with different iteration counts:")

import time

for test_iterations in [100, 1000, 10000]:
    print(f"\nTesting with {test_iterations} iterations:")
    
    # Generate input
    test_x = field.random_element()
    
    # Time proof generation
    start_time = time.time()
    test_proof, test_public_inputs = generate_stark_proof(
        test_x, alpha, test_iterations, field, stark_params
    )
    gen_time = time.time() - start_time
    
    # Time proof verification
    start_time = time.time()
    is_valid = verify_stark_proof(test_proof, test_public_inputs, field, stark_params)
    ver_time = time.time() - start_time
    
    print(f"  Proof generation time: {gen_time:.4f}s")
    print(f"  Proof verification time: {ver_time:.4f}s")
    print(f"  Proof valid: {is_valid}")
    print(f"  Proof size: {len(str(test_proof))} characters")

Step 9: Batch Proof Generation
python

# Generate proofs for multiple inputs
print("\nGenerating proofs for multiple inputs...")

batch_inputs = [field.random_element() for _ in range(3)]
proofs = []
public_inputs_list = []

for i, batch_x in enumerate(batch_inputs):
    print(f"Generating proof for input {i+1}...")
    proof, public_inputs = generate_stark_proof(
        batch_x, alpha, iterations, field, stark_params
    )
    proofs.append(proof)
    public_inputs_list.append(public_inputs)

# Verify all proofs
print("Verifying all proofs...")
for i, (proof, public_inputs) in enumerate(zip(proofs, public_inputs_list)):
    is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)
    print(f"Proof {i+1} valid: {is_valid}")

Step 10: Real-World Example
python

# Real-world example: verifiable computation
print("\nReal-world example: Verifiable computation")

# Simulate a meaningful computation
# In practice, this could be a complex computation whose result is expensive to verify
computation_input = 12345  # Meaningful input
computation_result = iterate_polynomial(computation_input, alpha, iterations, field)

print(f"Computation input: {computation_input}")
print(f"Computation result: {computation_result}")

# Generate proof that the computation was performed correctly
proof, public_inputs = generate_stark_proof(
    computation_input, alpha, iterations, field, stark_params
)

# Anyone can verify the proof without redoing the computation
is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)

print(f"Proof of computation valid: {is_valid}")
print("Verifier can trust the result without performing the computation!")

Complete Example
python

# tutorial_stark_proofs.py
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters
import time

# Initialize parameters
params = calculate_security_parameters(128)
field = FiniteField(params['field_size'])
alpha = params['alpha']
iterations = 1000

stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

# Generate input and compute result
x = field.random_element()
result = iterate_polynomial(x, alpha, iterations, field)

# Generate and verify proof
proof, public_inputs = generate_stark_proof(
    x, alpha, iterations, field, stark_params
)

is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)

print(f"Proof valid: {is_valid}")

Next Steps

Now that you've completed the STARK proofs tutorial:

    Explore the distributed synchronization tutorial for multi-party applications

    Learn about advanced usage for optimization techniques

    Read about zero-knowledge properties in the theory section

    Check the API reference for detailed documentation

Real-World Applications

STARK proofs with AOW can be used for:

    Verifiable computation: Prove correct execution of expensive computations

    Blockchain scaling: Offload computation with succinct proofs

    Privacy-preserving protocols: Prove statements without revealing inputs

    Audit systems: Provide cryptographic proof of correct operation

Further Reading

    STARK Proof Theory

    API Reference

    Advanced Usage Guide
