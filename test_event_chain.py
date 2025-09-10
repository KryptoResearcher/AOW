"""
Integration tests for event chain implementation.
"""

import pytest
from src.core.fields import FiniteField
from src.temporal.chain import EventChain, create_event_chain

class TestEventChain:
    """Integration tests for event chain."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)
    
    @pytest.fixture
    def event_chain(self, field):
        """Create an event chain for testing."""
        return EventChain(field, alpha=5)
    
    def test_empty_chain(self, event_chain):
        """Test operations on empty chain."""
        assert len(event_chain.chain) == 0
        assert event_chain.verify_chain()
    
    def test_add_events(self, event_chain):
        """Test adding events to chain."""
        # Add first event
        hash1 = event_chain.add_event(b"Event 1")
        assert len(event_chain.chain) == 1
        assert event_chain.verify_chain()
        
        # Add second event
        hash2 = event_chain.add_event(b"Event 2")
        assert len(event_chain.chain) == 2
        assert event_chain.verify_chain()
        
        # Hashes should be different
        assert hash1 != hash2
    
    def test_chain_integrity(self, event_chain):
        """Test chain integrity verification."""
        # Add events
        event_chain.add_event(b"Event 1")
        event_chain.add_event(b"Event 2")
        event_chain.add_event(b"Event 3")
        
        # Chain should be valid
        assert event_chain.verify_chain()
        
        # Tamper with chain
        event_chain.chain[1].data = b"Tampered event"
        
        # Chain should be invalid
        assert not event_chain.verify_chain()
    
    def test_create_event_chain(self, field):
        """Test create_event_chain function."""
        events = [b"Event 1", b"Event 2", b"Event 3"]
        chain = create_event_chain(events, field, alpha=5)
        
        assert len(chain.chain) == 3
        assert chain.verify_chain()