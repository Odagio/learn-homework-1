"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
       
    dir_scores = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4b', 'scores': [3,3,2,4,5]},
      {'school_class': '4c', 'scores': [5,4,3,5,4]}    
    ]
    
    score_sch = 0

    for score in dir_scores:
      score_sum = (sum(score['scores']))
      scores_avg = score_sum/ len(score['scores'])
      score_sch += score_sum/ len(score['scores']) 
      
      print (score['school_class'],scores_avg)
    print ('score',score_sch)

    
if __name__ == "__main__":
    main()
