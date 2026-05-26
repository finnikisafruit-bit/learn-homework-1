"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

products = [

    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},

    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},

    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},

  ]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for product in products:
        total_sold = sum(product['items_sold'])
        product['total_sold'] = total_sold
        product['average_sold'] = round(total_sold / len(product['items_sold']))

    summary = 0
    summary_average = 0

    for product in products:
        summary += product['total_sold']
        summary_average += product['average_sold']
        print(f'{product["product"]} было продано {product["total_sold"]} штук')
        print(f'{product["product"]} было продано в среднем {product["average_sold"]} штук')
    

    print(f'Суммарное количество продаж всех товаров {summary}')
    print(f'Суммарное количество продаж всех товаров {summary_average}')
    
if __name__ == "__main__":
    main()
