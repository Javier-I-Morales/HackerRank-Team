if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range (N):
        comando = input().split()
        if not "print" in comando:
            funcion = comando[0]
            parametros = comando[1:]
            exec('lista.'+funcion+'('+",".join(parametros)+')')
        else:
            print(lista)
