"""
Event chain implementation for Byzantine-resistant ordering.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..core.fields import FiniteField
from ..core.aiip import iterate_polynomial

@dataclass
class Event:
    """Representation of a temporal event."""
    data: bytes
    timestamp: int
    previous_hash: Optional[bytes] = None

class EventChain:
    """Temporal event chain using AOW for Byzantine resistance."""
    
    def __init__(self, field: FiniteField, alpha: int):
        """
        Initialize event chain.
        
        Args:
            field: Finite field instance
            alpha: Constant for polynomial f(x) = x² + α
        """
        self.field = field
        self.alpha = alpha
        self.chain = []
        self.genesis = self.field.random_element()
    
    def add_event(self, event_data: bytes, iterations: int = 1000) -> bytes:
        """
        Add an event to the chain.
        
        Args:
            event_data: Event data to add
            iterations: Number of AOW iterations
            
        Returns:
            Hash of the new event
        """
        # Hash the event data with previous hash
        if self.chain:
            prev_hash = self.chain[-1].hash
        else:
            prev_hash = self.genesis.to_bytes((self.genesis.bit_length() + 7) // 8, 'big')
        
        # Create hash input
        hash_input = event_data + prev_hash
        
        # Convert to field element (simplified)
        x = int.from_bytes(hash_input, 'big') % self.field.size
        
        # Compute AOW iteration
        y = iterate_polynomial(x, self.alpha, iterations, self.field)
        
        # Create event
        event_hash = y.to_bytes((y.bit_length() + 7) // 8, 'big')
        event = Event(data=event_data, timestamp=len(self.chain), previous_hash=prev_hash)
        self.chain.append(event)
        
        return event_hash
    
    def verify_chain(self) -> bool:
        """Verify the integrity of the entire event chain."""
        if not self.chain:
            return True
        
        # Check genesis matches
        if self.chain[0].previous_hash != self.genesis.to_bytes(
            (self.genesis.bit_length() + 7) // 8, 'big'
        ):
            return False
        
        # Verify each link in the chain
        for i in range(1, len(self.chain)):
            prev_event = self.chain[i-1]
            curr_event = self.chain[i]
            
            # Check previous hash matches
            if curr_event.previous_hash != prev_event.hash:
                return False
        
        return True

def create_event_chain(events: List[bytes], field: FiniteField, alpha: int) -> EventChain:
    """
    Create an event chain from a list of events.
    
    Args:
        events: List of event data
        field: Finite field instance
        alpha: Constant for polynomial
        
    Returns:
        Event chain instance
    """
    chain = EventChain(field, alpha)
    for event_data in events:
        chain.add_event(event_data)
    return chain