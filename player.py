class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.words_used = []

    def getting_number_words_used(self):
        """
        проверяет, есть ли указанное пользователем слово,
        в списке правильных слов
        """
        return len(self.words_used)

    def adding_word_to_used_words(self, user_answer):
        """
        добавляет верные слова в список использованных слов
        """
        self.words_used.append(user_answer)

    def checking_the_use(self, user_answer):
        """
        проверяет повторяемость пользовательских слов
        """
        return user_answer in self.words_used

    def __repr__(self):
        return f'user {self.user_name}'
