try:
    number = float(input("Введіть число: "))
    number = int(number)
    print("Ціле число:", number)

except ValueError:
    print("Помилка! Ви ввели не число.")