"""
Unit tests for finite field implementation.
"""

import pytest
from src.core.fields import FiniteField

class TestFiniteField:
    """Test cases for FiniteField class."""
    
    @pytest.fixture
    def field(self):
        """Create a finite field for testing."""
        return FiniteField(1000003)  # Prime field
    
    def test_initialization(self, field):
        """Test field initialization."""
        assert field.modulus == 1000003
        assert field.size == 1000003
    
    def test_addition(self, field):
        """Test field addition."""
        assert field.add(5, 10) == 15
        assert field.add(1000000, 10) == 7  # Wraps around modulus
    
    def test_subtraction(self, field):
        """Test field subtraction."""
        assert field.sub(10, 5) == 5
        assert field.sub(5, 10) == 1000003 - 5  # Negative result wraps
    
    def test_multiplication(self, field):
        """Test field multiplication."""
        assert field.mul(5, 10) == 50
        assert field.mul(1000, 1000) == (1000 * 1000) % 1000003
    
    def test_squaring(self, field):
        """Test field squaring."""
        assert field.sqr(5) == 25
        assert field.sqr(1000) == (1000 * 1000) % 1000003
    
    def test_inversion(self, field):
        """Test multiplicative inversion."""
        # Test inversion of 5
        inv = field.inv(5)
        assert field.mul(5, inv) == 1
        
        # Test that zero cannot be inverted
        with pytest.raises(ValueError):
            field.inv(0)
    
    def test_random_element(self, field):
        """Test random element generation."""
        element = field.random_element()
        assert 0 <= element < field.modulus
    
    def test_quadratic_residue(self, field):
        """Test quadratic residue detection."""
        # 4 is a quadratic residue (2² = 4)
        assert field.is_quadratic_residue(4)
        
        # Generate a non-residue
        non_residue = None
        for i in range(1, 100):
            if not field.is_quadratic_residue(i):
                non_residue = i
                break
        
        assert non_residue is not None
        assert not field.is_quadratic_residue(non_residue)
    
    def test_square_root(self, field):
        """Test square root calculation."""
        # Test square root of a quadratic residue
        root = field.sqrt(4)
        assert root is not None
        assert field.sqr(root) == 4
        
        # Test square root of a non-residue
        non_residue = None
        for i in range(1, 100):
            if not field.is_quadratic_residue(i):
                non_residue = i
                break
        
        assert non_residue is not None
        assert field.sqrt(non_residue) is None