import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):
    '''Определяем минимальное и максимальное значения, в которых компьютер
    будет искать число, счетчик попыток первоначально устанавливаем на 1,
    чтобы при совпадение созданных чисел засчитывался результат'''
    count = 1
    predict = np.random.randint(1, 101)
    min_value = 1
    max_value = 100
    while number != predict:
        count += 1
        '''Определяем разность между predict и number и выясняем в дальнейшем является ли
        она четной или нет, чтобы сократить количество циклов'''
        differense = predict - number
        if differense % 2 == 0:
            if differense > 0:
                max_value = predict - 2
            else:
                min_value = predict + 2
        else:
            if differense > 0:
                max_value = predict
            else:
                min_value = predict + 1
        '''Рассчитываем число исходя из измененных минимальных и максимальных значений'''
        predict = (min_value + max_value) // 2
    return count


score_game(game_core_v2)
