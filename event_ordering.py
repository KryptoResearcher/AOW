#!/usr/bin/env python3
"""
Example of Byzantine-resistant event ordering using AOW.
"""

import json
import time
from src.core.fields import FiniteField
from src.temporal.chain import create_event_chain
from src.utils import calculate_security_parameters

def main():
    """Demonstrate event ordering with AOW."""
    print("=== AOW Event Ordering Example ===\n")
    
    # Get recommended parameters
    params = calculate_security_parameters(128)
    field = FiniteField(params['field_size'])
    
    # Create sample events
    events = [
        b"Transaction: Alice -> Bob, 10 BTC",
        b"Transaction: Bob -> Charlie, 5 BTC",
        b"Transaction: Charlie -> Dave, 3 BTC",
        b"Transaction: Dave -> Eve, 2 BTC",
        b"Transaction: Eve -> Frank, 1 BTC"
    ]
    
    print("Creating event chain with the following events:")
    for i, event in enumerate(events):
        print(f"  {i+1}. {event.decode()}")
    
    # Create the event chain
    start_time = time.time()
    chain = create_event_chain(events, field, params['alpha'])
    end_time = time.time()
    
    print(f"\nEvent chain created in {end_time - start_time:.4f} seconds")
    print(f"Chain length: {len(chain.chain)} events")
    
    # Verify chain integrity
    is_valid = chain.verify_chain()
    print(f"Chain integrity verified: {is_valid}")
    
    # Show chain structure
    print("\nChain structure:")
    for i, event in enumerate(chain.chain):
        event_hash = int.from_bytes(event.previous_hash, 'big') if event.previous_hash else 0
        print(f"  Event {i+1}: Previous hash = {event_hash % 1000}... (truncated)")
    
    # Demonstrate tamper resistance
    print("\n=== Testing Tamper Resistance ===")
    
    # Save original chain state
    original_data = chain.chain[2].data
    
    # Attempt to tamper with an event
    chain.chain[2].data = b"Transaction: MALICIOUS -> Attack, 1000 BTC"
    
    # Verify chain integrity again
    is_valid_after_tamper = chain.verify_chain()
    print(f"Chain integrity after tampering: {is_valid_after_tamper}")
    
    # Restore original data
    chain.chain[2].data = original_data
    is_valid_after_restore = chain.verify_chain()
    print(f"Chain integrity after restoration: {is_valid_after_restore}")

if __name__ == "__main__":
    main()