t1 = 0
t2 = 1
t3 = 0
c = 1
while c <= 10:
    print(f"{t3}.", end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1

print( " Fim ")