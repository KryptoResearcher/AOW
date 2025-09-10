#!/usr/bin/env python3
"""
Generate a comprehensive report from benchmark results.
"""

import json
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime

def generate_report(config_file, result_files, output_file):
    """Generate a comprehensive benchmark report."""
    # Load configuration
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    # Load results
    results = []
    for result_file in result_files:
        with open(result_file, 'r') as f:
            results.append(json.load(f))
    
    # Create report
    report = {
        'generated_at': datetime.now().isoformat(),
        'configuration': config,
        'results': results,
        'summary': {}
    }
    
    # Calculate summary statistics
    for i, result in enumerate(results):
        benchmark_type = Path(result_files[i]).stem
        report['summary'][benchmark_type] = {
            'average_time': result.get('average_time', 0),
            'min_time': result.get('min_time', 0),
            'max_time': result.get('max_time', 0),
            'trials': len(result.get('trials', []))
        }
    
    # Save report
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Also generate a markdown report
    md_path = output_path.with_suffix('.md')
    with open(md_path, 'w') as f:
        f.write(f"# AOW Benchmark Report\n\n")
        f.write(f"Generated: {report['generated_at']}\n\n")
        
        f.write(f"## Configuration\n\n")
        f.write(f"- Field Size: {config['field_size']}\n")
        f.write(f"- Alpha: {config['alpha']}\n")
        f.write(f"- Iterations: {config.get('iterations', 'N/A')}\n")
        f.write(f"- Max Iterations: {config.get('max_iterations', 'N/A')}\n")
        f.write(f"- Num Events: {config.get('num_events', 'N/A')}\n")
        f.write(f"- Security Level: {config.get('security_level', 'N/A')}\n\n")
        
        f.write(f"## Results Summary\n\n")
        f.write("| Benchmark Type | Average Time (s) | Min Time (s) | Max Time (s) | Trials |\n")
        f.write("|---------------|------------------|--------------|--------------|--------|\n")
        
        for benchmark_type, summary in report['summary'].items():
            f.write(f"| {benchmark_type} | {summary['average_time']:.6f} | {summary['min_time']:.6f} | {summary['max_time']:.6f} | {summary['trials']} |\n")
        
        f.write("\n")
        
        f.write(f"## Detailed Results\n\n")
        
        for i, result in enumerate(results):
            benchmark_type = Path(result_files[i]).stem
            f.write(f"### {benchmark_type}\n\n")
            
            if 'trials' in result:
                f.write("| Trial | Time (s) |\n")
                f.write("|-------|----------|\n")
                
                for trial in result['trials']:
                    f.write(f"| {trial['trial']} | {trial['time']:.6f} |\n")
            
            f.write("\n")
    
    print(f"Report generated. JSON saved to {output_file}, Markdown saved to {md_path}")

def main():
    """Generate benchmark report."""
    parser = argparse.ArgumentParser(description='Generate benchmark report')
    parser.add_argument('-c', '--config', required=True, help='Configuration file')
    parser.add_argument('-i', '--input', required=True, nargs='+', help='Input result files')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    
    args = parser.parse_args()
    
    generate_report(args.config, args.input, args.output)

if __name__ == "__main__":
    main()