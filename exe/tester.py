#!/usr/bin/env python3

# test
'''
    Program to test for relation properties:
    one to one, onto, reflexive, symmetric, function,
    transitive
    Authored by Josias Moukpe
'''

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

    def __repr__(self):
        '''display the test data structures'''
        print(f'\tDomain \t\tRange')
        # for dom, ran in zip(self.domain_set, self.range_set):
        #     print(f'{dom}{ran}')
        for i in range(1, self.size + 1):
            print(
                f'{i}: \t{self.domain_set[i]} | \t{self.range_set[i]}')
        return str(self.size)

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

    def printEqv(self):
        # keep track of the already printed
        printed = {idx: False for idx in range(1, self.size + 1)}
        counter = 0
        was_partition = False
        to_print = True

        for idx in range(1, self.size + 1):
            for idy in self.domain_set[idx]:
                if not printed[idy]:
                    printed[idy] = True
                    was_partition = True
                    if to_print:
                        print(idy, end=' ')

            if was_partition:
                if to_print:
                    print()
                counter += 1
                was_partition = False

            if counter > 10:
                to_print = False

        if not to_print:
            print('...')
        print(f'\ntotal of {counter} partitions!')


def main():
    # prog_test = Test(sys.argv[1])

    # receive input from pipeing stdin
    prog_test = Test()

    # print(f'data received:\n{prog_test}')

    print('Running tests...\n')

    eq_checks = 0
    is_onto = False
    is_one2one = False

    if prog_test.isOnto():
        print('Onto')
        is_onto = True
    else:
        print('Not onto')

    if prog_test.isOne2one():
        print('One to one ')
        is_one2one = True
    else:
        print('Not one to one')

    if prog_test.isReflexive():
        print('Reflexive ')
        eq_checks += 1
    else:
        print('Not reflexive')

    if prog_test.isSymmetric():
        print('Symmetric ')
        eq_checks += 1
    else:
        print('Not symmetric')

    if prog_test.isTransitive():
        eq_checks += 1
        print('Transitive ')
    else:
        print('Not transitive')

    if prog_test.isFunction():
        print('Function')
        print('Onto function ' if is_onto else 'Not onto function')
        print('One to one function ' if is_one2one else 'Not one to one function')
    else:
        print('Not function')

    if eq_checks == 3:
        print('Equivalence relation')
        print('Partitions:')
        prog_test.printEqv()

    else:
        print('Not equivalence relation')

    print('\nTest complete!')


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(f'Error:{e} in Prog stdout')
    # print(sys.argv)
