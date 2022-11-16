class BasicWord:
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def sub_words_check(self, user_answer):
        """
        проверяет, есть ли указанное пользователем слово,
        в списке правильных слов
        """
        return user_answer.strip().lower() in self.sub_words

    def sub_words_count(self):
        """
        считает количество слов списке правильных слов
        """
        return len(self.sub_words)

    def __repr__(self):
        return f'word - {self.word}, ({self.sub_words})'
