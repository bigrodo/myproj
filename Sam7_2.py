import os
import json

def input_expense():
    name = input("Введите название расхода: ")
    amount = float(input("Введите сумму расхода: "))
    date = input("Введите дату расхода (в формате ГГГГ-ММ-ДД): ")
    return {"name": name, "amount": amount, "date": date}

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file)

def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []

def display_expenses(expenses):
    if not expenses:
        print("Нет сохраненных расходов.")
    else:
        for expense in expenses:
            print(f"Название: {expense['name']}, Сумма: {expense['amount']}, Дата: {expense['date']}")

def main():
    expenses = load_expenses()

    while True:
        print("\nВыберите действие:")
        print("1. Ввести новый расход")
        print("2. Показать существующие расходы")
        print("3. Сохранить и выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            new_expense = input_expense()
            expenses.append(new_expense)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
            print("Расходы сохранены. Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()