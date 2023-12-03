def uppercase_decorator(func):
    def wrapper(text):
        # Преобразуем текст в верхний регистр.
        upper_text = text.upper()
        # Вызываем оригинальную функцию с преобразованным текстом.
        return func(upper_text)
    return wrapper

# Функция, которая будет использовать декоратор.
@uppercase_decorator
def print_message(text):
    print(text)

# Функция, которая также будет использовать декоратор.
@uppercase_decorator
def get_length(text):
    length = len(text)
    print(f"Длина текста: {length}")

# Вызываем функции.
print_message("qwerty123!")
get_length("qwerty123!")