def longest(sentence: str):
    result = None
    char_count = 0
    for word in sentence.split(' '):
        if len(word) > char_count:
            char_count = len(word)
            result = word
    return '{}: {} characters'.format(result, char_count)


if __name__ == "__main__":
    print(longest('Saya sangat senang mengerjakan soal algoritma'))
