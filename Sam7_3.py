def calculate_statistics(file_path):
    letter_count = 0
    word_count = 0
    line_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1

            letter_count += sum(c.isalpha() for c in line)

            word_count += len(line.split())

    print(f"Letters: {letter_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")

calculate_statistics('input1.txt')