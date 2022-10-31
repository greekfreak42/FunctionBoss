#! /usr/bin/python3

import numpy as np

from functions.gr_function import GR_Function

def main() -> None:
    f = GR_Function(np.array([-1, 3]), np.array([3, 2]))
    g = f.get_differentiated()

    print(f)
    print(g)


if __name__ == '__main__': main()