def main():
    words_to_count = {}
    text = input("text: ")
    words = text.split()
    for word in words:
        try:
            words_to_count[word] += 1
        except KeyError:
            words_to_count[word] = 1
    keywords = list(words_to_count.keys())
    keywords.sort()
    max_length = max((len(word) for word in keywords))
    for word in keywords:
        print("{:{}} : {}".format(word, max_length, words_to_count[word]))


main()
