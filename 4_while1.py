"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def hello_user():

  while True:
    s = input('Как дела?')
    if s == 'Хорошо':
      break
    
    
if __name__ == "__main__":
    hello_user()

