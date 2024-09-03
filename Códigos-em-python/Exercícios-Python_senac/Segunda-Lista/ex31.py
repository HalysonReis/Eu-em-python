data = int(input('qual a idade do nadador? >>> '))

if data >= 5 and data < 12:
    print('infantil.')
elif data >= 12 and data <= 17:
    print('juvenil.')
elif data >= 18:
    print('senior.')