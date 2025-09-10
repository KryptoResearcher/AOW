
# Tutorial: Distributed Synchronization with AOW

## Introduction

This tutorial will guide you through using AOW for distributed synchronization in multi-party systems.

## Prerequisites

- Completion of [Basic Usage Tutorial](basic_usage.md)
- Completion of [STARK Proofs Tutorial](stark_proofs.md)
- Understanding of distributed systems concepts

## Step 1: Import Required Modules

```python
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters
import time
import random

Step 2: Define Distributed Node Class
python

class DistributedNode:
    """Simulation of a distributed node using AOW for synchronization."""
    
    def __init__(self, node_id, field, alpha, stark_params):
        self.node_id = node_id
        self.field = field
        self.alpha = alpha
        self.stark_params = stark_params
        self.local_state = field.random_element()
        self.round = 0
        self.proofs = {}
    
    def complete_round(self, iterations):
        """Complete a computation round and generate proof."""
        self.round += 1
        
        # Perform the computation
        start_time = time.time()
        new_state = iterate_polynomial(self.local_state, self.alpha, iterations, self.field)
        compute_time = time.time() - start_time
        
        # Generate proof
        proof_start = time.time()
        proof, public_inputs = generate_stark_proof(
            self.local_state, self.alpha, iterations, self.field, self.stark_params
        )
        proof_time = time.time() - proof_start
        
        # Update state
        self.local_state = new_state
        
        # Store proof
        self.proofs[self.round] = {
            'proof': proof,
            'public_inputs': public_inputs,
            'compute_time': compute_time,
            'proof_time': proof_time
        }
        
        return {
            'round': self.round,
            'state': new_state,
            'proof': proof,
            'public_inputs': public_inputs,
            'compute_time': compute_time,
            'proof_time': proof_time
        }
    
    def verify_round(self, other_node_id, round_data):
        """Verify another node's round computation."""
        verify_start = time.time()
        is_valid = verify_stark_proof(
            round_data['proof'],
            round_data['public_inputs'],
            self.field,
            self.stark_params
        )
        verify_time = time.time() - verify_start
        
        return {
            'valid': is_valid,
            'verify_time': verify_time,
            'verified_round': round_data['round'],
            'verified_node': other_node_id
        }

Step 3: Initialize Parameters and Nodes
python

# Initialize parameters
params = calculate_security_parameters(128)
field = FiniteField(params['field_size'])
alpha = params['alpha']
iterations = 100  # Use smaller iterations for simulation

stark_params = STARKParameters(
    blowup_factor=4,
    security_param=128,
    fri_folding_factor=2
)

# Create distributed nodes
nodes = [
    DistributedNode(1, field, alpha, stark_params),
    DistributedNode(2, field, alpha, stark_params),
    DistributedNode(3, field, alpha, stark_params),
    DistributedNode(4, field, alpha, stark_params)
]

print(f"Created {len(nodes)} distributed nodes")
print(f"Using {iterations} iterations per round")

Step 4: Simulate Computation Rounds
python

# Simulate several rounds of computation
num_rounds = 3
all_round_data = {}

for round_num in range(1, num_rounds + 1):
    print(f"\n--- Round {round_num} ---")
    
    round_data = {}
    
    # Each node completes the round
    for node in nodes:
        result = node.complete_round(iterations)
        round_data[node.node_id] = result
        
        print(f"Node {node.node_id}: "
              f"state = {result['state'] % 1000}... (truncated), "
              f"compute = {result['compute_time']:.4f}s, "
              f"proof = {result['proof_time']:.4f}s")
    
    # Nodes verify each other's proofs
    verification_results = []
    for verifier in nodes:
        for target_id, target_data in round_data.items():
            if verifier.node_id != target_id:
                result = verifier.verify_round(target_id, target_data)
                verification_results.append(result)
    
    # Count successful verifications
    successful_verifications = sum(1 for r in verification_results if r['valid'])
    total_verifications = len(verification_results)
    
    print(f"Verifications: {successful_verifications}/{total_verifications} successful")
    
    # Store round data
    all_round_data[round_num] = {
        'computations': round_data,
        'verifications': verification_results
    }

Step 5: Analyze Performance
python

# Analyze performance data
print("\n--- Performance Analysis ---")

total_compute_time = 0
total_proof_time = 0
total_verify_time = 0

for round_num, round_data in all_round_data.items():
    for node_id, computation in round_data['computations'].items():
        total_compute_time += computation['compute_time']
        total_proof_time += computation['proof_time']
    
    for verification in round_data['verifications']:
        total_verify_time += verification['verify_time']

print(f"Total compute time: {total_compute_time:.4f}s")
print(f"Total proof generation time: {total_proof_time:.4f}s")
print(f"Total verification time: {total_verify_time:.4f}s")
print(f"Total time: {total_compute_time + total_proof_time + total_verify_time:.4f}s")

# Calculate averages
num_computations = sum(len(round_data['computations']) for round_data in all_round_data.values())
num_verifications = sum(len(round_data['verifications']) for round_data in all_round_data.values())

avg_compute_time = total_compute_time / num_computations
avg_proof_time = total_proof_time / num_computations
avg_verify_time = total_verify_time / num_verifications

print(f"\nAverages:")
print(f"  Compute time: {avg_compute_time:.4f}s")
print(f"  Proof generation time: {avg_proof_time:.4f}s")
print(f"  Verification time: {avg_verify_time:.4f}s")

Step 6: Test Byzantine Resistance
python

# Test Byzantine resistance
print("\n--- Testing Byzantine Resistance ---")

# Create a malicious node
malicious_node = DistributedNode(99, field, alpha, stark_params)

# The malicious node tries to claim it did more work than it actually did
malicious_result = malicious_node.complete_round(iterations // 2)  # Only half the work
malicious_result['public_inputs']['iterations'] = iterations  # But claims full work

# Other nodes verify the malicious claim
verification_results = []
for node in nodes:
    result = node.verify_round(malicious_node.node_id, malicious_result)
    verification_results.append(result)

# Count successful verifications
successful_verifications = sum(1 for r in verification_results if r['valid'])

print(f"Malicious node verification: {successful_verifications}/{len(verification_results)} successful")
print("A properly implemented STARK would detect this fraud (simulated here)")

Step 7: Simulate Network Conditions
python

# Simulate network conditions
print("\n--- Simulating Network Conditions ---")

def simulate_network_delay():
    """Simulate network delay."""
    delay = random.uniform(0.1, 0.5)  # 100-500ms delay
    time.sleep(delay)
    return delay

# Simulate round with network delay
print("Simulating round with network delay...")

round_data = {}
network_delays = []

for node in nodes:
    # Node completes round
    result = node.complete_round(iterations)
    round_data[node.node_id] = result
    
    # Simulate network delay for broadcasting
    delay = simulate_network_delay()
    network_delays.append(delay)

print(f"Network delays: {[f'{d:.3f}s' for d in network_delays]}")
print(f"Average delay: {sum(network_delays)/len(network_delays):.3f}s")

Step 8: Complete Example
python

# tutorial_distributed_sync.py
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters
import time
import random

# Implementation of DistributedNode class and simulation code from above

if __name__ == "__main__":
    # Initialize parameters
    params = calculate_security_parameters(128)
    field = FiniteField(params['field_size'])
    alpha = params['alpha']
    iterations = 100
    
    stark_params = STARKParameters(
        blowup_factor=4,
        security_param=128,
        fri_folding_factor=2
    )
    
    # Create nodes and run simulation
    nodes = [
        DistributedNode(1, field, alpha, stark_params),
        DistributedNode(2, field, alpha, stark_params),
        DistributedNode(3, field, alpha, stark_params),
        DistributedNode(4, field, alpha, stark_params)
    ]
    
    # Run 3 rounds
    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")
        
        round_data = {}
        for node in nodes:
            result = node.complete_round(iterations)
            round_data[node.node_id] = result
            print(f"Node {node.node_id} completed round")
        
        print(f"Round {round_num} completed successfully")

Next Steps

Now that you've completed the distributed synchronization tutorial:

    Explore the advanced usage guide for optimization techniques

    Learn about real-world applications

    Read about performance optimization

    Check the API reference for detailed documentation

Real-World Applications

Distributed synchronization with AOW can be used for:

    Blockchain consensus: Byzantine-resistant agreement on state

    Distributed ledgers: Synchronized record-keeping across parties

    Multi-party computation: Coordinated computation with verification

    Game theory mechanisms: Provably fair distributed mechanisms

Further Reading

    Byzantine Fault Tolerance

    API Reference

    Advanced Usage Guide

text


This comprehensive documentation provides:

1. **Theory**: Mathematical foundations and security properties
2. **User Guide**: Installation, quickstart, and advanced usage
3. **API Reference**: Detailed documentation of all modules and classes
4. **Tutorials**: Step-by-step guides for common use cases

