def print_hi(name) -> bool:
    # Use a breakpoint in the code line below to debug your script.
    number = int(input())
    c = 0
    m = []
    p = 0
    p_p = 0
    for i in range(1, len(str(number))+1):#отделение каждой единицы, десятка, сотни и тд
        m.append(((number%(10**i))-p)//10**(i-1))#вычитание из полученного отделения уже отделившийся части
        p += ((number%(10**i))-p)#сумма наденной части
    for i in m:
        new_number += str(i)#нахождение нового числа
    if int(new_number) == number:
        return print(True)
    else:
        return print(False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
