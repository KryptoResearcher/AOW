# Mathematical Foundations

## Finite Field Arithmetic

AOW operates over finite fields \( \mathbb{F}_q \) where \( q = p^k \) is a prime power. The implementation uses:

- Modular arithmetic operations
- Efficient squaring and inversion
- Quadratic residue testing

## Polynomial Iteration

The core operation is iterated polynomial evaluation:
\[ f^{(0)}(x) = x \]
\[ f^{(n)}(x) = f(f^{(n-1)}(x)) \]

For quadratic polynomials \( f(x) = x^2 + \alpha \), the degree grows exponentially:
\[ \deg(f^{(n)}) = 2^n \]

## Cycle Structure

Quadratic polynomials over finite fields have specific cycle structures:

- Expected cycle length: \( \Theta(\sqrt{q}) \)
- Number of cycles: \( \Theta(\log q) \)
- Preimage tree structure

## Algebraic Properties

### Composition

Iterated composition exhibits algebraic properties:
\[ f^{(m+n)}(x) = f^{(m)}(f^{(n)}(x)) \]

### Fixed Points

Points where \( f(x) = x \) form the basis of cycle structures.

### Functional Graphs

The iteration structure forms functional graphs with:
- Cycles of various lengths
- Trees feeding into cycles

## Reduction to Hard Problems

### MQ Reduction

AIIP reduces to solving systems of \( O(2^n) \) multivariate quadratic equations.

### HCDLP Reduction

For \( f(x) = x^2 + \alpha \) with \( \alpha \) a quadratic non-residue, AIIP embeds into DLP on hyperelliptic curves of genus \( g = 2^{n-1} - 1 \).

## Complexity Analysis

### Time Complexity

- Evaluation: \( O(n) \) field operations
- Preimage finding: \( O(2^n) \) operations (conjectured)

### Space Complexity

- Evaluation: \( O(1) \) space
- Preimage finding: \( O(2^{n/2}) \) space for meet-in-middle

## References

See [References](references.md) for detailed mathematical sources.