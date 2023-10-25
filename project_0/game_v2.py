
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



def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count



def game_core_v3(number: int = 1) -> int:
    """Устанавливаем верхнюю и нижнюю границы поиска, алгоритм угадывает число по принципу бинарного дерева,
    если число больше центрального числа в диапазоне поиска, тогда переопределяем нижнюю границу,
    она становится равной загаданному числу, если число меньше, то переопределяем вернюю границу,
    и так каждый раз сокращаем диапазон поиска в два раза.
    Функция принимает загаданной число, и возвращает количество попыток.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    max_num = 101 # Верхняя граница поиска
    min_num = 1 # Нижняя граница поиска
    
    while True:
        count +=1  
        mid = (max_num+min_num) // 2 # Находим центральное число в диапазоне
        if number == mid:
            break
        elif mid < number:
            min_num = mid
        else:
            max_num = mid        
    # Ваш код заканчивается здесь
    
    return count   
      
      

def score_game(random_predict) -> int:
    """ В среднем, за какое количество попыток, за 1000 подходов, угадывает число наш алгоритм

    Args:
        random_predict (_type_):Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = [] # Список для сохранения попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Массив из 1000 элементов, каждый из которых является случайным числом от 1 до 100
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # Находим среднее количество попыток
    
    print(f'Алгоритм угадывает число в среднем за {score} раз')
    return score


# RUN
if __name__ == '_main_': # Если главный скрипт выполняется в этом файле, условие выполняется, если код будет импортирован, фенкция запускаться не будет
    score_game(game_core_v3)


    
        
        