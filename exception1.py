"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    user_dict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Когда закончишь?': 'Не знаю'}
    def ask_user_dict():
        while True:        
            try:
                ask_question = input('Пользователь: ')
                if ask_question in user_dict.keys():
                    print(f"Программа: {user_dict[ask_question]}")  
            except KeyboardInterrupt:
                print('Пока!')
                break
    ask_user_dict()    
        


if __name__ == "__main__":
    ask_user()
