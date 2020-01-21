# main file for unit testing

from test import Test
import sys


def main():
    prog_test = Test(sys.argv[1])

    print('Running tests...')

    prog_test.isOnto()
    prog_test.isOne2one()
    prog_test.isReflexive()
    prog_test.isSymmetric()
    prog_test.isTransitive()
    prog_test.isFunction()

    print('Test complete!')


if __name__ == "__main__":
    main()
    # print(sys.argv)
