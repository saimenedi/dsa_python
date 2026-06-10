def count_words(sentence):

    count = 1

    for char in sentence:
        if char == ' ':
            count += 1
    return count


sentence = "Programming is fun and challenging"
print("Number of words:", count_words(sentence))
