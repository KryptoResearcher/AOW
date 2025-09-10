# Install benchmark dependencies
pip install -r benchmarks/requirements.txt

# Run AIIP iteration benchmark
python benchmarks/scripts/benchmark_aiip.py \
  -c benchmarks/configurations/small_params.json \
  -o benchmarks/results/aiip_small.json \
  -t iteration

# Run temporal binding benchmark
python benchmarks/scripts/benchmark_temporal.py \
  -c benchmarks/configurations/small_params.json \
  -o benchmarks/results/temporal_small.json \
  -t verification

# Run STARK proof benchmark
python benchmarks/scripts/benchmark_stark.py \
  -c benchmarks/configurations/small_params.json \
  -o benchmarks/results/stark_small.json

# Run event chain benchmark
python benchmarks/scripts/benchmark_event_chain.py \
  -c benchmarks/configurations/small_params.json \
  -o benchmarks/results/event_chain_small.json

# Generate performance plots
python benchmarks/analysis/plot_performance.py \
  -i benchmarks/results/aiip_small.json \
  -o benchmarks/results/plots/aiip_performance.png

# Generate comparison plots
python benchmarks/analysis/plot_performance.py \
  -i benchmarks/results/aiip_small.json benchmarks/results/aiip_standard.json \
  -o benchmarks/results/plots/aiip_comparison.png \
  -c

# Generate comprehensive report
python benchmarks/analysis/generate_report.py \
  -c benchmarks/configurations/small_params.json \
  -i benchmarks/results/aiip_small.json benchmarks/results/temporal_small.json \
  -o benchmarks/results/reports/small_benchmark_report.json