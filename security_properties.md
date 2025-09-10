# Security Properties

## Computational Hardness

### AIIP Hardness Assumption

For appropriate parameters, no probabilistic polynomial-time algorithm can solve AIIP with non-negligible probability.

### Concrete Security

With \( q = 2^{2\lambda} \) and \( n = \lambda \):
- Classical security: \( \Omega(2^\lambda) \) operations
- Quantum security: \( \Omega(2^{\lambda/2}) \) operations (against generic quantum attacks)

## Temporal Binding Properties

### Sequential Evaluation

Computing \( f^{(n)}(x) \) requires \( \Omega(n) \) sequential steps:
- Each iteration depends on the previous result
- No known parallelization strategy

### Depth Uniqueness

For \( n \neq m \leq n_{\max} \):
\[ \Pr_{x \leftarrow \mathbb{F}_q}[f^{(n)}(x) = f^{(m)}(x)] \leq \frac{(m-n) \cdot 2^{m-n}}{q} \]

### Inversion Hardness

Finding preimages is computationally infeasible under the AIIP hardness assumption.

## Attack Resistance

### Algebraic Attacks

- High degree (\( 2^n \)) prevents algebraic manipulation
- Linearization requires handling \( O(2^n) \) monomials

### Cycle Attacks

- Expected cycle length \( \Theta(\sqrt{q}) \) provides resistance
- Cycle finding requires \( \Omega(\sqrt{q}) \) operations

### Meet-in-Middle Attacks

- Requires \( O(\sqrt{q}) \) storage
- For \( q = 2^{256} \), requires \( O(2^{128}) \) storage (infeasible)

### Quantum Attacks

#### Grover's Algorithm

- Provides quadratic speedup \( O(\sqrt{q}) \)
- Each iteration requires \( O(n) \) operations
- Total time \( O(n \cdot \sqrt{q}) \) remains exponential

#### Quantum Algebraic Attacks

- No known exponential speedup for high-degree polynomials
- Linearization still requires exponential resources

## Reduction Security

### Security Reduction

Any adversary breaking temporal binding can solve AIIP with comparable advantage:
\[ \Pr[\text{Break}] \leq n_{\max} \cdot \Pr[\text{Solve AIIP}] \]

### Parameter Selection

Parameters are chosen such that \( n_{\max} \cdot \epsilon \leq \negl(\lambda) \) for AIIP advantage \( \epsilon \).

## Post-Quantum Security

AOW provides post-quantum security based on:
1. MQ problem hardness (quantum-resistant)
2. High-genus HCDLP hardness (quantum-resistant)

## Implementation Security

### Side-Channel Resistance

- Constant-time field arithmetic
- Protection against timing attacks

### Randomness Requirements

- Proper generation of quadratic non-residues
- Secure random number generation

## Security Proofs

Formal security proofs are provided in the accompanying paper:
- Temporal binding theorem
- Security reduction to AIIP
- Quantum resistance analysis