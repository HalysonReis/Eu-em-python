n = input('um numero de 100 a 9999. >>> ')

while int(n) <= 100 or int(n) >= 9999:
    n = input('um numero de 100 a 9999. >>> ')

c = 0

while c != len(n):
    print(n[c])
    c += 1