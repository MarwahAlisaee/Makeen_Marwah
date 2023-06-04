def find_word(sentence, target):
    words = sentence.split()
    for index, word in enumerate(words, 1):
        if word == target:
            return f"I found {target} at {index}"
    return f"I didn't find {target}"

input_sentence = input("Enter a sentence: ")
target_word = "CodeAcademy"

result = find_word(input_sentence, target_word)
print(result)
