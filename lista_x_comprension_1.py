if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista_permutaciones=[[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i <= x and j <= y and k <= z]
    lista_filtrada = [a for a in lista_permutaciones if a[0] + a[1] + a[2] != n]
    print (lista_filtrada)