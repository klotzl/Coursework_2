class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f"Player({self.name}, {self.used_words}"

    def used_words_count(self):
        '''Получение количества использованных слов'''
        return len(self.used_words)

    def add_word(self, word):
        '''Добавление слова в использованные слова'''
        self.used_words.append(word)

    def word_examination(self, word):
        '''Проверка использования данного слова до этого'''
        return word in self.used_words
