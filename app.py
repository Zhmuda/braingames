import prompt
from cli import welcome_user
from constants import AMOUNT_OF_ROUNDS

def run_start_to_end(game):
    name = welcome_user()
    count = 0
    while count < AMOUNT_OF_ROUNDS:
        question, answer = game.question_and_answer()
        print(game.GAME_QUEST)
        print(f'Question: {question}')
        user_input = prompt.string('Your answer: ')
        if user_input.lower() != str(answer):
            print(f"'{user_input}' is wrong answer ;(.")
            print(f'Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')
