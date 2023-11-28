import random

def main():
    cub = random.randint(1, 6)
    print("Вы бросили кубик")
    print(f"Выпало: {cub}")
    if cub == 5 or cub == 6:
        print("Вы победили!")
    elif cub == 3 or cub == 4:
        main()
    else:
        print("Вы проиграли!")

if __name__ == "__main__":
    main()