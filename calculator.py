######### CALCULATOR

"""
pip install numpy
pip install statistics
"""

import numpy as np
import statistics as st


def head():
    # header
    for i in range(40):
        print('-', end='')
    print()
    print('|', 'Calculator'.rjust(23), '|'.rjust(14))
    for i in range(40):
        print('-', end='')

    # body
    print()
    # print('|', ' '*36, '|')
    print('|', 'Menu'.ljust(36), '|')
    print('|', '1. Calculate'.ljust(36), '|')
    print('|', '2. Base-N'.ljust(36), '|')
    print('|', '3. Matrix'.ljust(36), '|')
    print('|', '4. Statistics'.ljust(36), '|')
    print('|', '5. Polynomial Roots'.ljust(36), '|')
    print('|', '6. Simul Equations'.ljust(36), '|')
    print('|', '7. Exit Calculator'.ljust(36), '|')
    for i in range(40):
        print('-', end='')


def calculate():
    exp = input('Enter an expression (+, -, *, /, ^): ')
    exp = exp.replace('^', '**')
    try:
        print('Answer:', eval(exp))
    except:
        print('Invalid Expression.')
        return False

    return True


def baseN():
    bases = {1: 2, 2: 8, 3: 10, 4: 16}
    print('''1. Binary
2. Octal
3. Decimal
4. Hex''')
    ch = int(input('Base of the input number: '))
    inp = input('Enter a number: ')
    try:
        inp = int(inp, bases[ch])
    except:
        print('Invalid number')
        return False

    ch2 = int(input('Base of the number to be converted to: '))

    if ch2 == ch:
        print('Both the bases are equal')

    elif ch2 == 1:
        print('binary:', str(bin(inp))[2::])

    elif ch2 == 2:
        print('octal:', str(oct(inp))[2::])

    elif ch2 == 3:
        print('decimal:', inp)

    elif ch2 == 4:
        print('hex:', str(hex(inp))[2::])

    else:
        print('Invalid Input! Try Again.')
        return False

    return True


def matrices():
    # matrices
    r1, c1 = map(int, input('Enter space-separated rows and columns of first matrix: ').split())
    a = np.array(list(map(int, input('Enter first matrix spaced row-wise numbers: ').split())))
    try:
        a = a.reshape(r1, c1)
    except:
        print('Invalid number of elements!')
        return False

    r2, c2 = map(int, input('Enter space separated rows and columns of second matrix: ').split())
    b = np.array(list(map(int, input('Enter second matrix spaced row-wise numbers: ').split())))
    # l2 = np.array(l2)
    try:
        b = b.reshape(r2, c2)
    except:
        print('Invalid number of elements!')
        return False

    print()
    print('''1. Matrix addition
2. Matrix subtraction
3. Matrix multiplication
4. Transpose
5. Determinant
6. Inverse
7. Exit Matrix Calculations''')

    while True:
        print()
        ch = int(input('Enter a matrix operation: '))

        if ch == 1:
            try:
                print(np.add(a, b))
            except:
                print('Invalid dimensions')

        elif ch == 2:
            try:
                print(np.subtract(a, b))
            except:
                print('Invalid dimensions')

        elif ch == 3:
            try:
                print(np.dot(a, b))
            except:
                print('Invalid dimensions')

        elif ch == 4:
            ch2 = int(input('Transpose of matrix(1) or matrix(2)? '))

            if ch2 == 1:
                print(np.transpose(a))
            else:
                print(np.transpose(b))

        elif ch == 5:
            ch2 = int(input('Determinant of matrix(1) or matrix(2)? '))

            try:
                if ch2 == 1:
                    print(np.linalg.det(a))
                else:
                    print(np.linalg.det(b))
            except:
                print('Invalid dimensions')

        elif ch == 6:
            ch2 = int(input('Inverse of matrix(1) or matrix(2)? '))

            try:
                if ch2 == 1:
                    print(np.linalg.inv(a))
                else:
                    print(np.linalg.inv(b))
            except:
                print('Invalid dimensions')

        elif ch == 7:
            return True

        else:
            print('Invalid Input! Try Again.')


def statistics():
    a = list(map(int, input('Enter space-seperated numbers: ').split()))
    print()
    print('''1. Mean
2. Mode
3. Median
4. Variance
5. Standard Deviation
6. Exit Statistical Calculations''')
    while True:
        print()
        ch = int(input('Enter your statistical operation: '))

        if ch == 1:
            print('Mean:', st.mean(a))

        elif ch == 2:
            print('Mode:', st.mode(a))

        elif ch == 3:
            print('Median:', st.median(a))

        elif ch == 4:
            print('Variance:', st.variance(a))

        elif ch == 5:
            print('Standard Deviation:', st.stdev(a))

        elif ch == 6:
            return True

        else:
            print('Invalid Input! Try Again.')


def polynomial():
    a = list(map(int, input('Enter space-seperated coefficients of the polynomial: ').split()))
    r = np.roots(a)
    for i in range(len(r)):
        print('x%d: %.2f' % (i + 1, r[i]))

    return True


def simul():
    l = ['x', 'y', 'z']
    n = int(input('Number of unknowns[1-3]?: '))
    if n > 3:
        return False
    print('Enter space-separated coefficients and solution of the')
    a1 = list(map(int, input('First equation: ').split()))
    b1 = list(map(int, input('Second equation: ').split()))
    if len(a1) != len(b1):
        print('Invalid number of values! Try again.')
        return False

    a = np.array([a1[:len(a1) - 1], b1[:len(b1) - 1]])
    b = np.array([a1[len(a1) - 1], b1[len(b1) - 1]])
    c = np.linalg.solve(a, b)
    for i in range(len(c)):
        print('%s: ' % (l[i]), end='')
        print(c[i])

    return True


def foot():
    for i in range(40):
        print('-', end='')
    print()
    print('|', 'Thank You!'.rjust(23), '|'.rjust(14))
    for i in range(40):
        print('-', end='')


def main():
    while True:
        print()
        head()
        print()
        ch = input('Enter your calculation choice: ')
        if ch == '1':
            while True:
                t = calculate()
                if t:
                    break

        elif ch == '2':
            while True:
                t = baseN()
                if t:
                    break

        elif ch == '3':
            while True:
                t = matrices()
                if t:
                    break

        elif ch == '4':
            while True:
                t = statistics()
                if t:
                    break

        elif ch == '5':
            while True:
                t = polynomial()
                if t:
                    break

        elif ch == '6':
            while True:
                t = simul()
                if t:
                    break

        elif ch == '7':
            foot()
            break

        else:
            print('Invalid Input! Try Again.')


# main
if __name__ == '__main__':
    main()
