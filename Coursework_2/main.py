from player import Player
from config import data_path
from utils import get_random_word

user_name = input("Ввведите имя игрока \n")

basic_word = get_random_word(data_path)
player = Player(user_name)

print(
    f'\nПривет {user_name}!\nСоставьте {basic_word.sub_words_count()} слов из слова {basic_word.get_word().upper()}\nСлова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите "stop"\nПоехали, ваше первое слово?')


while player.used_words_count() < basic_word.sub_words_count():

    user_word = input()

    if len(user_word) < 3:
        print('слишком короткое слово')

    elif user_word.lower() in ['stop', 'стоп']:
        break

    elif not basic_word.has_sub_word(user_word):
        print('неверно')

    elif player.word_examination(user_word):
        print('уже использовано')

    else:
        print('верно')
        player.add_word(user_word)

print(f'Игра завершена, вы угадали {player.used_words_count()} слов!')
