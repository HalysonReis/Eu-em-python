c = 0

total = 0

while c <= 10:
    nota = float(input('digite a nota: '))
    if nota > 10:
        break

    total += nota

    c += 1

media = total / c

print(f'foram digitadas {c}, e a media delas são {media}')