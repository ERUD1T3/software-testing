#!/usr/bin/env python3

# main file for unit testing

from test import Test


def main():
    # prog_test = Test(sys.argv[1])
    prog_test = Test()

    print('Running tests...')

    prog_test.isOnto()
    prog_test.isOne2one()
    prog_test.isReflexive()
    prog_test.isSymmetric()
    prog_test.isTransitive()
    prog_test.isFunction()
    prog_test.isFunction('onto')
    prog_test.isFunction('one2one')

    print('Test complete!')


if __name__ == "__main__":
    main()
    # print(sys.argv)
