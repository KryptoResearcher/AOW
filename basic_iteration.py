#!/usr/bin/env python3
"""
Basic example of AOW polynomial iteration.
"""

import time
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial, compute_iteration_trace
from src.utils import calculate_security_parameters

def main():
    """Demonstrate basic AOW iteration."""
    print("=== AOW Basic Iteration Example ===\n")
    
    # Get recommended parameters for 128-bit security
    params = calculate_security_parameters(128)
    field = FiniteField(params['field_size'])
    
    print(f"Using field size: {params['field_size']}")
    print(f"Using alpha: {params['alpha']}")
    print(f"Using iterations: {params['max_iterations']}")
    
    # Generate a random input
    x = field.random_element()
    print(f"\nRandom input value: {x}")
    
    # Time the iteration
    start_time = time.time()
    result = iterate_polynomial(x, params['alpha'], params['max_iterations'], field)
    end_time = time.time()
    
    print(f"Result after {params['max_iterations']} iterations: {result}")
    print(f"Computation time: {end_time - start_time:.4f} seconds")
    
    # Show a small trace for demonstration
    print("\nFirst 5 iterations (for demonstration):")
    small_trace = compute_iteration_trace(x, params['alpha'], 5, field)
    for i, value in enumerate(small_trace):
        print(f"  f^({i})(x) = {value}")
    
    # Demonstrate temporal binding verification
    print(f"\nVerifying temporal binding for {params['max_iterations']} iterations:")
    from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters
    
    temporal_params = TemporalBindingParameters(
        field_size=params['field_size'],
        alpha=params['alpha'],
        max_iterations=params['max_iterations'],
        security_param=128
    )
    
    is_valid = verify_temporal_binding(x, result, params['max_iterations'], temporal_params, field)
    print(f"Temporal binding verified: {is_valid}")

if __name__ == "__main__":
    main()