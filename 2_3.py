def main():
    def check(string):
        dicts = {'(': ')', '{': '}', '[': ']'}
        open = []
        for i in string:
            if i in dicts:
                open.append(i)
            else:
                if not open or dicts[open.pop()] != i:
                    return False
        if open:
            return False
        else:
            return True
    return print(check(str(input())))
if __name__ == '__main__':
    main()
# Press the green button in the gutter to run the script.
