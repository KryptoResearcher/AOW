# API Reference - Utils Module

## Overview

The utils module provides utility functions and data structures for AOW.

## Data Classes

### AOWParameters
Dataclass for AOW parameters.

**Attributes**:
- `field_size` (int): Size of finite field
- `alpha` (int): Constant term
- `iterations` (int): Number of iterations
- `security_param` (int): Security parameter (default: 128)

### TemporalClaim
Dataclass representing a temporal claim with proof.

**Attributes**:
- `input_value` (int): Input value
- `output_value` (int): Output value
- `iterations` (int): Number of iterations
- `proof` (dict or None): Optional proof

### EventOrdering
Dataclass representing event ordering with temporal guarantees.

**Attributes**:
- `events` (list): List of events
- `temporal_proofs` (list): List of temporal proofs
- `chain_hash` (bytes): Hash of the event chain

## Utility Functions

### hash_to_field(data, field)
Hash data to a field element.

**Parameters**:
- `data` (bytes or str): Data to hash
- `field` (FiniteField): Finite field instance

**Returns**: (int) Field element representation of hash

**Example**:
```python
from src.utils import hash_to_field

field_element = hash_to_field(b"hello world", field)

generate_quadratic_non_residue(field)

Generate a quadratic non-residue in the field.

Parameters:

    field (FiniteField): Finite field instance

Returns: (int) Quadratic non-residue element

Example:
python

from src.utils import generate_quadratic_non_residue

alpha = generate_quadratic_non_residue(field)

calculate_security_parameters(security_level)

Calculate recommended parameters for a given security level.

Parameters:

    security_level (int): Security level in bits (128, 192, or 256)

Returns: (dict) Recommended parameters

Example:
python

from src.utils import calculate_security_parameters

params = calculate_security_parameters(128)
print(f"Field size: {params['field_size']}")
print(f"Max iterations: {params['max_iterations']}")

Helper Functions
validate_parameters(params)

Validate AOW parameters.

Parameters:

    params (dict or AOWParameters): Parameters to validate

Returns: (bool) True if parameters are valid

Raises: ValueError if parameters are invalid
create_temporal_claim(x, alpha, iterations, field)

Create a temporal claim with optional proof.

Parameters:

    x (int): Input value

    alpha (int): Constant term

    iterations (int): Number of iterations

    field (FiniteField): Finite field instance

    include_proof (bool): Whether to include proof (default: False)

Returns: (TemporalClaim) Temporal claim
Examples
Parameter Calculation
python

from src.utils import calculate_security_parameters

# Get recommended parameters for different security levels
params_128 = calculate_security_parameters(128)
params_192 = calculate_security_parameters(192)
params_256 = calculate_security_parameters(256)

Hash to Field
python

from src.utils import hash_to_field

# Hash different types of data
hash1 = hash_to_field(b"binary data", field)
hash2 = hash_to_field("string data", field)
hash3 = hash_to_field(str(12345).encode(), field)

Parameter Validation
python

from src.utils import validate_parameters, AOWParameters

# Create parameters
params = AOWParameters(
    field_size=1000003,
    alpha=5,
    iterations=1000,
    security_param=128
)

# Validate parameters
is_valid = validate_parameters(params)
if is_valid:
    print("Parameters are valid")
else:
    print("Parameters are invalid")

Error Handling

    ValueError: For invalid parameters or inputs

    TypeError: For incorrect argument types

    SecurityError: For security-related issues (custom exception)

Performance Notes

    Utility functions are designed for efficiency

    Parameter validation has minimal overhead

    Hashing uses cryptographic hash functions (SHA-256)

Security Notes

    Uses cryptographically secure hash functions

    Validates parameters to ensure security properties

    Generates proper quadratic non-residues for security

See Also

    Core Module

    Temporal Module

    Proofs Module