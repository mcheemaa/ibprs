# Improved Break Point Reversal Sort

It is an approximation algorithm with a performance guarantee of at most 4.

The program takes an input of a text file which contains a list of permuted numbers (each number represents a gene number ) and sorts the
numbers by reducing the number of breakpoints based on decreasing strips. The program outputs each step of sorting, including the number of breakpoints for the permutation of each step. It also outputs the reversal distance (i.e., the number of reversals) to the identity permutation. 

The program should be run as the following:

    $ python ibprs.py inputFile outputFile
