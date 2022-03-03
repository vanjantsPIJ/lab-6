#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word = input("Введите слово: ")
    k = len(word)
    print(f"Длина слова: {k}")
    word = k * '*' + word + k * '*'
    print(word)