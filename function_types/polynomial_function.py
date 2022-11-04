import numpy as np

class PolynomialFunction:
    def __init__(self, a: np.ndarray, m: np.ndarray) -> None:
        assert len(a) == len(m)

        self.a = a
        self.m = m
    

    def get_differentiated(self):
        assert len(self.a) == len(self.m)
        n = len(self.a)

        new_a = np.empty(n)
        new_m = np.empty(n)

        for i in range(n):
            new_a[i] = self.a[i] * self.m[i]
            new_m[i] = self.m[i] - 1
        
        return PolynomialFunction(new_a, new_m)
    

    def _summarize(self) -> None:
        elements = {}

        assert len(self.a) == len(self.m)

        for i in range(len(self.a)):
            if self.m[i] not in elements.keys(): elements.update({self.m[i] : self.a[i]})
            else: elements[self.m[i]] += self.a[i]
        
        new_size = len(elements)
        new_a = np.empty(new_size)
        new_m = np.empty(new_size)

        for i in range(len(new_m)):
            max_exp = max(elements.keys())
            new_m[i] = max_exp
            new_a[i] = elements[max_exp]
            del elements[max_exp]
        
        self.a = new_a
        self.m = new_m
    

    def __add__(self, other):
        result = PolynomialFunction(self.a.copy(), self.m.copy())

        for i, exp in enumerate(other.m):
            if exp in result.m:
                idx = np.where(result.m == exp)[0][0]
                result.a[idx] += other.a[i]
            else:
                np.append(result.a, other.a[i])
                np.append(result.m, other.m[i])
                result._summarize()
        
        return result
    

    def negated(self): return PolynomialFunction(self.a * -1, self.m.copy())


    def __sub__(self, other): return self + other.negated()


    def __mul__(self, other):
        if type(other) is not PolynomialFunction: return PolynomialFunction(self.a * other, self.m.copy())

        assert len(self.a) == len(self.m)
        assert len(other.a) == len(other.m)

        new_size = len(self.a) * len(other.a)

        new_a = np.zeros(new_size)
        new_m = np.zeros(new_size)

        for i in range(len(other.a)):
            for j in range(len(self.a)):
                new_a[j + i*len(self.a)] = other.a[i] * self.a[j]
                new_m[j + i*len(self.a)] = other.m[i] + self.m[j]
        
        result = PolynomialFunction(new_a, new_m)
        result._summarize()
        return result
    

    def __str__(self) -> str:
        assert len(self.a) == len(self.m)

        n = len(self.a)
        s = ''

        for i in range(n):
            if self.a[i] < 0: s += '-'
            elif i > 0: s += '+'

            if i > 0: s += ' '

            if self.m[i] == 0:
                s += str(abs(self.a[i]))
            elif self.m[i] == 1:
                s += f'{abs(self.a[i])}*x'
            else:
                s += f'{abs(self.a[i])}*x^{str(self.m[i])}'

            if i < n-1: s += ' '
    
        return s
    

    def __repr__(self) -> str: return self.__str__()