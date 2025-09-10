# Affine One-Wayness (AOW) - Post-Quantum Temporal Verification

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Research](https://img.shields.io/badge/status-research--implementation-orange)

A reference implementation of **Affine One-Wayness (AOW)**, the reliability component of the broader **CASH framework** (Chaotic Affine Secure Hash). AOW provides transparent post-quantum temporal verification through polynomial iteration over finite fields, enabling Byzantine-resistant event ordering and distributed synchronization with provable security guarantees.

> **Research Implementation Notice**: This project is a theoretical construct and reference implementation intended for research validation. It is not yet audited or ready for production use.

## Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Theoretical Foundations](#-theoretical-foundations)
- [Repository Structure](#-repository-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Examples](#-examples)
- [Benchmarking](#-benchmarking)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Citation](#-citation)

## Overview

The Affine One-Wayness (AOW) primitive addresses the challenge of verifiable temporal ordering in distributed systems without synchronized clocks or trusted authorities. AOW provides strong temporal binding guarantees by reducing its security to the hardness of the Affine Iterated Inversion Problem (AIIP), which possesses dual foundations in multivariate quadratic algebra and the arithmetic of high-genus hyperelliptic curves.

AOW serves as the reliability component of the CASH framework triad:
- **Iron Layer (AOW)**: Temporal reliability and Byzantine resistance
- **Gold Layer (CEE)**: Data confidentiality and entropy preservation  
- **Clay Layer (SH)**: Legal opposability and verifiable interpretation

## Key Features

- **Transparent Setup**: No trusted authorities or hidden parameters required
- **Post-Quantum Security**: Security reductions to AIIP hardness with quantum resistance
- **Efficient Verification**: Native integration with STARK proof systems with O(λ log n) verification complexity
- **Temporal Binding**: Provable sequential computation requirements with depth uniqueness
- **Byzantine Resistance**: Robust event ordering resistant to malicious participants
- **Zero-Knowledge Proofs**: Support for privacy-preserving verification of temporal claims

## Theoretical Foundations

AOW is built upon the **Affine Iterated Inversion Problem (AIIP)** with security reductions to:
1. Multivariate Quadratic (MQ) problem hardness
2. High-genus Hyperelliptic Curve Discrete Logarithm Problem (HCDLP)

The primitive maintains three core temporal verification properties:
1. **Sequential Evaluation**: Ω(n) sequential steps required for evaluation
2. **Depth Uniqueness**: Negligible probability of output collisions at different depths
3. **Inversion Hardness**: Computational infeasibility of finding preimages

Formally, for security parameter λ, field size q = 2²λ, and maximum depth n_max = 2^{λ/2}:
Pr[Adversary wins temporal forgery game] ≤ negl(λ)

## Repository Structure

affine-one-wayness/
├── src/                          # Source code
│   ├── core/                     # Cryptographic operations (AIIP, finite fields)
│   ├── temporal/                 # Temporal binding and verification
│   ├── proofs/                   # STARK proof integration
│   ├── types.py                  # Core data structures
│   └── utils.py                  # Helper functions
├── tests/                        # Comprehensive test suite
│   ├── unit/                     # Unit tests for components
│   ├── property/                 # Property-based tests
│   ├── integration/              # Integration tests
│   └── conftest.py               # Test configuration
├── examples/                     # Practical usage examples
│   ├── basic_iteration.py        # Basic AIIP iteration
│   ├── event_ordering.py         # Byzantine-resistant event ordering
│   ├── stark_proofs.py           # STARK proof generation and verification
│   └── data/                     # Example datasets
├── benchmarks/                   # Performance benchmarking
│   ├── scripts/                  # Benchmarking scripts
│   ├── configurations/           # Parameter configurations
│   ├── results/                  # Benchmark results
│   └── analysis/                 # Result analysis & visualization
├── docs/                         # Comprehensive documentation
│   ├── theory/                   # Theoretical explanations
│   ├── user-guide/               # Usage instructions
│   ├── api-reference/            # API documentation
│   └── tutorials/                # Step-by-step tutorials
├── assets/                       # Resources & templates
│   ├── images/                   # Diagrams & visualizations
│   ├── parameters/               # Parameter sets
│   └── templates/                # Configuration templates
└── README.md                     # This file


## Installation

# Clone the repository
git clone https://github.com/KryptoResearcher/AOW.git
cd AOW

# Install in development mode
pip install -e .

# Install benchmarking dependencies (optional)
pip install -r benchmarks/requirements.txt


## Quick Start


from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.verification import verify_temporal_binding
from src.types import AOWParameters

# Initialize parameters
params = AOWParameters(
    field_size=2**256,   # Field size for 128-bit security
    alpha=5,             # Quadratic non-residue
    iterations=1000,     # Number of iterations
    security_param=128   # Security level
)

# Compute AOW function
field = FiniteField(params.field_size)
result = iterate_polynomial(123456, params.alpha, params.iterations, field)

# Verify temporal binding properties
is_valid = verify_temporal_binding(result, params)
print(f"Temporal binding verified: {is_valid}")


Run the basic example:

python examples/basic_iteration.py


## Examples

The repository includes several practical examples:

1. **Basic Iteration** (`examples/basic_iteration.py`):
   - Demonstrates core AIIP polynomial iteration

2. **Event Ordering** (`examples/event_ordering.py`):
   - Shows Byzantine-resistant temporal event chain construction

3. **STARK Proofs** (`examples/stark_proofs.py`):
   - Demonstrates STARK proof generation and verification for AOW computations

4. **Distributed Synchronization** (`examples/distributed_sync.py`):
   - Example of using AOW for distributed system synchronization

## Benchmarking

The benchmarking suite allows performance assessment across different parameter configurations:


# Run AOW performance benchmarks
python benchmarks/scripts/benchmark_aow.py \
  -c benchmarks/configurations/standard_params.json \
  -o benchmarks/results/current/aow_performance.csv

# Generate performance visualization
python benchmarks/analysis/plot_performance.py \
  -i benchmarks/results/current/aow_performance.csv \
  -o benchmarks/results/current/aow_performance.png \
  -t time

# Generate comprehensive report
python benchmarks/analysis/generate_report.py \
  -c benchmarks/configurations/standard_params.json \
  -i benchmarks/results/current/aow_performance.csv \
  -o benchmarks/results/current/report.md

Pre-configured parameter sets are available for:
- Development testing (`small_params.json`)
- Realistic assessment (`standard_params.json`) 
- Theoretical validation (`theoretical_params.json`)

## Documentation

Comprehensive documentation is available in the `/docs` directory:

- **Theory Guides**: Mathematical foundations and theoretical framework
- **User Guides**: Practical usage instructions and parameter configuration
- **API Reference**: Technical API documentation
- **Tutorials**: Step-by-step walkthroughs of examples

Key documentation files:
- [Theory Overview](/docs/theory/overview.md)
- [Installation Guide](/docs/user-guide/installation.md) 
- [Quick Start Guide](/docs/user-guide/quickstart.md)
- [Parameter Configuration](/docs/user-guide/parameters.md)

## Contributing

As a research implementation, we welcome contributions from the academic community:

1. **Explore the Theory**: Read the accompanying paper and documentation
2. **Experiment with Code**: Run examples and explore the implementation
3. **Identify Issues**: Report bugs or theoretical concerns via GitHub Issues
4. **Suggest Enhancements**: Propose improvements to algorithms or documentation
5. **Submit Pull Requests**: Contribute code improvements or additional examples

Please see our [Contributing Guidelines](docs/contributing.md) and [Research Statement](docs/research.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this implementation in academic work, please cite the accompanying paper:

@article{aow2025,
  title={The Affine One-Wayness (AOW): A Transparent Post-Quantum Temporal Verification via Polynomial Iteration},
  author={anonymised for doubleblind review},
  journal={anonymised for doubleblind review},
  year={2025},
  publisher={anonymised for doubleblind review}
}

## Roadmap

Future work includes:

1. **Performance Optimization**: Migration of performance-critical components to Rust
2. **STARK Integration**: Full integration with a production-grade STARK prover
3. **Additional Polynomial Families**: Support for broader polynomial families beyond quadratic maps
4. **Formal Verification**: Application of formal methods to verify implementation correctness
5. **Community Engagement**: Collaboration with distributed systems and cryptographic research communities

---

For questions and discussions, please open an issue on GitHub or contact the research team at krytoresearcher@proton.me.