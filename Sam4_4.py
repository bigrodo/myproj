def avergens(*args):
    if not args:
        return 0
    a =sum(args)
    b = len(args)
    c = a/ b
    return c

if __name__ == "__main__":
    result = avergens(2, 4, 5, 7, 1, 5, 8)
    print(f"Среднее арифметическое: {result}")