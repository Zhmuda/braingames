import sys
from extra_files.brain_game_launcher import launch_game


def main():
    # Получаем имя модуля игры из аргументов командной строки
    if len(sys.argv) != 2:
        print("Usage: python brain_game_starter.py <game_module>")
        sys.exit(1)

    game_module_name = sys.argv[1]

    try:
        # Импортируем модуль игры по его имени
        game_module = __import__(game_module_name, fromlist=[''])
        launch_game(game_module)
    except ModuleNotFoundError:
        print(f"Error: Module '{game_module_name}' not found.")
        sys.exit(1)


if __name__ == '__main__':
    main()
