from itertools import product
def get_pins(count: int) -> int:
    banks = []
    cashs = []
    it = []
    max_cash = 0

    for i in range(count):
        name = input()
        cash = int(input())
        one = [name, cash]
        banks.append(one)
        cashs.append(cash)

    if cashs[0] > cashs[1]:#если сумма денег в первом банке больше, то пусть сумма второго банка равна первому
        it.append(banks[0])
        cashs[1] = cashs[0]

    for i in range(2, len(cashs)):
        if cashs[i] + cashs[i-2] > cashs[i-1]:#если сумма денег в третьем банке и в первом больше, чем во втором, то количество денег третьего банка равна сумме третьего и первого 
            cashs[i] = cashs[i]+cashs[i-2]
            it.append(banks[i])
        else:
            cashs[i] = cashs[i-1]#иначе пусть количевство денег в третьем банке равно количеству денег во втором
    print(max(cashs))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins(int(input()))
