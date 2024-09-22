import random
from constants import MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER
import math

GAME_QUEST = 'Find the least common multiple (LCM) of the given numbers.'

# Генерируем вопрос и ответ для LCM
def question_and_answer():
    """Game-LCM"""
    number1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number3 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    question = f'{number1} {number2} {number3}'
    answer = calculate_lcm_of_three(number1, number2, number3)

    return question, answer

# Рассчитываем НОК двух чисел
def calculate_lcm(number1, number2):
    return abs(number1 * number2) // math.gcd(number1, number2)

# Рассчитываем НОК трёх чисел
def calculate_lcm_of_three(number1, number2, number3):
    return calculate_lcm(calculate_lcm(number1, number2), number3)
