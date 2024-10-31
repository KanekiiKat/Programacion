def checkcolumnas(sudoku):
    num_columnmas = len(sudoku[0])
    for num_filas in sudoku:
        if num_columnmas != len(num_filas):
            return False
        else:
            