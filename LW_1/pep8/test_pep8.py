"""Тестовий файл для ознайомлення з правилами форматування і оформлення коду.

згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code.
"""

import string
import time

SHIFT = 3


def print_time(show_time):
    """Виводить поточний час, якщо show_time == True."""
    if show_time:
        print(time.ctime())


def main():
    """Кодує або декодує текст залежно від mode ('encode' або 'decode')."""
    choice_mode = input("would you like to encode or decode?")
    word = input("Please enter text")
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""

    if choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                index = letters.index(letter) + SHIFT
                encoded += letters[index]

    if choice_mode == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                index = letters.index(letter) - SHIFT
                encoded += letters[index]

    print(encoded)


if __name__ == '__main__':
    main()
