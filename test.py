#! /usr/bin/python3

import numpy as np

from function_types.polynomial_function import PolynomialFunction

def main() -> None:
    f = PolynomialFunction(np.array([3, 4, -3, 2, 7, -23]), np.array([6, 5, 3, 2, 1, 0]))
    g = PolynomialFunction(np.array([7, 8]), np.array([3, 2]))

    print(f'f(x) = {f}')
    print(f'g(x) = {g}')

    h = f * g

    print(f'h(x) = f(x) * g(x) = {h}')


if __name__ == '__main__': main()