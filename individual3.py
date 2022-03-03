#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    sentence = input("Введите предложение: ")
    sentence = sentence.replace('c', '')  # Удаление английских букв "с"
    sentence = sentence.replace('с', '')  # Удаление русских букв "с"
    sentence = sentence.replace('C', '') #Удаление английских букв "C"
    sentence = sentence.replace('С', '') # Удаление русских букв "С"
    print(sentence)
