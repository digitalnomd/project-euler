import sys
from functools import reduce


def problem1():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def problem2():
    return fibo_even_sum(4000000)

def fibo_even_sum(n):

    fib1 = 1
    fib2 = 2
    sum = 0

    while(fib2 < n):
        if fib2 % 2 == 0:
            sum += fib2

        temp = fib2
        fib2 += fib1
        fib1 = temp

    return sum

def problem6():
    """ Difference between the square of sum and sum of squares
        of the first 100 natural numbers """
    return square_of_sums(101) - sum_of_squares_lambda(101)

def problem18(triangle, height):
    return dp_triangle(triangle, height, 0, 0, dict())

def dp_triangle(triangle, height, row, col, maxs):
    if row == height - 1:
        return int(triangle[row][col])

    keyLeft = str(row + 1) + "," + str(col)
    keyRight = str(row + 1) + "," + str(col + 1)

    if keyLeft in maxs:
        maxLeft = maxs[keyLeft]
    else:
        maxLeft = dp_triangle(triangle, height, row + 1, col, maxs)
        maxs[keyLeft] = maxLeft

    if keyRight in maxs:
        maxRight = maxs[keyRight]
    else:
        maxRight = dp_triangle(triangle, height, row + 1, col + 1, maxs)
        maxs[keyRight] = maxRight

    return max(maxLeft, maxRight) + int(triangle[row][col])

def square_of_sums(n):
    return reduce(lambda x, y: x + y, range(1, n)) ** 2

def sum_of_squares(n):
    return sum(x ** 2 for x in range(1, n))

def sum_of_squares_lambda(n):
    return reduce(lambda x, y: x + y**2, range(1, n))


def main(argv):
    with open(argv[1], 'r') as f:
        triangle = f.readlines()

    height = len(triangle)

    triangle = [x.strip().split() for x in triangle]

    print(problem18(triangle, height))


if __name__ == '__main__':
    main(sys.argv)
