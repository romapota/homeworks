def funcks(values: str) -> int:
    names = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'o': 0}#словарь со значением каждой буквы
    values += 'o'#добавяем в конце 'o', чтобы не было ошибок о выходе за пределы
    if len(values) >= 1 and len(values) <= 15:
        values_list = [i for i in values]
        values_arab = 0
        ch = 0
        for i in range(len(values_list)-1):
            if ch == 1:
                ch = 0
                continue
            #если 'I' стоит перед 'V' или 'X' или 'V' или 'X' стоит перед 'L' или 'C', или 'С' стоит перед 'D' или 'M', то вычитаем из значения второго символа первое
            if (values_list[-1] not in ['i', 'X', 'C']) and ((values_list[i] == 'I' and (values_list[i+1] in ['V', 'X'])) or (values_list[i] == 'X' and (values_list[i+1] in ['L', 'C'])) or (values_list[i] == 'C' and (values_list[i+1] in ['D', 'M']))):
                values_arab += names[values_list[i+1]]-names[values_list[i]]
                ch = 1
            else:#иначе просто суммируем
                values_arab += names[values_list[i]]
        return print(values_arab)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    funcks(input())
