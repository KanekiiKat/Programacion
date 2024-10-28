from src.pruebilla import suma
import pytest

@pytest.mark.pruebilla
def test_prueba():
    assert suma(0) == 0 
    assert suma(1) == 0 
    assert suma(2) == 0 
