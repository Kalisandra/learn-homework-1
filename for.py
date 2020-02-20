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
    
school = [
    {'school_class': '1', 'scores': [5,4,3,5,4,3]}, 
    {'school_class': '2', 'scores': [4,4,3,5,5,2]},
    {'school_class': '3', 'scores': [5,5,3,4,5,5]},
    {'school_class': '4', 'scores': [3,3,4,4,5,5]}
]

sch_score_sum = 0
n_cl = 0
for cl in school:
    cl_scores_sum = 0
    for score in cl['scores']:
        cl_scores_sum += score
    avr_cl_score = cl_scores_sum / len(cl['scores'])
    print(f"средний бал по классу {cl['school_class']}: {avr_cl_score}")
    n_cl += 1
    sch_score_sum += avr_cl_score 
avr_sch_score = sch_score_sum / n_cl

print(f"средний бал по школе {avr_sch_score}")


    
if __name__ == "__main__":
    main()
