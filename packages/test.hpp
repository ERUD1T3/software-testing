// unit testing class

#ifndef TEST_HPP
#define TEST_HPP

#include <string>
#include <list>

using namespace std;

class Test
{
private:
    /* data */
    string prog_name;          //prgram name, containing the full path if it is in other directory
    unsigned int num_io_pairs; //number of input-output pairs from the data set
    list<unsigned int> *data;

public:
    Test(string &prog_name); //load a program into a test object

    unsigned int getNumPairs() const; // return the number of pairs in prog output
    string getProgName() const;       // return the prog command run for the object

    bool isOnto() const;       // return true if prog is onto
    bool isOne2One() const;    // return true if prog is one2one
    bool isReflexive() const;  // return true if prog is reflexive
    bool isSymmetric() const;  // return true if prog is symmetric
    bool isTransitive() const; // return true if prog is transitive
    bool isFunction() const;   // return true if prog is function
    // Test();
};

#endif
