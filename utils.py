import random
import requests
from basic_word import BasicWord


def load_random_word():
    """
    загрузка словаря со словами из внешнего ресурса и
    передача рандомного слова со списком возможных слов
    в класс BasicWord
    """
    word_set = requests.get('https://api.npoint.io/f9b8e04835d451d02df0')
    word_set_json = word_set.json()

    word_random = random.choice(word_set_json)
    basic_word = BasicWord(word_random.get('word'), word_random.get('subwords'))

    return basic_word


def check_word(basic_word, player):
    """
    запускает цикл, которые проверяет пользовательские слова на корректность
    и, в случае, успеха, вызывает метод добавления слов в список
    Так же, подсчитывает количество верных слов
    """
    while basic_word.sub_words_count() - player.getting_number_words_used() != 0:
        user_answer = input()
        if len(user_answer) < 3:
            print('слишком короткое слово')
        elif basic_word.sub_words_check(user_answer) is True:
            if player.checking_the_use(user_answer) is True:
                print('уже использовано')
            else:
                player.adding_word_to_used_words(user_answer)
                print('верно')
        elif user_answer in ['stop', 'стоп']:
            print(f'Игра завершена, вы угадали {len(player.words_used)} слов!')
            quit()
        else:
            print('неверно')
    print(f'Игра завершена, вы угадали {len(player.words_used)} слов!')
