n =int( input("digite Quantos quantos você deseja: "))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print(f"{t3}.", end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print( " Fim ")