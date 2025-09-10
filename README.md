
assets/parameters/README.md
markdown

# AOW Parameter Sets

This directory contains pre-configured parameter sets for different security levels.

## Parameter Files

### params_128.json
Parameters for 128-bit security level. Suitable for most applications with moderate security requirements.

### params_192.json
Parameters for 192-bit security level. Provides enhanced security for sensitive applications.

### params_256.json
Parameters for 256-bit security level. Maximum security for long-term protection and high-value applications.

## Parameter Descriptions

### Field Parameters
- `field_size`: The size of the finite field (prime modulus)
- `field_type`: Type of field (currently only "prime" supported)
- `alpha`: Constant term in the polynomial f(x) = x² + α
- `alpha_type`: Specifies that α is a quadratic non-residue

### Iteration Parameters
- `max_iterations`: Maximum allowed iterations for security reasons
- `recommended_iterations`: Recommended iteration count for typical use

### STARK Parameters
- `blowup_factor`: Blowup factor for STARK proof system
- `security_param`: Security parameter for STARK proofs
- `fri_folding_factor`: FRI folding factor
- `num_queries`: Number of query points for proof verification

### Performance Characteristics
Estimated performance metrics for planning purposes:
- `iteration_time_ms`: Average time per iteration in milliseconds
- `verification_time_ms`: Average verification time in milliseconds
- `proof_size_bytes`: Estimated proof size in bytes

## Usage

To use these parameters in your code:

```python
import json
from src.core.fields import FiniteField

# Load parameters
with open('assets/parameters/params_128.json', 'r') as f:
    params = json.load(f)

# Create field
field = FiniteField(params['field_size'])

# Use parameters
alpha = params['alpha']
iterations = params['recommended_iterations']

Customization

You can create custom parameter sets by modifying these files. Ensure that:

    The field size provides adequate security for your needs

    α is a quadratic non-residue in the chosen field

    Iteration counts are within reasonable limits for your application

Security Notes

    These parameters are provided as examples and should be validated for your specific use case

    Always use cryptographically secure random number generation

    Regularly update parameters as computational capabilities improve

Performance Testing

Use the benchmarking tools to test performance with these parameters:
bash

python benchmarks/scripts/benchmark_aiip.py \
  -c assets/parameters/params_128.json \
  -o benchmarks/results/aiip_128.json

