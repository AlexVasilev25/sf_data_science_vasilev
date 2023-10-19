"""Компьютер сам загадывает и сам угадывает число"""
import numpy as np


def random_predict(number: int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count +=1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break
    
    return count




def score_game(random_predict) -> int:
    """ В среднем, за какое количество попыток, за 1000 подходов, угадывает число наш алгоритм

    Args:
        random_predict (_type_):Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = [] # Список для сохранения попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # Массив из 1000 элементов, каждый из которых является случайным числом от 1 до 100
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # Находим среднее количество попыток
    
    print(f'Алгоритм угадывает число в среднем за {score} раз')
    return score


# RUN
if __name__ == '_main_': # Если главный скрипт выполняется в этом файле, условие выполняется, если код будет импортирован, фенкция запускаться не будет
    score_game(random_predict)


    
        
        