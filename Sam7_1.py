def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        most_common_word = max(word_frequency, key=word_frequency.get)

        return word_count, most_common_word, word_frequency

file_path = 'statia.txt'
word_count, most_common_word, word_frequency = count_words(file_path)

print(f"Количество слов в файле: {word_count}")
print(f"Самое часто встречающееся слово: {most_common_word}")
print("Частота каждого слова:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")