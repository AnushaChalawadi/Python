#!/bin/python3

import math
import os
import random
import re
import sys

#testcase 0 : if n is 3 and its ODD
#testcase 1 : if n is 24 (n>20) and its EVEN

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:              
        print("Weird")
    elif n>=2 and n<=5:
        print("Not Wierd")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
