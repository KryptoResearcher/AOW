# AOW Theory Overview

## Introduction

Affine One-Wayness (AOW) is a cryptographic primitive for verifiable temporal ordering based on iterative polynomial evaluation over finite fields. AOW provides strong temporal binding guarantees by reducing its security to the hardness of the Affine Iterated Inversion Problem (AIIP).

## Core Concepts

### Temporal Binding

Temporal binding ensures that:
1. Computation requires sequential steps (cannot be parallelized)
2. Outputs at different depths are unique with high probability
3. Finding preimages is computationally infeasible

### AIIP Problem

The Affine Iterated Inversion Problem (AIIP) asks: given a polynomial \( f \), iteration count \( n \), and target \( y \), find \( x \) such that:
\[ f^{(n)}(x) = y \]

### Security Foundations

AOW's security relies on two complementary foundations:

1. **Multivariate Quadratic (MQ) Hardness**: AIIP reduces to solving systems of multivariate quadratic equations
2. **High-Genus Hyperelliptic Curve DLP**: AIIP embeds into discrete logarithm problems on high-genus hyperelliptic curves

## Mathematical Formulation

For a quadratic polynomial \( f(x) = x^2 + \alpha \) over finite field \( \mathbb{F}_q \), the AOW function is defined as:
\[ \mathsf{AOW}_f^{(n)}(x) = f^{(n)}(x) \]

## Security Parameters

| Security Level | Field Size | Max Iterations |
|----------------|------------|----------------|
| 128-bit        | \( 2^{256} \) | \( 2^{64} \)    |
| 192-bit        | \( 2^{384} \) | \( 2^{96} \)    |
| 256-bit        | \( 2^{512} \) | \( 2^{128} \)   |

## Further Reading

- [Mathematical Foundations](mathematical_foundations.md)
- [Security Properties](security_properties.md)
- [References](references.md)