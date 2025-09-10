# Run all tests
pytest

# Run specific test categories
pytest tests/unit/
pytest tests/property/
pytest tests/integration/

# Run with verbose output
pytest -v

# Run with coverage reporting
pytest --cov=src