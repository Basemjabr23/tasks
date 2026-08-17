sentence = input("Enter a sentence: ")

print("Length:", len(sentence))

words = sentence.split()
print("First word:", words[0])

print("Reversed:", sentence[::-1])