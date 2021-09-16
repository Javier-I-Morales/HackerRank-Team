if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
    segundo = sorted(list(set([x[1] for x in lista])))[1]
    print('\n'.join(sorted([n for n, v in lista if v == segundo])))