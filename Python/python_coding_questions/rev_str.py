def reversed_words(input_string):
    words = input_string.split(" ")
    rev_words = []
    for word in words:
        rev_words.append(word[::-1])
    return " ".join(rev_words)

inp = "Hey this is Sapna"
output = reversed_words(inp)
print(output)

