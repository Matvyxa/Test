a = int(input('Введите целое число '))
b = a % 10
while b >= a:
    b = b / 10
print(b)


