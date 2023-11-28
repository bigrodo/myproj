def count_repeated_digits(input_string):
    digit_count = {}

    for digit in input_string:
        digit = int(digit)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)

    result = {}
    for digit, count in sorted_digits[:3]:
        result[digit] = count

    return result


input_string = "546723487920134"
result_dict = count_repeated_digits(input_string)

print("Словарь из трех самых часто встречаемых чисел:", result_dict)