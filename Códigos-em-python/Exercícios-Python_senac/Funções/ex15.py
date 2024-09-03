def maior(num1, num2, num3):
    numeros = [num1, num2, num3]
    maior = 0

    for num in numeros:
        if num > maior:
            maior = num
    
    return maior

comparar = maior(22567,566, 44)

print('o maior ', comparar)