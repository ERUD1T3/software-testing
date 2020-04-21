#!/usr/bin/env python3

# test
'''
    Program to test for relation properties:
    one to one, onto, reflexive, symmetric, function,
    transitive, and equivalence
    Authored by Josias Moukpe
'''

from bisect import insort
import sys


class Test:
    '''Test class for prog unit testing'''

    def __init__(self, no_std_in=False):
        '''initializes a test object for a test program based on stdin data'''

        # with open(self.filename, 'r') as f:

        # print(f'line read: {sys.stdin.readline()}')

        self.size = 0 if no_std_in else int(sys.stdin.readline())

        # reading the first line in as the total number of pairs
        # self.size = int(f.readline())

        # setting up the domain_set structure to containt the pairs
        self.domain_set = {i: [] for i in range(1, self.size + 1)}
        # print(f'domain {self.domain_set}')
        # setting up the domain_set structure to containt the pairs
        self.range_set = {i: [] for i in range(1, self.size + 1)}
        # print(f'range {self.range_set}')

        for line in sys.stdin.readlines():
            # looping through the file to store the domain_set and range_set
            i, o = line.split()

            # print(f'i = {i}, o = {o}')
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
        '''return true if the prog is onto, false otherwise'''
        res = True
        for idx in range(1, self.size + 1):
            if len(self.range_set[idx]) < 1:
                # if one element in range has less than one
                # antecedent in domain then it is not onto
                res = False
                break

        return res
        # print('Onto' if res else 'Not onto')

    def isOne2one(self):
        '''return true if the prog is one2one, false otherwise'''
        res = True
        d_count = 0  # count of 1's in domain set
        r_count = 0  # count of 1's in range set

        for idx in range(1, self.size + 1):
            # if either an element in the set or domain has than
            # one pair associated, it is not one 2 one
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
        '''return true if the prog is reflexive, false otherwise'''

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
        '''return true if the prog is symmetric, false otherwise'''
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
        '''return true if the prog is a function, false otherwise'''

        res = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1:
                # if one element in the domain has more than or
                # less than one element in the range, it is not function
                res = False
                break

        return res
        # print('Function ' if res else 'Not function', end='')

    def isTransitive(self):
        '''return true if the prog is transitive, false otherwise'''
        # go through all numbers idx in set
        for idx in range(1, self.size + 1):
            # go through all idy numbers forming a pair with idx
            for idy in self.domain_set[idx]:
                 # go through all idz numbers forming a pair with idy
                for idz in self.domain_set[idy]:
                    # check if idz also forms a pair with idx
                    if idz not in self.domain_set[idx]:
                        return False

        return True

    def printEqv(self):
        '''Prints equivalence classes partitions'''
        # keep track of the already printed classes
        printed = {idx: False for idx in range(1, self.size + 1)}
        # tracks the number of printed partitions (no more than 10 )
        counter = 0
        # tracks if a list of number is a partition that hasn't yet been printed
        was_partition = False
        to_print = False  # tracks if remaining partitions should be printed

        for idx in range(1, self.size + 1):
            for idy in self.domain_set[idx]:
                if not printed[idy]:
                    printed[idy] = True
                    was_partition = True
                    if to_print:
                        print(idy, end=' ')

            if was_partition:
                if to_print:
                    print()  # adds new line after a single partition is printed
                counter += 1
                was_partition = False

            if counter > 10:
                # shouldn't print partitions anymore
                to_print = False

        if not to_print:
            # print('...')
            pass

            # prints the total number of partitions
        print(f'\n {counter} classes')


def main(no_std_in=False):

    # receive input from pipeing stdin
    # constructor load data into prog_test test object
    prog_test = Test(no_std_in)

    # print(f'data received:\n{prog_test}')  #prints the data stored for test

    # print('Running tests...\n')
    # print('\n---Start of Test Program---')

    eq_checks = 0  # tracks equivalence checks (3 needed for equivalence)
    is_onto = False  # tracks if onto
    is_one2one = False  # tracks if one to one

    if prog_test.isOnto():
        print('\nIs onto\n', end='')
        is_onto = True
    else:
        print('\nIs not onto\n', end='')

    if prog_test.isOne2one():
        print('Is one to one ')
        is_one2one = True
    else:
        print('Is not one to one')

    if prog_test.isReflexive():
        print('Is reflexive ')
        eq_checks += 1  # eq_checks = 1
    else:
        print('Is not reflexive')

    if prog_test.isSymmetric():
        print('Is symmetric ')
        eq_checks += 1  # eq_checks = 2
    else:
        print('Is not symmetric')

    if prog_test.isTransitive():
        eq_checks += 1  # eq_checks = 3
        print('Is transitive ')
    else:
        print('Is not transitive')

    if prog_test.isFunction():
        print('Is function')
        # print('Is onto function ' if is_onto else 'Is not onto function')
        # print('One to one function ' if is_one2one else 'Not one to one function')
    else:
        print('Is not function')

    if eq_checks == 3:
        print('Is equivalence relation')
        # print('Partitions:')
        prog_test.printEqv()

    else:
        print('Is not equivalence relation')

    # print('\nTest complete!')
    # print('---End of Test---')


if __name__ == "__main__":

    try:
        # run the main function
        main()

    except ValueError as v:
        main(True)

    except Exception as e:
        print(f'\n--{e}: Error in receiving stdin input--\n')
    # print(sys.argv)
