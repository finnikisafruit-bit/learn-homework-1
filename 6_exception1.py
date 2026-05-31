"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def hello_user():
  while True:
    try:
      s = input('Как дела?')
      if s == 'Хорошо':
        break
    except KeyboardInterrupt:
      print('Пока!')
      break

if __name__ == "__main__":
    hello_user()
