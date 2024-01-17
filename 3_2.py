import numpy
def get_pins() -> list:
    matrix = []
    matrix_v = []
    s = int(input('Столбцов: '))
    c = int(input('Стррок: '))
    for i in range(c):
        for j in range(s):
            matrix_v.append(int(input()))
        matrix.append(matrix_v)
        matrix_v = []
    print(matrix)
    if len(matrix[0]) > len(matrix):#если столбцов больше, чем строк, то дополняется нулями
        for i in range(len(matrix[0])-len(matrix)):
            matrix.append([0 for _ in range(len(matrix[0]))])
    if len(matrix) > len(matrix[0]):#если строк больше, чем столбцов, то дополняется нулями
        for i in range(len(matrix)):
            for j in range(len(matrix)-len(matrix[-1])):
                matrix[i].append(0)
    matrix_nn = numpy.array(matrix)
    matrix_r = numpy.rot90(matrix_nn)#поворот матрицы на 90 градусов
    return print(matrix_r)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins()
