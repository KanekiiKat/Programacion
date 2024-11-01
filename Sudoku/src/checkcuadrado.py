def checkcuadrado(sudoku):
    assert isinstance(sudoku, list), "Debe ser un sudoku en forma de lista"
    sudokubueno = True
    num_filas = len(sudoku)

    for fila in sudoku:
        if len(fila) != num_filas:
            sudokubueno = False
            break

    assert isinstance(sudokubueno, bool), "la interfaz exige devolver un valor lógico"
    return sudokubueno

if __name__ == '__main__':

    print("Esto es el main de checkCuadrado")

    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", checkcuadrado(casosTest.__dict__[attr]))
