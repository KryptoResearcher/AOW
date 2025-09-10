#!/usr/bin/env python3
"""
Plot performance data from benchmark results.
"""

import json
import argparse
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def plot_performance_data(input_file, output_file, metric='time'):
    """Plot performance data from benchmark results."""
    # Load data
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Extract trial data
    trials = data['trials']
    trial_numbers = [trial['trial'] for trial in trials]
    metric_values = [trial[metric] for trial in trials]
    
    # Plot data
    ax.plot(trial_numbers, metric_values, 'o-', label=f'{metric} per trial')
    ax.axhline(y=data[f'average_{metric}'], color='r', linestyle='--', 
               label=f'Average {metric}: {data[f"average_{metric}"]:.6f}s')
    
    # Customize plot
    ax.set_xlabel('Trial Number')
    ax.set_ylabel(f'{metric.capitalize()} (seconds)')
    ax.set_title(f'{metric.capitalize()} Performance: {data["field_size"]} field, {data["iterations"]} iterations')
    ax.legend()
    ax.grid(True)
    
    # Save plot
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved to {output_file}")

def plot_comparison(input_files, output_file, metric='time'):
    """Plot comparison of multiple benchmark results."""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for input_file in input_files:
        # Load data
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Extract trial data
        trials = data['trials']
        trial_numbers = [trial['trial'] for trial in trials]
        metric_values = [trial[metric] for trial in trials]
        
        # Plot data
        label = f"{data['field_size']} field, {data['iterations']} iterations"
        ax.plot(trial_numbers, metric_values, 'o-', label=label)
        ax.axhline(y=data[f'average_{metric}'], color='r', linestyle='--', alpha=0.5)
    
    # Customize plot
    ax.set_xlabel('Trial Number')
    ax.set_ylabel(f'{metric.capitalize()} (seconds)')
    ax.set_title(f'{metric.capitalize()} Performance Comparison')
    ax.legend()
    ax.grid(True)
    
    # Save plot
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Comparison plot saved to {output_file}")

def main():
    """Plot benchmark results."""
    parser = argparse.ArgumentParser(description='Plot benchmark results')
    parser.add_argument('-i', '--input', required=True, nargs='+', help='Input file(s)')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-m', '--metric', default='time', help='Metric to plot')
    parser.add_argument('-c', '--comparison', action='store_true', help='Create comparison plot')
    
    args = parser.parse_args()
    
    if args.comparison:
        plot_comparison(args.input, args.output, args.metric)
    else:
        if len(args.input) > 1:
            print("Warning: Multiple input files specified but no --comparison flag. Using first file only.")
        plot_performance_data(args.input[0], args.output, args.metric)

if __name__ == "__main__":
    main()