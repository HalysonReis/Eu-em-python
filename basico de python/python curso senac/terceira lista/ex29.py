mmc = 1

for i in range(2, 21):
    mlc = mmc
    while mlc % i != 0:
        mlc += mmc
    mmc = mlc

print(f'o mmc é {mmc}')