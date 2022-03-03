#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word1, word2 = input("Введите два слова: ").split()
    if word1 == word2:
        print("Все символы в этих словах одинаковые!")
        exit(0)
    else:
        k = 0
        for i in range(len(word1)):
            if word1[i] in word2[i]:
                k += 1
            else:
                break
    print(f"В данных словах содержится {k} одинаковых начальных символов")
