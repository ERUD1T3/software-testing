#!/usr/bin/env python3

# test

from bisect import insort
import sys


class Test:
    '''Test class for prog unit testing'''

    def __init__(self):
        '''initializes a test object for a test program based on output file'''
        # self.filename = prog_output_file

        # with open(self.filename, 'r') as f:
        self.size = int(sys.stdin.readline())
        # reading the first line in as the total number of pairs
        # self.size = int(f.readline())

        # setting up the domain_set structure to containt the pairs
        self.domain_set = {i: [] for i in range(1, self.size + 1)}
        # print(f'domain {self.domain_set}')
        # setting up the domain_set structure to containt the pairs
        self.range_set = {i: [] for i in range(1, self.size + 1)}
        # print(f'range {self.range_set}')

        for line in sys.stdin.readlines():
            # looping through the file to store the domain_set
            i, o = line.split()

            i = int(i)
            o = int(o)
            # print(f'i = {i}, o = {o}')
            # insert the domain_set at the adequate position
            insort(self.domain_set[i], o)
            insort(self.range_set[o], i)

    def isOnto(self):
        '''return true if the prog is onto'''
        res = True
        for idx in range(1, self.size + 1):
            if len(self.range_set[idx]) < 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                res = False
                break

        return res
        # print('Onto' if res else 'Not onto')

    def isOne2one(self):
        '''return true if the prog is one2one'''
        res = True
        d_count = 0  # count of 1's in domain set
        r_count = 0  # count of 1's in range set

        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) > 1 or \
                    len(self.range_set[idx]) > 1:
                res = False
                break

            if len(self.domain_set[idx]) == 1:
                d_count += 1
            if len(self.range_set[idx]) == 1:
                r_count += 1

        if d_count != r_count:
            res = False

        return res
        # print('One to one' if res else 'Not one to one')

    def isReflexive(self):
        '''return true if the prog is reflexive'''

        res = True
        for idx in range(1, self.size+1):
            if idx not in self.domain_set[idx]:
                    # check if the range has at least one element in
                    # and if the number itself is present in the range
                res = False
                break

        return res
        # print('Reflexive' if res else 'Not reflexive')

    def isSymmetric(self):
        '''return true if the prog is symmetric'''
        res = True
        idx = 1  # iteritor through dict keys
        while res and idx <= self.size:
            # while result is not false and index is less than size
            if len(self.domain_set[idx]) != len(self.range_set[idx]):
                # mismatch in set length, no sym
                res = False
                break
            else:
                for d_el, r_el in zip(self.domain_set[idx], self.range_set[idx]):
                    if d_el != r_el:
                        # mismatch in set element, no sym
                        res = False
                        break
                idx += 1
        return res
        # print('Symmetric' if res else 'Not symmetric')

    def isFunction(self):
        '''return true if the prog is a function'''

        res = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                res = False
                break

        return res
        # print('Function ' if res else 'Not function', end='')

    def isTransitive(self):
        '''return true if the prog is transitive '''

        for idx in range(1, self.size + 1):
            for idy in self.domain_set[idx]:
                for idz in self.domain_set[idy]:
                    if idz not in self.domain_set[idx]:
                        return False

        return True


def main():
    # prog_test = Test(sys.argv[1])

    # receive input from pipeing stdin
    prog_test = Test()

    print('Running tests...')

    prog_test.isOnto()
    print('Onto ' if prog_test.isOnto() else 'Not onto')
    print('One to one ' if prog_test.isOne2one() else 'Not one to one')
    print('Reflexive ' if prog_test.isReflexive() else 'Not reflexive')
    print('Symmetric ' if prog_test.isSymmetric() else 'Not symmetric')

    print('Function ' if prog_test.isFunction() else 'Not function')
    print('Onto function ' if prog_test.isFunction()
          and prog_test.isOnto() else 'Not onto function')
    print('One to one Function ' if prog_test.isFunction()
          and prog_test.isOne2one() else 'Not one to one function')

    print('Function ' if prog_test.isTransitive() else 'Not function')

    print('Test complete!')


if __name__ == "__main__":

    try:
        main()
    except:
        print('Error in Prog stdout')
    # print(sys.argv)
