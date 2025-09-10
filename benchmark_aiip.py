#!/usr/bin/env python3
"""
Benchmark script for AIIP polynomial iteration performance.
"""

import time
import json
import argparse
import csv
from pathlib import Path
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial, compute_iteration_trace

def benchmark_aiip_iteration(field_size, alpha, iterations, num_trials=10):
    """Benchmark AIIP iteration performance."""
    field = FiniteField(field_size)
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'iterations': iterations,
        'trials': [],
        'average_time': 0,
        'min_time': float('inf'),
        'max_time': 0
    }
    
    for i in range(num_trials):
        # Generate random input
        x = field.random_element()
        
        # Time the iteration
        start_time = time.time()
        result = iterate_polynomial(x, alpha, iterations, field)
        end_time = time.time()
        
        iteration_time = end_time - start_time
        
        results['trials'].append({
            'trial': i + 1,
            'input': x,
            'output': result,
            'time': iteration_time
        })
        
        results['average_time'] += iteration_time
        results['min_time'] = min(results['min_time'], iteration_time)
        results['max_time'] = max(results['max_time'], iteration_time)
    
    results['average_time'] /= num_trials
    
    return results

def benchmark_aiip_trace(field_size, alpha, iterations, num_trials=5):
    """Benchmark AIIP trace computation performance."""
    field = FiniteField(field_size)
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'iterations': iterations,
        'trials': [],
        'average_time': 0,
        'min_time': float('inf'),
        'max_time': 0,
        'memory_usage': iterations * 8  # Estimate memory usage (bytes)
    }
    
    for i in range(num_trials):
        # Generate random input
        x = field.random_element()
        
        # Time the trace computation
        start_time = time.time()
        trace = compute_iteration_trace(x, alpha, iterations, field)
        end_time = time.time()
        
        trace_time = end_time - start_time
        
        results['trials'].append({
            'trial': i + 1,
            'input': x,
            'trace_length': len(trace),
            'time': trace_time
        })
        
        results['average_time'] += trace_time
        results['min_time'] = min(results['min_time'], trace_time)
        results['max_time'] = max(results['max_time'], trace_time)
    
    results['average_time'] /= num_trials
    
    return results

def main():
    """Run AIIP benchmarks."""
    parser = argparse.ArgumentParser(description='Benchmark AIIP performance')
    parser.add_argument('-c', '--config', required=True, help='Configuration file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-t', '--type', choices=['iteration', 'trace'], default='iteration', 
                       help='Benchmark type')
    parser.add_argument('-n', '--trials', type=int, default=10, help='Number of trials')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Run benchmark
    if args.type == 'iteration':
        results = benchmark_aiip_iteration(
            config['field_size'],
            config['alpha'],
            config['iterations'],
            args.trials
        )
    else:
        results = benchmark_aiip_trace(
            config['field_size'],
            config['alpha'],
            config['iterations'],
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
        writer = csv.writer(f)
        writer.writerow(['field_size', 'alpha', 'iterations', 'trial', 'time'])
        
        for trial in results['trials']:
            writer.writerow([
                results['field_size'],
                results['alpha'],
                results['iterations'],
                trial['trial'],
                trial['time']
            ])
    
    print(f"Benchmark completed. Results saved to {args.output} and {csv_path}")
    print(f"Average time: {results['average_time']:.6f} seconds")
    print(f"Time range: {results['min_time']:.6f} - {results['max_time']:.6f} seconds")

if __name__ == "__main__":
    main()