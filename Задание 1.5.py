cash = int(input("Введите значение выручки за очетный период:"))
cost = int(input("Введите значение издержек за очетный период:"))
raznica = cash - cost
while cash > cost:
    print(f"Прибыль компании {raznica} рублей")
    print(f"Рентабильность составит {cash / cost:.2f}")
    people = int(input("Сколько человек работает в компании?"))
    print(f"Прибыль на одного сотрудника составит {raznica / people:.2f} рублей")
    break
if cash <= cost:
    print(f"Компания на гране банкротства, долги составляют {raznica} рублей")




