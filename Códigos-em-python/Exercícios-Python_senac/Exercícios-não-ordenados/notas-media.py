n = int(input('quantas avaliações? '))
c = n
nota = 0

while c != 0:
    nota += int(input('qual a nota: '))
    c -= 1

print(f'a media é {nota / n}')