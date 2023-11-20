predlozh = input("Введите предложение на английском: ")
print("Длина предложения: ", len(predlozh))
lowercase_predlozh = predlozh.lower()
print("Предложение в нижнем регистре: ", lowercase_predlozh)
vowels = "aeiou"
vowel_count = sum(1 for char in lowercase_predlozh if char in vowels)
print("Количество гласных: ", vowel_count)
replaced_predlozh = lowercase_predlozh.replace("ugly", "beauty")
print("Предложение с заменой 'ugly' на 'beauty': ", replaced_predlozh)
starts_with_the = lowercase_predlozh.startswith("the")
ends_with_end = lowercase_predlozh.endswith("end")

if starts_with_the:
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")
if ends_with_end:
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")