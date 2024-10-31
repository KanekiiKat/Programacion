def checkcolumnas(sudoku):
    assert isinstance(
        sudoku, list), "El input tiene que ser un sudoku"
    
    num_filas = len(sudoku)

    fila_actual = 0

    for filas in sudoku:
        for numero in filas:
            fila_siguiente = fila_actual + 1
            while fila_siguiente < num_filas:
                try:
                    pos_fila_siguiente = sudoku[fila_siguiente].index(numero)

                except ValueError:

                    return False

                else:
                    if pos_fila_siguiente == filas.index(numero):
                        return False
                    else:
                        fila_siguiente += 1
        fila_actual += 1

    return True

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):

        if attr.startswith('__'):

            pass

        else:
            print(attr, " => ", checkcolumnas(casosTest.__dict__[attr]))
