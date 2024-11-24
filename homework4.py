first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda word1, word2: word1 == word2, first, second))

def get_advanced_writer(file_name):
        def write_everything(*data_set):
                with open(file_name, 'w', encoding='utf-8') as file:
                        for data in data_set:
                                print(data, file = file)

                return write_everything
        write = get_advanced_writer('example.txt')
        write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        from random import choice
        return choice(self.words)

from random import choice
#Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Выведет случайный ответ из списка
print(first_ball())  # Выведет еще один случайный ответ
print(first_ball())  # И еще один случайный ответ