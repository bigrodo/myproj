class CustomException(Exception):
    def __init__(self, message):
        self.message = message

# Функция, которая может вызвать исключение.
def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Делить на ноль нельзя!")
    else:
        return a / b

# Фрагмент кода, который обрабатывает исключение.
try:
    result = divide_numbers(30, 3)
    print("Результат деления:", result)
except CustomException as e:
    print("Исключение:", e.message)

# Еще один фрагмент кода, который также обрабатывает исключение.
try:
    result = divide_numbers(5, 0)
    print("Результат деления:", result)
except CustomException as e:
    print("Исключение:", e.message)