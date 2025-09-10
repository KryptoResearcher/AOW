# Parameter Selection Guide

## Introduction

This guide explains how to choose appropriate parameters for AOW based on your security requirements and performance constraints.

## Security Levels

AOW supports three standard security levels:

### 128-bit Security

```python
parameters = {
    "field_size": 2**256,       # 256-bit field
    "alpha": 5,                 # Quadratic non-residue
    "max_iterations": 2**64,    # 64-bit iteration bound
    "security_param": 128       # 128-bit security
}

192-bit Security
python

parameters = {
    "field_size": 2**384,       # 384-bit field
    "alpha": 5,                 # Quadratic non-residue
    "max_iterations": 2**96,    # 96-bit iteration bound
    "security_param": 192       # 192-bit security
}

256-bit Security
python

parameters = {
    "field_size": 2**512,       # 512-bit field
    "alpha": 5,                 # Quadratic non-residue
    "max_iterations": 2**128,   # 128-bit iteration bound
    "security_param": 256       # 256-bit security
}

Parameter Definitions
Field Size (qq)

The size of the finite field FqFq​. Larger fields provide higher security but require more computation.

Recommendation: q≥22λq≥22λ for λλ-bit security
Alpha (αα)

The constant term in the quadratic polynomial f(x)=x2+αf(x)=x2+α. Must be a quadratic non-residue in FqFq​.

Recommendation: Use a fixed value that's known to be a quadratic non-residue
Maximum Iterations (nmax⁡nmax​)

The maximum number of iterations allowed. Affects the security reduction tightness.

Recommendation: nmax⁡=2λ/2nmax​=2λ/2 for λλ-bit security
Security Parameter (λλ)

The target security level in bits. Determines all other parameters.

Recommendation: Use 128-bit for most applications, 256-bit for long-term security
Performance Considerations
Computation Time

AOW iteration time scales linearly with the number of iterations:
T(n)=O(n)
T(n)=O(n)
Memory Usage

Basic iteration uses constant memory O(1)O(1). Trace computation uses O(n)O(n) memory.
Proof Size

STARK proof size scales as:
S(n)=O(λlog⁡n)
S(n)=O(λlogn)
Verification Time

STARK verification time scales as:
V(n)=O(λlog⁡n)
V(n)=O(λlogn)
Choosing Iteration Count

The iteration count nn determines:

    Sequentiality: Minimum time required for computation

    Security: Resistance to parallel attacks

Recommendation: Choose nn based on your time requirements:

    n=220n=220 (~1 million): ~1 second on modern hardware

    n=230n=230 (~1 billion): ~15 minutes on modern hardware

Field Selection
Prime Fields

Prime fields FpFp​ are recommended for efficiency:

    Use primes of the form p=2k−cp=2k−c for small cc

    Enables efficient modular reduction

Extension Fields

Extension fields FpkFpk​ can be used for specific applications:

    Require more complex arithmetic

    May offer performance benefits for certain operations

Security Trade-offs
Field Size vs. Iteration Count

Increasing field size provides better security against algebraic attacks but increases computation cost per iteration.

Increasing iteration count provides better sequentiality but may weaken the security reduction.
Quantum Resistance

For quantum resistance, use at least 256-bit security parameters:

    Field size: 25122512

    Iteration count: 21282128

Practical Examples
Example 1: Blockchain Consensus
python

# Moderate security, fast verification
params = {
    "field_size": 2**256,
    "alpha": 5,
    "iterations": 2**20,  # ~1 million iterations
    "security_param": 128
}

Example 2: Long-Term Storage
python

# High security, slower computation
params = {
    "field_size": 2**512,
    "alpha": 5,
    "iterations": 2**30,  # ~1 billion iterations
    "security_param": 256
}

Example 3: Testing and Development
python

# Low security, fast computation
params = {
    "field_size": 1000003,  # Small prime
    "alpha": 5,
    "iterations": 1000,
    "security_param": 80
}

Validation and Testing

Always validate your parameter choices:

    Security Analysis: Ensure parameters meet security requirements

    Performance Testing: Benchmark with expected workloads

    Compatibility Testing: Verify with all system components

Tools and Utilities

Use the provided utilities to help with parameter selection:
python

from src.utils import calculate_security_parameters

# Get recommended parameters for 128-bit security
params = calculate_security_parameters(128)
print(params)

Further Reading

    Theory Overview

    Security Properties

    API Reference

