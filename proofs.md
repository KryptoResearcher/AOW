# API Reference - Proofs Module

## Overview

The proofs module provides functionality for STARK proof generation and verification.

## STARK Proofs

### generate_stark_proof(x, alpha, iterations, field, params)
Generate a STARK proof for AOW computation.

**Parameters**:
- `x` (int): Input value
- `alpha` (int): Constant term
- `iterations` (int): Number of iterations
- `field` (FiniteField): Finite field instance
- `params` (STARKParameters): STARK parameters

**Returns**: (tuple) Proof and public inputs

**Example**:
```python
from src.proofs.stark import generate_stark_proof, STARKParameters

stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

proof, public_inputs = generate_stark_proof(
    x, alpha, iterations, field, stark_params
)

verify_stark_proof(proof, public_inputs, field, params)

Verify a STARK proof for AOW computation.

Parameters:

    proof (dict): STARK proof

    public_inputs (dict): Public inputs to verification

    field (FiniteField): Finite field instance

    params (STARKParameters): STARK parameters

Returns: (bool) True if verification succeeds, False otherwise

Example:
python

from src.proofs.stark import verify_stark_proof

is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)

Data Classes
STARKParameters

Dataclass for STARK parameters.

Attributes:

    blowup_factor (int): Blowup factor for proof system (default: 4)

    security_param (int): Security parameter (default: 128)

    fri_folding_factor (int): FRI folding factor (default: 2)

Proof Structure

The STARK proof has the following structure:
python

{
    "trace_length": int,          # Length of execution trace
    "trace_commitment": str,      # Commitment to execution trace
    "fri_layers": int,            # Number of FRI layers
    "queries": int                # Number of query points
}

Public Inputs Structure

The public inputs have the following structure:
python

{
    "input": int,                 # Input value
    "output": int,                # Output value
    "iterations": int             # Number of iterations
}

Examples
Basic Proof Generation
python

from src.proofs.stark import generate_stark_proof, STARKParameters

# Set up STARK parameters
stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

# Generate proof
proof, public_inputs = generate_stark_proof(
    x, alpha, iterations, field, stark_params
)

print(f"Proof size: {len(str(proof))} characters")
print(f"Public inputs: {public_inputs}")

Proof Verification
python

from src.proofs.stark import verify_stark_proof

# Verify proof
is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)

if is_valid:
    print("Proof is valid")
else:
    print("Proof is invalid")

Batch Proof Generation
python

def batch_proof_generation(inputs, alpha, iterations, field, stark_params):
    """Generate proofs for multiple inputs."""
    proofs = []
    public_inputs_list = []
    
    for x in inputs:
        proof, public_inputs = generate_stark_proof(
            x, alpha, iterations, field, stark_params
        )
        proofs.append(proof)
        public_inputs_list.append(public_inputs)
    
    return proofs, public_inputs_list

Error Handling

    ValueError: For invalid parameters (e.g., iterations too large)

    TypeError: For incorrect argument types

    ProofGenerationError: For errors during proof generation (custom exception)

    ProofVerificationError: For errors during proof verification (custom exception)

Performance Notes

    Proof generation time: O(n log n)

    Proof verification time: O(λ log n)

    Proof size: O(λ log n)

Security Notes

    Proofs are zero-knowledge: they reveal no information about the input beyond the output

    Proof soundness relies on cryptographic commitments and FRI protocol

    Security parameter determines the number of queries and soundness level

See Also

    Core Module

    Temporal Module

    Utils Module
