import numbers

class Nikola:
    __slots__ = ('__name', '__age')

    def __init__(self, name='Николай', age=10):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, numbers.Number) or value.lower() == 'николай':
            self.__name = 'Николай'
        else:
            self.__name = 'Я не ' + value + ', а Николай'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError('Автору 0 лет')

nik = Nikola()
nik1 = Nikola('Максим')
nik2 = Nikola(34)

print(nik.name)
print(nik1.name)
print(nik2.name)

# Exception raised
nik.surname = 'Иванов'
print(nik.name, nik.surname)
