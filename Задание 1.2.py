sec = int(input("Введите время в секунадах"))
h = sec // 3600
m = (sec // 60) - (h * 60)
s = sec % 60
print(f"{h:02}:{m:02}:{s:02}")
