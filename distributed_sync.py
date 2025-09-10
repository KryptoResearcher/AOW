#!/usr/bin/env python3
"""
Example of distributed synchronization using AOW.
"""

import time
import random
from src.core.fields import FiniteField
from src.core.aiip import iterate_polynomial
from src.proofs.stark import generate_stark_proof, verify_stark_proof, STARKParameters
from src.utils import calculate_security_parameters

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

def main():
    """Demonstrate distributed synchronization with AOW."""
    print("=== AOW Distributed Synchronization Example ===\n")
    
    # Get recommended parameters
    params = calculate_security_parameters(128)
    field = FiniteField(params['field_size'])
    
    # Use smaller iterations for simulation
    iterations = 50
    
    # Create STARK parameters
    stark_params = STARKParameters(
        blowup_factor=4,
        security_param=128,
        fri_folding_factor=2
    )
    
    # Create distributed nodes
    nodes = [
        DistributedNode(1, field, params['alpha'], stark_params),
        DistributedNode(2, field, params['alpha'], stark_params),
        DistributedNode(3, field, params['alpha'], stark_params),
        DistributedNode(4, field, params['alpha'], stark_params)
    ]
    
    print(f"Created {len(nodes)} distributed nodes")
    print(f"Using {iterations} iterations per round")
    
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
    
    # Demonstrate Byzantine resistance
    print("\n=== Testing Byzantine Resistance ===")
    
    # Create a malicious node that tries to cheat
    malicious_node = DistributedNode(99, field, params['alpha'], stark_params)
    
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

if __name__ == "__main__":
    main()