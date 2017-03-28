#!/usr/bin/python

import sys

def main():
    m = int(sys.argv[1])
    x = int(sys.argv[2])
    print("s^" + sys.argv[1] + "(" + sys.argv[2] + ") =" , str(successor(m,x)))

    print("multiplication?",successor(m*2,x))

def successor(m, x):
    if m == 0:
        return x
    else:
        return successor(m-1,x+1)
main()
