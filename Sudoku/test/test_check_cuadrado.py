import pytest
from src.checkcuadrado import checkcuadrado
import casosTest.casosTestSudoku as casosTest

@pytest.mark.es_cuadrado
@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correcto, True),
                            (casosTest.num_repetido_fila_columna, True),
                            (casosTest.num_repetido_columna, True),
                            (casosTest.num_no_presente, True),
                            (casosTest.num_fuera_del_rango, True),
                            (casosTest.caracteres, True),
                            (casosTest.numeros_reales, True),
                            (casosTest.irregular_fila, False),
                            (casosTest.irregular_columna, False)])
def test_check_cuadrado(sudoku, sano):
    assert checkcuadrado(sudoku) == sano