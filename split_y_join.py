def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

'''
si tengo el string siguiente: hola como estas

y hago "-".join(string)

me devuelve h-o-l-a- -c-o-m-o- -e-s-t-a-s

si hago string.split(" ")

me devuelve "hola" "como" "estas"
'''