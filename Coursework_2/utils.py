import random
import requests
from basic_word import BasicWord


def load_data_from_json(filename) -> list[dict]:
    '''Напишите функцию `load_random_word()` в файле `utils`, которая:
    - получит список слов с внешнего ресурса,
    - выберет случайное слово,
    - создаст экземпляр класса `BasicWord`,
    - вернет этот экземпляр.'''
    result = requests.get(filename)
    data = result.json()

    return data


def get_random_word(filename) -> BasicWord:
    '''Загружает данные по адресу и возвращает экземпляр BasicWord'''
    words_list = load_data_from_json(filename)
    random_word = random.choice(words_list)

    word_value = random_word["word"]
    sub_words_value = random_word["subwords"]

    basic_word = BasicWord(word_value, sub_words_value)

    return basic_word
