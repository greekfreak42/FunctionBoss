import numpy as np

class PolynomialFunction:
    def __init__(self, a: np.ndarray, m: np.ndarray) -> None:
        assert len(a) == len(m)

        self.a = a
        self.m = m
    

    def get_differentiated(self):
        assert len(self.a) == len(self.m)
        n = len(self.a)

        new_a = np.zeros(n)
        new_m = np.zeros(n)

        for i in range(n):
            new_a[i] += self.a[i] * self.m[i]
            new_m[i] += self.m[i] - 1
        
        return PolynomialFunction(new_a, new_m)
    

    def __str__(self) -> str:
        assert len(self.a) == len(self.m)

        n = len(self.a)
        s = ''

        for i in range(n):
            if self.a[i] < 0: s += '-'
            elif i > 0: s += '+'

            if i > 0: s += ' '

            s += f'{abs(self.a[i])}*x^{str(self.m[i])}'

            if i < n-1: s += ' '
    
        return s
    

    def __repr__(self) -> str: return self.__str__()