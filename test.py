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

    def isReflexive(self):
        '''return true if the prog is reflexive'''

        fn_status = True
        for idx in range(1, self.size+1):
            if len(self.data[idx]) != 1 \
               or idx not in self.data[idx]:
                    # check if the range has at least one element in
                    # and if the number itself is present in the range
                fn_status = False
                break

        print('Reflexive' if fn_status else 'Not reflexive')

    def isSymmetric(self):
        '''return true if the prog is symmetric'''
        return True

    def isTransitive(self):
        '''return true if the prog is Transitive'''
        return True

    def isFunction(self):
        '''return true if the prog is a function'''
        fn_status = True
        for idx in range(1, self.size + 1):
            if len(self.data[idx]) != 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                fn_status = False
                break

        print('Function' if fn_status else 'Not function')
