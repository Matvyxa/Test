while True:
    days = 1
    start = int(input("Введите дистанцию для начала тренировок: "))
    finish = int(input("Введите дистанцию для достижения цели: "))
    if finish < 0 or start <= 0 or finish < start:
        print("Введите правильные данные")
    else:
        while finish > start:
            start = start + 0.1 * start
            days += 1
        print(f"Через {days} результат будет дастигнут")
        break

