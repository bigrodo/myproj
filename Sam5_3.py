import math
one = [12, 25, 3, 48, 71] 
two = [5, 18, 40, 62, 98] 
three = [4, 21, 37, 56, 84]

def main(one, two, three):
    max_one = sorted(one)[-1]
    max_two = sorted(two)[-1]
    max_three = sorted(three)[-1]
    min_one = sorted(one)[0]
    min_two = sorted(two)[0]
    min_three = sorted(three)[0]
    max_p = (max_one + max_two + max_three)/2
    max_s = math.sqrt((max_p * (max_p - max_one) * (max_p - max_two) * (max_p - max_three)))
    min_p = (min_one + min_two + min_three)/2
    min_s = math.sqrt((min_p * (min_p - min_one) * (min_p - min_two) * (min_p - min_three)))
    print(f'Площадь треугольника из минимальных стророн {min_s}')
    print("Площадь треугольника из максимальных строн", max_s)


if __name__ == "__main__":
    main(one, two, three)