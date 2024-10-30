class Soda:
    def __init__(self, addition=''):
        self.__addition = addition

    def show_my_drink(self):
        if self.__addition == '':
            print('Обычная газировка')
        else:
            print('Газировка и', self.__addition)

soda = Soda()
soda1 = Soda('апельсин')
soda2 = Soda('сахар')

soda.show_my_drink()
soda1.show_my_drink()
soda2.show_my_drink()
