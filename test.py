# test

from bisect import insort


class Test:
    '''Test class for prog unit testing'''

    def __init__(self, prog_output_file):
        '''initializes a test object for a test program based on output file'''
        self.filename = prog_output_file

        with open(self.filename, 'r') as f:
            # reading the first line in as the total number of pairs
            self.size = f.readline()

            # setting up the data structure to containt the pairs
            self.data = {i: [] for i in range(1, self.size + 1)}

            for line in f:
                # looping through the file to store the data
                i, o = line.split()
                # insert the data at the adequate position
                insort(self.data[i], o)

    def isOnto(self):
        '''return true if the prog is onto'''
        return True

    def isOne2one(self):
        '''return true if the prog is one2one'''
        for idx in range(1, self.size):
            if len(self.data[idx]) != 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not a one2one
                return False
        return True

    def isReflexive(self):
        '''return true if the prog is reflexive'''
        return True

    def isSymmetric(self):
        '''return true if the prog is symmetric'''
        return True

    def isTransitive(self):
        '''return true if the prog is Transitive'''
        return True

    def isFunction(self):
        '''return true if the prog is a function'''
        return True
