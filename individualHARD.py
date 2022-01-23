word1, word2 = input("Введите два слова: ").split()
for ch in word1:
    if ch in word2:
        print("Да", end=" ")
    else:
        print("Нет", end=" ")