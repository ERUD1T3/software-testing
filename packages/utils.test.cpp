// utility functions for the test class

#include "test.hpp"
#include "iostream"

using namespace std;

Test::Test(string &prog_name)
{
    /* Constructor for a test object for one file 
        loads data from file into test object
    */
    data = new list<unsigned int>[num_io_pairs];
}

unsigned int Test::getNumPairs() const
{
    /*return number of input output pairs from prog*/
    return this->num_io_pairs;
}

string Test::getProgName() const
{
    /* return the command run by program to construct test object */
    cout << this->prog_name << endl;
    return this->prog_name;
}