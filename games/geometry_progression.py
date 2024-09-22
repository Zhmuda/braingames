import random
from constants import (
    MIN_RANDOM_NUMBER,
    MAX_RANDOM_NUMBER,
    MAX_PROGRESSION_LENGTH
)

GAME_QUEST = 'What number is missing in the geometric progression?'


# Генерируем вопрос и ответ для geometric progression
def question_and_answer():
    """Brain-geometric-progression

    Цель игры: определить число, которое заменено в геометрической
    прогрессии двумя точками.

    """
    start_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    ratio = random.randint(2, MAX_RANDOM_NUMBER)  # Множитель для геометрической прогрессии
    progression_length = random.randint(5, MAX_PROGRESSION_LENGTH)

    sequence = make_geometric_progression(start_number, ratio, progression_length)
    random_index = random.randint(0, len(sequence) - 1)

    answer = sequence[random_index]
    sequence[random_index] = ".."

    question = ' '.join(str(num) for num in sequence)
    return question, answer


# Создаем геометрическую прогрессию
def make_geometric_progression(start, ratio, length):
    progression = [start]
    current_number = start
    while len(progression) < length:
        current_number *= ratio  # Для геометрической прогрессии умножаем на ratio
        progression.append(current_number)
    return progression
