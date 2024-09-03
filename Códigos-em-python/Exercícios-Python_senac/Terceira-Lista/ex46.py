altura_chico = 170
altura_ze = 120

print('altura inicial chico: ', altura_chico)
print('altura inicial zé: ', altura_ze)

c = 0
while altura_chico > altura_ze:
    altura_chico += 2
    altura_ze += 3
    print('-='*10)
    print('CHICO: ', altura_chico)
    print('ZÉ: ', altura_ze)
    print('-='*10)

    c += 1

print(f'foram necessarios {c} anos para zé ultrapassar chico')
