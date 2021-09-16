if __name__ == '__main__':
    a = int(input())
    b = int(input())
    operators = ('+','-','*')
    for o in operators:
        print(eval(str(a)+o+str(b)))