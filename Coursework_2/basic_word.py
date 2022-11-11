class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"BasicWord({self.word}, {self.sub_words})"

    def sub_words_count(self):
        '''Считает количество подслов'''
        return len(self.sub_words)

    def has_sub_word(self, word):
        '''Проверяет присудствие подслова'''
        return word in self.sub_words

    def get_word(self):
        '''Получает оригинал слова'''
        return self.word


