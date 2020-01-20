# test

from bisect import insort


class Test:
    '''Test class for prog unit testing'''

    def __init__(self, prog_output_file):
        '''initializes a test object for a test program based on output file'''
        self.filename = prog_output_file

        with open(self.filename, 'r') as f:
            # reading the first line in as the total number of pairs
            self.size = int(f.readline())

            # setting up the domain_set structure to containt the pairs
            self.domain_set = {i: [] for i in range(1, self.size + 1)}

            # setting up the domain_set structure to containt the pairs
            self.range_set = {i: [] for i in range(1, self.size + 1)}

            for line in f:
                # looping through the file to store the domain_set
                i, o = line.split()
                # insert the domain_set at the adequate position
                insort(self.domain_set[i], o)
                insort(self.range_set[o], i)

    def isOnto(self):
        '''return true if the prog is onto'''
        fn_status = True
        for idx in range(1, self.size + 1):
            if len(self.range_set[idx]) < 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                fn_status = False
                break

        print('Onto' if fn_status else 'Not onto')

    def isOne2one(self):
        '''return true if the prog is one2one'''
        fn_status = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1 or \
                    len(self.range_set[idx]) != 1:

                fn_status = False
                break

        print('One to one' if fn_status else 'Not one to one')

    def isReflexive(self):
        '''return true if the prog is reflexive'''

        fn_status = True
        for idx in range(1, self.size+1):
            if len(self.domain_set[idx]) != 1 \
               or idx not in self.domain_set[idx]:
                    # check if the range has at least one element in
                    # and if the number itself is present in the range
                fn_status = False
                break

        print('Reflexive' if fn_status else 'Not reflexive')

    def isSymmetric(self):
        '''return true if the prog is symmetric'''
        fn_status = True
        idx = 1  # iteritor through dict keys
        while fn_status and idx <= self.size:
            if len(self.domain_set[idx]) != len(self.range_set[idx]):
                # mismatch in set length, no sym
                fn_status = False
                break
            else:
                for d_el, r_el in zip(self.domain_set[idx], self.range_set[idx]):
                    if d_el != r_el:
                        # mismatch in set element, no sym
                        fn_status = False
                        break
                idx += 1

        print('Symmetric' if fn_status else 'Not symmetric')

    def isTransitive(self):
        '''return true if the prog is Transitive'''
        return True

    def isFunction(self):
        '''return true if the prog is a function'''
        fn_status = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                fn_status = False
                break

        print('Function' if fn_status else 'Not function')
