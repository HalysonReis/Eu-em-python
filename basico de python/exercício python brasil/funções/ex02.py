def numero(n):
    for i in range(n+1):
        for numero in range(i):
            print(numero + 1, end=' ')
        print('\n')

            
numero(20)