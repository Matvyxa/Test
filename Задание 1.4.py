# не смог свое первоначальное решение адаптировать, скопировал решение через хранилище
num_init = int(input("Ввведите целое положительное число: "))
zero = 0
num = num_init
while num > 0:
    big = num % 10
    if big > zero:
        zero = big
    num = num // 10
print(f"Наибольшая цифра в числе {num_init} равна {zero}")



