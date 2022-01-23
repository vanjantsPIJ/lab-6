word = input("Введите слово: ")
k = len(word)
print(f"Длина слова: {k}")
word = k * '*' + word + k * '*'
print(word)