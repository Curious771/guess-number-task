"""Игра угадай число
Компьютер сам загадывает и сам угадывает число не более чем за 20 попыток
"""

import numpy as np
import random

random_number = random.randint(1, 101)


def game_score_v3(number: int = 1)->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1
    stop = 100

    while True:
        count += 1
        average_number = (start + stop)//2
        if average_number == random_number:
            print(f'число {average_number} найдено за {count} попыток')
            break #если число угадано
        elif average_number > random_number:
            stop = average_number
        else:
            start = average_number
    
    return count

def score_game(game_score_v3)->int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_score_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток 
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(game_score_v3(number))
    score=int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    return score

# RUN
if __name__ == '__main__':
    score_game(game_score_v3)