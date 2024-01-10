def print_hi(name):
    negative_b = 0
    number = int(input())
    if number < 0:
        number *= -1
        negative_b = 1
    c = 0
    m = []
    p = 0
    p_p = 0
    for i in range(1, len(str(number))+1):
        m.append(((number%(10**i))-p)//10**(i-1))
        p += ((number%(10**i))-p)
    new_number = ''
    for i in m:
        new_number += str(i)
    new_number = int(new_number)
    if negative_b == 1:
        new_number *= -1
    if (int(new_number) >= -128) and (int(new_number) <= 127):
        return print(new_number)
    else:
        return print('not solution')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')