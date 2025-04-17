# exercicio 5

primo = int(input("Insira um número: "))
contador = 0

if primo < 2:
    print("Números menores que 2 não são primos.")
else:
    for num in range(1, primo + 1):
        if primo % num == 0:
            contador += 1
    if contador == 2:
        print("O número inserido é primo.")
    else:
        print("O número inserido não é primo.")
