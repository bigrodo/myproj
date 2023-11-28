def load_prohibited_words(file_path):
    with open(file_path, 'r') as file:
        prohibited_words = file.read().split()
    return prohibited_words

def censor_sentence(sentence, prohibited_words):
    words = sentence.split()
    censored_words = []

    for word in words:
        lowercase_word = word.lower()
        if lowercase_word in prohibited_words:
            censored_word = '*' * len(word)
            censored_words.append(censored_word)
        else:
            censored_words.append(word)

    censored_sentence = ' '.join(censored_words)
    return censored_sentence

def main():
    prohibited_words_file = 'input2.txt'
    sentence = input("Введите предложение: ")

    prohibited_words = load_prohibited_words(prohibited_words_file)
    censored_sentence = censor_sentence(sentence, prohibited_words)

    print("Цензурированное предложение:")
    print(censored_sentence)

if __name__ == "__main__":
    main()