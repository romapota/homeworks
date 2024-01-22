s:list
circle: int
figure: int
square: int
flag: bool
def check(s: str) -> bool:
    circle = figure = square = 0
    flag = True
    for i in range(len(s)):#подсчет
        if s[i] == '(':
            circle += 1
        if s[i] == ')':
            circle -= 1
        if s[i] == '{':
            figure += 1
        if s[i] == '}':
            figure -= 1
        if s[i] == '[':
            square += 1
        if s[i] == ']':
            square -= 1
        if (circle < 0) or (figure < 0) or (square < 0):#если скобки не закрываются попарно, то останавливаем цикл
            flag = False
            break
    if (circle != 0) or (figure != 0) or (square != 0) or (nutr(s) == False):#если открывающихся и закрывающихся скобок не одинаковое количество, то flag = false
        flag = False
    return flag

def nutr(s: str) -> bool:
    flag = True
    for i in range(len(s) - 1):#если скобка не закрывается в следующем символе flag = false
        if ((s[i] == '{') and ((s[i + 1] == ']') or (s[i + 1] == ')'))) or ((s[i] == '[') and ((s[i + 1] == '}') or (s[i + 1] == ')'))) or ((s[i] == '(') and ((s[i + 1] == ']') or (s[i + 1] == '}'))):
            flag = False
    return flag


def main():
    s = str(input('Введите строку '))
    if check(s):#если строка правильная, выводит True
        return print(True)
    else:
        s_s = s_s_s = ''
        circle = figure =square = 0
        for n in range(len(s)):#перебираем скобки в строке и подсчитываем количество скобок
            s_s = ''
            for i in range(n, len(s)):
                if s[i] == '(':
                    circle += 1
                elif s[i] == ')':
                    circle -= 1
                elif s[i] == '{':
                    figure += 1
                elif s[i] == '}':
                    figure -= 1
                elif s[i] == '[':
                    square += 1
                elif s[i] == ']':
                    square -= 1
                s_s += s[i]
                if check(s_s):
                    if len(s_s) > len(s_s_s):#если текущая строка больше самой большой, то меняем значение
                        s_s_s = s_s
        if s_s_s == '':
            return print(False)
        else:#если строка не пустая, то выводим ее
            return print(s_s_s)

if __name__ == "__main__":
    main()