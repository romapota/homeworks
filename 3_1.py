import numpy
def cins(list_values):
    s = []
    for i in list_values:
        s.append(i)
    return s

def get_pins():
    matrix = []
    matrix_p = []
    matrix_v = []
    s = int(input('Количество строк: '))
    c = int(input('Количество столбцов: '))
    for i in range(s):
        for j in range(c):
            matrix_p.append(int(input()))
        matrix.append(matrix_p)
        matrix_p = []
    indexRight = 0
    indexLeft = 0
    indexTop = 0
    indexBottom = 0
    matrix_str = []
    indexBottom = len(matrix)-1
    indexRight = len(matrix[0])-1
    for j in range(len(matrix)//2):
        for i in matrix[indexTop][indexLeft:indexRight+1]:#top
            matrix_str.append(i)
        indexTop += 1
        for i in range(indexTop, indexBottom+1):#right
            matrix_str.append(matrix[i][indexRight])
        indexRight -= 1

        st = cins(matrix[indexBottom])
        for i in st[indexLeft+1:indexRight+1][::-1]:#bottom revers
            matrix_str.append(int(i))
        indexBottom -= 1

        for i in range(indexBottom+1, indexTop-1, -1):#left revers
            matrix_str.append(matrix[i][indexLeft])
        indexLeft += 1
        if len(matrix) % 2 != 0:
            for i in matrix[indexTop][indexLeft:indexRight+1]:#last top
                matrix_str.append(i)

    return print(matrix_str)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins()