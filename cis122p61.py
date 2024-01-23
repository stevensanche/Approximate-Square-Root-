"""
CIS 122 Spring 2022 Project 6-1
Author: Steven Sanchez Jimenez
Credit: CIS 122 Resources, Office Hours
Description: Approximate Square Root
"""
import math




def mysqrt(a):
    """
    This function will give an approximation of the square root of a.

    >>>mysqrt(3)
    1.7320508075688772
    """
    epsilon = .0000001
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        else:
            x = y
    return y


def square_root_compare():
    """
    This function will compare my function of a square root and the actual square
    root function from the math import.

    >>>square_root_compare()
    1    1.0                      1.0                      0.0
    2    1.414213562373095        1.4142135623730951       2.220446049250313e-16
    3    1.7320508075688772       1.7320508075688772       0.0
    4    2.000000000000002        2.0                      2.220446049250313e-15
    5    2.23606797749979         2.23606797749979         0.0
    6    2.449489742783178        2.449489742783178        0.0
    7    2.6457513110645907       2.6457513110645907       0.0
    8    2.82842712474619         2.8284271247461903       4.440892098500626e-16
    9    3.0                      3.0                      0.0
    10   3.162277660168379        3.1622776601683795       4.440892098500626e-16
    """
    for i in range(1, 1000):
        own = mysqrt(i)
        py = math.sqrt(i)
        difference = abs(own - py)
        print(f'{i:<5}{own:<25}{py:<25}{difference:<25}')
    return


def main():
    """driver"""
    # print table header
    print('\nSquare Root Calculator\n')
    print(f'{"a":5}{"mysqrt(a)":25}{"math.sqrt(a)":25}{"diff":25}')
    square_root_compare()
    return


main()
