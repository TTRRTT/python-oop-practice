class RealString(str):
    def __lt__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) < len(other)
        else:
            raise ValueError('Cannot compare', self, 'and', other)

    def __le__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) <= len(other)
        else:
            raise ValueError('Cannot compare', self, 'and', other)

    def __gt__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) > len(other)
        else:
            raise ValueError('Cannot compare', self, 'and', other)

    def __ge__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) >= len(other)
        else:
            raise ValueError('Cannot compare', self, 'and', other)

    def __eq__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) == len(other)
        else:
            raise ValueError('Cannot compare', self, 'and', other)

str1 = 'Apple'
real_str1 = RealString('Яблоко')
real_str2 = RealString('Banana')

print(f'{str1} < {real_str1}? {str1 < real_str1}')
print(f'{real_str1} > {real_str2}? {real_str1 > real_str2}')
print(f'{str1} == {real_str1}? {str1 == real_str1}')
print(f'{real_str2} >= {real_str1}? {real_str2 >= real_str1}')
print(f'{real_str2} <= {str1}? {real_str2 <= str1}')
