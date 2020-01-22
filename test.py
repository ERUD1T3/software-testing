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
            # print(f'domain {self.domain_set}')
            # setting up the domain_set structure to containt the pairs
            self.range_set = {i: [] for i in range(1, self.size + 1)}
            # print(f'range {self.range_set}')

            for line in f:
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

        print('Onto' if res else 'Not onto')

    def isOne2one(self):
        '''return true if the prog is one2one'''
        res = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1 or \
                    len(self.range_set[idx]) != 1:

                res = False
                break

        print('One to one' if res else 'Not one to one')

    def isReflexive(self):
        '''return true if the prog is reflexive'''

        res = True
        for idx in range(1, self.size+1):
            if len(self.domain_set[idx]) != 1 \
               or idx not in self.domain_set[idx]:
                    # check if the range has at least one element in
                    # and if the number itself is present in the range
                res = False
                break

        print('Reflexive' if res else 'Not reflexive')

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

        print('Symmetric' if res else 'Not symmetric')

    def dfsTrans(self,
                 visited, graph, src, dest,
                 min_nedges, max_nedges, n_edges=0):
        '''
            runs depth first search on adjacency list graph
            return true if there is transitivity
        '''
        if src == dest and \
                n_edges >= min_nedges and \
                n_edges < max_nedges:
                # if you reached destination and
                # the number of edge visited is within range
            return True

        if n_edges >= max_nedges:
            # return when going beyond assigned max_nedges
            return False

        if src not in visited:
            # print(src)
            visited.append(src)
            for nghbr in graph[src]:
                return self.dfsTrans(visited, graph, nghbr, dest,
                                     min_nedges, max_nedges, n_edges + 1)

        return False  # defaulting to False

    def isTransitive(self):
        '''return true if the prog is Transitive'''
        res = True
        idx = 1
        while res and idx <= self.size:
            for idy in self.domain_set[idx]:
                visited = []
                if not self.dfsTrans(visited, self.domain_set, idx, idy, 2, 3):
                    res = False
                    break
            idx += 1

        print('Transitive' if res else 'Not transitive')

    def isFunction(self, option=None):
        '''return true if the prog is a function'''

        res = True
        for idx in range(1, self.size + 1):
            if len(self.domain_set[idx]) != 1:
                # if one element in the input has more than or
                # less than one element in the output, it is not function
                res = False
                break

        print('Function ' if res else 'Not function', end='')

        if res == True and option == 'onto':
            self.isOnto()

        if res == True and option == 'one2one':
            self.isOne2one()

        print()
