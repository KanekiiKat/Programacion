import pytest
from src.checkcolumnas import checkcolumnas
import casosTest.casosTestSudoku as casosTest

@pytest.mark.columnas_validas
@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correcto, True),
                            (casosTest.numero_repetido_fila_columna, False),
                            (casosTest.numero_repetido_columna, False),
                            (casosTest.numero_no_presente, False),
                            pytest.param(casosTest.numero_fuera_del_rango,
                                         False,
                                         marks=pytest.mark.barricada)])

def test_check_columnas(sudoku, sano):
    assert checkcolumnas(sudoku) == sano