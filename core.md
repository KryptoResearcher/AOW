### docs/api-reference/
```markdown
# API Reference - Core Module

## Overview

The core module provides fundamental cryptographic operations for AOW, including finite field arithmetic and polynomial iteration.

## FiniteField Class

### Constructor

```python
FiniteField(modulus)

Creates a finite field with the given modulus.

Parameters:

    modulus (int): Prime modulus for the field

Returns: FiniteField instance

Example:
python

field = FiniteField(1000003)

Methods
add(a, b)

Add two field elements.

Parameters:

    a (int): First field element

    b (int): Second field element

Returns: (int) Sum modulo field modulus
sub(a, b)

Subtract two field elements.

Parameters:

    a (int): First field element

    b (int): Second field element

Returns: (int) Difference modulo field modulus
mul(a, b)

Multiply two field elements.

Parameters:

    a (int): First field element

    b (int): Second field element

Returns: (int) Product modulo field modulus
sqr(a)

Square a field element.

Parameters:

    a (int): Field element to square

Returns: (int) Square modulo field modulus
inv(a)

Compute multiplicative inverse of a field element.

Parameters:

    a (int): Field element to invert

Returns: (int) Multiplicative inverse modulo field modulus

Raises: ValueError if a = 0
random_element()

Generate a random field element.

Returns: (int) Random element in [0, modulus-1]
is_quadratic_residue(a)

Check if a field element is a quadratic residue.

Parameters:

    a (int): Field element to check

Returns: (bool) True if a is a quadratic residue, False otherwise
sqrt(a)

Compute square root of a field element if it exists.

Parameters:

    a (int): Field element

Returns: (int or None) Square root if it exists, None otherwise
Properties
modulus

Field modulus.
size

Number of elements in the field (same as modulus).
AIIP Functions
iterate_polynomial(x, alpha, iterations, field)

Compute f^{(n)}(x) where f(x) = x² + α.

Parameters:

    x (int): Input value

    alpha (int): Constant term

    iterations (int): Number of iterations

    field (FiniteField): Finite field instance

Returns: (int) Result of polynomial iteration

Example:
python

result = iterate_polynomial(123, 5, 1000, field)

compute_iteration_trace(x, alpha, iterations, field)

Compute the full trace of polynomial iteration.

Parameters:

    x (int): Input value

    alpha (int): Constant term

    iterations (int): Number of iterations

    field (FiniteField): Finite field instance

Returns: (list) List of all intermediate values

Example:
python

trace = compute_iteration_trace(123, 5, 10, field)
# Returns [x, f(x), f(f(x)), ..., f^{(10)}(x)]

QuadraticPolynomial Class
Constructor
python

QuadraticPolynomial(alpha, field)

Creates a quadratic polynomial f(x) = x² + α.

Parameters:

    alpha (int): Constant term

    field (FiniteField): Finite field instance

Returns: QuadraticPolynomial instance
Methods
evaluate(x)

Evaluate polynomial at point x.

Parameters:

    x (int): Point to evaluate

Returns: (int) f(x) = x² + α
iterate(x, n)

Compute n-th iteration of polynomial.

Parameters:

    x (int): Input value

    n (int): Number of iterations

Returns: (int) f^{(n)}(x)
trace(x, n)

Compute full trace of n iterations.

Parameters:

    x (int): Input value

    n (int): Number of iterations

Returns: (list) List of all intermediate values
Data Classes
AIIPParameters

Dataclass for AIIP parameters.

Attributes:

    field_size (int): Size of finite field

    alpha (int): Constant term

    iterations (int): Number of iterations

    security_param (int): Security parameter (default: 128)

Utility Functions
hash_to_field(data, field)

Hash data to a field element.

Parameters:

    data (bytes or str): Data to hash

    field (FiniteField): Finite field instance

Returns: (int) Field element representation of hash
generate_quadratic_non_residue(field)

Generate a quadratic non-residue in the field.

Parameters:

    field (FiniteField): Finite field instance

Returns: (int) Quadratic non-residue element
calculate_security_parameters(security_level)

Calculate recommended parameters for a given security level.

Parameters:

    security_level (int): Security level in bits (128, 192, or 256)

Returns: (dict) Recommended parameters
Examples
Basic Usage
python

from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial

# Create finite field
field = FiniteField(1000003)

# Compute AOW function
result = iterate_polynomial(123, 5, 1000, field)
print(f"Result: {result}")

Using QuadraticPolynomial
python

from src.core.polynomials import QuadraticPolynomial

# Create polynomial
poly = QuadraticPolynomial(5, field)

# Evaluate and iterate
y = poly.evaluate(123)
z = poly.iterate(123, 1000)
trace = poly.trace(123, 10)

Parameter Calculation
python

from src.utils import calculate_security_parameters

# Get recommended parameters
params = calculate_security_parameters(128)
print(f"Field size: {params['field_size']}")
print(f"Max iterations: {params['max_iterations']}")

Error Handling

Most functions raise standard Python exceptions:

    ValueError: For invalid parameters (e.g., modulus not prime)

    TypeError: For incorrect argument types

    ArithmeticError: For mathematical errors (e.g., division by zero)

Performance Notes

    Field operations are optimized for performance

    Iteration has O(n) time complexity

    Memory usage is O(1) for iteration, O(n) for trace computation

See Also

    Temporal Module

    Proofs Module

    Utils Module


