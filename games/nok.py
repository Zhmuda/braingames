import random
from constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER

GAME_QUEST = 'Find the least common multiple (LCM) of the given numbers.'


# Генерируем вопрос и ответ для LCM
def question_and_answer():
    """Game-LCM

    Цель игры: пользователю показывается три случайных числа,
    например, 5 7 15. Пользователь должен вычислить и ввести наименьшее
    общее кратное этих чисел.

    """
    number1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number3 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    question = f'{number1} {number2} {number3}'
    answer = calculate_lcm_of_three(number1, number2, number3)

    return (question, answer)


# Рассчитываем НОК двух чисел
def calculate_lcm(number1, number2):
    return abs(number1 * number2) // calculate_gcd(number1, number2)


# Рассчитываем НОК трёх чисел
def calculate_lcm_of_three(number1, number2, number3):
    return calculate_lcm(calculate_lcm(number1, number2), number3)


# Рассчитываем НОД (наибольший общий делитель)
def calculate_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if abs(number1) > abs(number2):
            number1 %= number2
        else:
            number2 %= number1
    return abs(number1 or number2)
