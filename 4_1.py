def main(count):
    numbers = [int(input()) for _ in range(count)]
    target = int(input('Цель: '))
    dict_info = {}
    for index_one in range(count):
        for index_two in range(count):
            for index_three in range(count):
                for index_four in range(count):
                    if index_one != index_two and index_one != index_three and index_one != index_four and index_two != index_three and index_two != index_four and index_three != index_four:
                        sum = numbers[index_one] + numbers[index_two] + numbers[index_three] + numbers[index_four]
                        if sum == target:
                            return print(numbers[index_one], numbers[index_two], numbers[index_three], numbers[index_four])
                        else:
                            delta = abs(target - sum)
                            dict_info[delta] = [numbers[index_one], numbers[index_two], numbers[index_three], numbers[index_four]]
    print(dict_info[min(dict_info)])

if __name__ == '__main__':
    main(int(input('Количество чисел: ')))
