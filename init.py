"""
STARK proof integration for AOW.
"""

from .stark import generate_stark_proof, verify_stark_proof, STARKParameters

__all__ = ['generate_stark_proof', 'verify_stark_proof', 'STARKParameters']