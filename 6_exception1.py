"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dir_quest = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    """
    Замените pass на ваш код
    """
    try:
      while True:
        user_say = input('задай вопрос?')
        print(user_say)
        print(dir_quest.get (user_say))
    except(KeyboardInterrupt):
      print('Пока!')
    
if __name__ == "__main__":
    ask_user()
