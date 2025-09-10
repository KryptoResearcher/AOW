#!/usr/bin/env python3
"""
Benchmark script for temporal binding verification performance.
"""

import time
import json
import argparse
import csv
from pathlib import Path
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.temporal.binding import verify_temporal_binding, TemporalBindingParameters

def benchmark_temporal_verification(field_size, alpha, max_iterations, num_trials=10):
    """Benchmark temporal binding verification performance."""
    field = FiniteField(field_size)
    params = TemporalBindingParameters(
        field_size=field_size,
        alpha=alpha,
        max_iterations=max_iterations,
        security_param=128
    )
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'max_iterations': max_iterations,
        'trials': [],
        'average_time': 0,
        'min_time': float('inf'),
        'max_time': 0
    }
    
    for i in range(num_trials):
        # Generate random input and compute result
        x = field.random_element()
        iterations = max_iterations // 2  # Use half the max iterations
        y = iterate_polynomial(x, alpha, iterations, field)
        
        # Time the verification
        start_time = time.time()
        is_valid = verify_temporal_binding(x, y, iterations, params, field)
        end_time = time.time()
        
        verification_time = end_time - start_time
        
        results['trials'].append({
            'trial': i + 1,
            'input': x,
            'output': y,
            'iterations': iterations,
            'valid': is_valid,
            'time': verification_time
        })
        
        results['average_time'] += verification_time
        results['min_time'] = min(results['min_time'], verification_time)
        results['max_time'] = max(results['max_time'], verification_time)
    
    results['average_time'] /= num_trials
    
    return results

def benchmark_depth_uniqueness(field_size, alpha, max_iterations, num_pairs=1000):
    """Benchmark depth uniqueness probability calculation."""
    field = FiniteField(field_size)
    params = TemporalBindingParameters(
        field_size=field_size,
        alpha=alpha,
        max_iterations=max_iterations,
        security_param=128
    )
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'max_iterations': max_iterations,
        'pairs': [],
        'average_probability': 0,
        'min_probability': float('inf'),
        'max_probability': 0
    }
    
    from src.temporal.binding import depth_uniqueness_probability
    
    start_time = time.time()
    
    for i in range(num_pairs):
        # Generate random iteration counts
        n = i % max_iterations + 1
        m = (i * 3) % max_iterations + 1
        
        # Calculate probability
        prob = depth_uniqueness_probability(n, m, params)
        
        results['pairs'].append({
            'pair': i + 1,
            'n': n,
            'm': m,
            'probability': prob
        })
        
        results['average_probability'] += prob
        results['min_probability'] = min(results['min_probability'], prob)
        results['max_probability'] = max(results['max_probability'], prob)
    
    end_time = time.time()
    
    results['average_probability'] /= num_pairs
    results['computation_time'] = end_time - start_time
    
    return results

def main():
    """Run temporal binding benchmarks."""
    parser = argparse.ArgumentParser(description='Benchmark temporal binding performance')
    parser.add_argument('-c', '--config', required=True, help='Configuration file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-t', '--type', choices=['verification', 'uniqueness'], default='verification', 
                       help='Benchmark type')
    parser.add_argument('-n', '--trials', type=int, default=10, help='Number of trials/pairs')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Run benchmark
    if args.type == 'verification':
        results = benchmark_temporal_verification(
            config['field_size'],
            config['alpha'],
            config['max_iterations'],
            args.trials
        )
    else:
        results = benchmark_depth_uniqueness(
            config['field_size'],
            config['alpha'],
            config['max_iterations'],
            args.trials
        )
    
    # Save results
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Also save as CSV for easier analysis
    csv_path = output_path.with_suffix('.csv')
    with open(csv_path, 'w', newline='') as f:
        if args.type == 'verification':
            writer = csv.writer(f)
            writer.writerow(['field_size', 'alpha', 'max_iterations', 'trial', 'time'])
            
            for trial in results['trials']:
                writer.writerow([
                    results['field_size'],
                    results['alpha'],
                    results['max_iterations'],
                    trial['trial'],
                    trial['time']
                ])
        else:
            writer = csv.writer(f)
            writer.writerow(['field_size', 'alpha', 'max_iterations', 'pair', 'n', 'm', 'probability'])
            
            for pair in results['pairs']:
                writer.writerow([
                    results['field_size'],
                    results['alpha'],
                    results['max_iterations'],
                    pair['pair'],
                    pair['n'],
                    pair['m'],
                    pair['probability']
                ])
    
    print(f"Benchmark completed. Results saved to {args.output} and {csv_path}")
    
    if args.type == 'verification':
        print(f"Average verification time: {results['average_time']:.6f} seconds")
    else:
        print(f"Average probability: {results['average_probability']:.6f}")
        print(f"Computation time: {results['computation_time']:.6f} seconds")

if __name__ == "__main__":
    main()