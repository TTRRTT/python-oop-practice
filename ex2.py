import numbers

class TriangleChecker:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def is_triangle(self):
        if not isinstance(self.__a, numbers.Number) \
            or not isinstance(self.__b, numbers.Number) \
            or not isinstance(self.__c, numbers.Number):
            print('Нужно вводить только числа!')
        elif self.__a <= 0 or self.__b <= 0 or self.__c <= 0:
            print('С отрицательными числами ничего не выйдет (как и с нулем)!')
        elif (self.__a + self.__b > self.__c) \
            and (self.__a + self.__c > self.__b) \
            and (self.__b + self.__c > self.__a):
            print('Ура, можно построить треугольник!')
        else:
            print('Жаль, но из этого треугольник не сделать')

tr1 = TriangleChecker(2, 4, 7)
tr2 = TriangleChecker(4, 'fds', 8)
tr3 = TriangleChecker(8, 1, -20)
tr4 = TriangleChecker(3, 0, 2)
tr5 = TriangleChecker(1.2, 4.2, 3.1)

tr1.is_triangle()
tr2.is_triangle()
tr3.is_triangle()
tr4.is_triangle()
tr5.is_triangle()
