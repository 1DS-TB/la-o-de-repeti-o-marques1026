# exercicio 5

primo = int(input("insira um numero: "))
contador = 0
for num in range (1, primo +1):
    if (primo % num) == 0:
        contador = contador + 1
if contador == 2:
    print("o numero inserido é primo")
else:
    print("o numero inserido não é primo")
