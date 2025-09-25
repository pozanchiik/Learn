"""Тестовий файл для ознайомлення з правилами форматування і оформлення коду згідно Python Enhancement Proposals PEP 8 – Style Guide for Python Code."""
# розділити перший рядок до слова "згідно", поставити крапку, зробити 1 пустий рядок

import string
import os # Не використовується
import math, time # Краще імпортувати кожен модуль з нового рядка, імпорт "math" не використовується

shift = 3 #назва константи пишеться виключно у верхньому регістрі
PI= 3.14   #Ця змінна не використовується

def PrintTime(x): # Назви функцій повинні бути у нижньому регістрі з підкресленнями між словами;
    # пояснити знизу за допомогою потрійних лапок зміст функції; потрібна більш конкретна назва змінній x
   if x == True:  # Можна спростити до if x: ; потрібна більш конкретна назва змінній x
      print( time.ctime() ) # Пробіл між функцією і дужками не потрібен
   return # return не потрібен

def main ():  # Пробіл між назвою функції і дужками не потрібен; пояснити знизу за допомогою потрійних лапок, що зміст функції
    Choice_mode = input("would you like to encode or decode?") # Назви змінних у нижньому регістрі
    word = input("Please enter text")
    LETTERS = string.ascii_letters + string.punctuation + string.digits # Назви змінних у нижньому регістрі
    encoded = ""
    if Choice_mode == "encode": # назви змінних у нижньому регістрі
        for letter in word:
            if letter == " ":
                encoded = encoded + " " # Можна спростити до encoded += " "
            else:
                x = LETTERS.index(letter) + shift # Краще придумати більше інформативну назву для змінної x; назви змінних у нижньому регістрі
                encoded = encoded + LETTERS[x] # Можна спростити до encoded += LETTERS[x]; назви змінних у нижньому регістрі
                y=x + 5 # Змінна y не використовується; коректніше буде мати структуру y = x + 5



    if Choice_mode is "decode": # Краще використовувати == замість is для порівняння значень; назви змінних у нижньому регістрі
        for letter in word:
            if letter == " ":
                encoded = encoded+" " # Можна спростити до encoded += " "
            else:
                x = LETTERS.index(letter)- shift  # x = LETTERS.index(letter) - shift; назви змінних у нижньому регістрі; потрібна більш конкретна назва змінній x
                encoded=encoded + LETTERS[x] # Можна спростити до encoded += LETTERS[x]; назви змінних у нижньому регістрі
                y= x - 5  # Змінна y не використовується; коректніше буде мати структуру y = x + 5

    print(encoded)
    print(Word)  # Word не визначена



if __name__ == '__main__':
    main()

