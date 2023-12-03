def add_numbers():
    try:
        number1 = 2
        number2 = int(input("Введите число: "))
        result = number1 + number2
        print(f"Сумма чисел: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


add_numbers()
add_numbers()
add_numbers()