"""
Utility functions for AOW.
"""

import hashlib
from typing import Union
from .core.fields import FiniteField

def hash_to_field(data: Union[bytes, str], field: FiniteField) -> int:
    """
    Hash data to a field element.
    
    Args:
        data: Data to hash
        field: Finite field instance
        
    Returns:
        Field element representation of hash
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Use SHA256 for cryptographic hashing
    hash_bytes = hashlib.sha256(data).digest()
    
    # Convert to integer and reduce modulo field size
    hash_int = int.from_bytes(hash_bytes, 'big')
    return hash_int % field.size

def generate_quadratic_non_residue(field: FiniteField) -> int:
    """
    Generate a quadratic non-residue in the field.
    
    Args:
        field: Finite field instance
        
    Returns:
        A quadratic non-residue element
    """
    while True:
        element = field.random_element()
        if not field.is_quadratic_residue(element):
            return element

def calculate_security_parameters(security_level: int) -> dict:
    """
    Calculate recommended parameters for a given security level.
    
    Args:
        security_level: Desired security level in bits
        
    Returns:
        Dictionary of recommended parameters
    """
    if security_level == 128:
        return {
            'field_size': 2**256,
            'max_iterations': 2**64,
            'alpha': 5  # Example value, should be a quadratic non-residue
        }
    elif security_level == 192:
        return {
            'field_size': 2**384,
            'max_iterations': 2**96,
            'alpha': 5  # Example value
        }
    elif security_level == 256:
        return {
            'field_size': 2**512,
            'max_iterations': 2**128,
            'alpha': 5  # Example value
        }
    else:
        raise ValueError(f"Unsupported security level: {security_level}")