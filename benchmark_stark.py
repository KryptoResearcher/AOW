#!/usr/bin/env python3
"""
Benchmark script for STARK proof generation and verification performance.
"""

import time
import json
import argparse
import csv
from pathlib import Path
from src.core.fields import FiniteField
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters

def benchmark_stark_proofs(field_size, alpha, iterations, num_trials=5):
    """Benchmark STARK proof generation and verification performance."""
    field = FiniteField(field_size)
    stark_params = STARKParameters(
        blowup_factor=4,
        security_param=128,
        fri_folding_factor=2
    )
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'iterations': iterations,
        'trials': [],
        'average_generation_time': 0,
        'average_verification_time': 0,
        'min_generation_time': float('inf'),
        'max_generation_time': 0,
        'min_verification_time': float('inf'),
        'max_verification_time': 0
    }
    
    for i in range(num_trials):
        # Generate random input
        x = field.random_element()
        
        # Time proof generation
        gen_start_time = time.time()
        proof, public_inputs = generate_stark_proof(x, alpha, iterations, field, stark_params)
        gen_end_time = time.time()
        
        generation_time = gen_end_time - gen_start_time
        
        # Time proof verification
        ver_start_time = time.time()
        is_valid = verify_stark_proof(proof, public_inputs, field, stark_params)
        ver_end_time = time.time()
        
        verification_time = ver_end_time - ver_start_time
        
        results['trials'].append({
            'trial': i + 1,
            'input': x,
            'generation_time': generation_time,
            'verification_time': verification_time,
            'valid': is_valid
        })
        
        results['average_generation_time'] += generation_time
        results['average_verification_time'] += verification_time
        results['min_generation_time'] = min(results['min_generation_time'], generation_time)
        results['max_generation_time'] = max(results['max_generation_time'], generation_time)
        results['min_verification_time'] = min(results['min_verification_time'], verification_time)
        results['max_verification_time'] = max(results['max_verification_time'], verification_time)
    
    results['average_generation_time'] /= num_trials
    results['average_verification_time'] /= num_trials
    
    return results

def main():
    """Run STARK benchmarks."""
    parser = argparse.ArgumentParser(description='Benchmark STARK proof performance')
    parser.add_argument('-c', '--config', required=True, help='Configuration file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-n', '--trials', type=int, default=5, help='Number of trials')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Run benchmark
    results = benchmark_stark_proofs(
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
        writer.writerow(['field_size', 'alpha', 'iterations', 'trial', 'generation_time', 'verification_time'])
        
        for trial in results['trials']:
            writer.writerow([
                results['field_size'],
                results['alpha'],
                results['iterations'],
                trial['trial'],
                trial['generation_time'],
                trial['verification_time']
            ])
    
    print(f"Benchmark completed. Results saved to {args.output} and {csv_path}")
    print(f"Average generation time: {results['average_generation_time']:.6f} seconds")
    print(f"Average verification time: {results['average_verification_time']:.6f} seconds")

if __name__ == "__main__":
    main()