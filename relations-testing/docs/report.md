# software-testing
repo for all code testing 2 class related


## example of command to run

> $./filename **args > output.txt && python main.py output.txt


decimals are truncated

func: 0 to 2 args
    no args = random output with random large range

    1 args
    char input and 0 = prog return 0
    positive value = range of values from 1 to that value
        left numbers are in order
    negative values = prog return the negative value

    2 args
    second args insures a constant output (second arg could be anything)

    more than 2 args, does nothing


    Function

    function for certain combinations of arguments


one2one: 0 to 2 args

    no args = random output with random large range

    1 args
    char inputs and 0 = floating point execption
    positive value = range of values from 1 to that in specific order but with variable number of length
    negative value = range of values from 1 to abs(that)

    2 args
    second args insures a constant output (second arg could be anything)

    more than 2 args, does nothing

    one to one for certain combinations of arguments

onto: 0 to 2 args
    no args = random output with random large range

    1 args
    char inputs and 0 = prog return 0
    positive value = range of values from 1 to that in random order
    negative value = prog retun the negative value

    2 args
    second args insures a constant output (second arg could be anything)

    more than 2 args, does nothing

    onto for certain combinations of arguments


reflex: 0 to 3 args
    no args = random output with random large range

    1 args
    char inputs and 0 = prog return 0
    positive value = range of values from 1 to that in constant order with constant lines
    negative value = prog retun the negative value

    2 args
    char input, zero, or negative = prog return args 1
    positive value = determines the number of lines on the output but in random order


    3 args 
    third args insures a constant output (second arg could be anything)


    more than 3 args, does nothing

    reflexive for certain combinations of arguments




