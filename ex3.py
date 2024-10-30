class KgToPounds:
    def __init__(self, kg=1):
        self.kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

kg5 = KgToPounds(5)
kgX = KgToPounds()
kgX.kg = 10

print(kg5.kg)
print(kgX.kg)

# Raising error
kgN = KgToPounds('n')
print(kgN.kg)
