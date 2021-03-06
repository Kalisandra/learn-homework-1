"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

def str_exercises(str1, str2):
    if type(str1) != str or type(str2) != str:
        return '0'
    elif str1 == str2:
        return '1'
    elif len(str1) > len(str2) and str2 != 'learn':
        return '2'
    elif str1 != str2 and str2 == 'learn':
        return '3'

str1 = 123
str2 = True
various_str = str_exercises(str1, str2)
print(various_str)

str1 = 'Alex'
str2 = 'Alex'
various_str = str_exercises(str1, str2)
print(various_str)

str1 = 'Exercise'
str2 = 'String'
various_str = str_exercises(str1, str2)
print(various_str)

str1 = 'Alex'
str2 = 'learn'
various_str = str_exercises(str1, str2)
print(various_str)
    
if __name__ == "__main__":
    main()
