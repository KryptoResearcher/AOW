#!/usr/bin/env python3
"""
Benchmark script for event chain operations performance.
"""

import time
import json
import argparse
import csv
from pathlib import Path
from src.core.fields import FiniteField
from src.temporal.chain import create_event_chain

def benchmark_event_chain(field_size, alpha, num_events, num_trials=5):
    """Benchmark event chain creation and verification performance."""
    field = FiniteField(field_size)
    
    results = {
        'field_size': field_size,
        'alpha': alpha,
        'num_events': num_events,
        'trials': [],
        'average_creation_time': 0,
        'average_verification_time': 0,
        'min_creation_time': float('inf'),
        'max_creation_time': 0,
        'min_verification_time': float('inf'),
        'max_verification_time': 0
    }
    
    # Create sample events
    events = [f"Event {i}".encode() for i in range(num_events)]
    
    for i in range(num_trials):
        # Time chain creation
        creation_start_time = time.time()
        chain = create_event_chain(events, field, alpha)
        creation_end_time = time.time()
        
        creation_time = creation_end_time - creation_start_time
        
        # Time chain verification
        verification_start_time = time.time()
        is_valid = chain.verify_chain()
        verification_end_time = time.time()
        
        verification_time = verification_end_time - verification_start_time
        
        results['trials'].append({
            'trial': i + 1,
            'creation_time': creation_time,
            'verification_time': verification_time,
            'valid': is_valid
        })
        
        results['average_creation_time'] += creation_time
        results['average_verification_time'] += verification_time
        results['min_creation_time'] = min(results['min_creation_time'], creation_time)
        results['max_creation_time'] = max(results['max_creation_time'], creation_time)
        results['min_verification_time'] = min(results['min_verification_time'], verification_time)
        results['max_verification_time'] = max(results['max_verification_time'], verification_time)
    
    results['average_creation_time'] /= num_trials
    results['average_verification_time'] /= num_trials
    
    return results

def main():
    """Run event chain benchmarks."""
    parser = argparse.ArgumentParser(description='Benchmark event chain performance')
    parser.add_argument('-c', '--config', required=True, help='Configuration file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-n', '--trials', type=int, default=5, help='Number of trials')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Run benchmark
    results = benchmark_event_chain(
        config['field_size'],
        config['alpha'],
        config['num_events'],
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
        writer.writerow(['field_size', 'alpha', 'num_events', 'trial', 'creation_time', 'verification_time'])
        
        for trial in results['trials']:
            writer.writerow([
                results['field_size'],
                results['alpha'],
                results['num_events'],
                trial['trial'],
                trial['creation_time'],
                trial['verification_time']
            ])
    
    print(f"Benchmark completed. Results saved to {args.output} and {csv_path}")
    print(f"Average creation time: {results['average_creation_time']:.6f} seconds")
    print(f"Average verification time: {results['average_verification_time']:.6f} seconds")

if __name__ == "__main__":
    main()