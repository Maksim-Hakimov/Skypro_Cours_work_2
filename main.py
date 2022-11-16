from player import Player
from utils import load_random_word, check_word

if __name__ == '__main__':
    user_name = input('Ввведите имя игрока: ')
    player = Player(user_name)
    basic_word = load_random_word()

    print(f'Привет, {user_name}!')
    print(f'Составьте {basic_word.sub_words_count()} слов из слова {basic_word.word}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    check_word(basic_word, player)
