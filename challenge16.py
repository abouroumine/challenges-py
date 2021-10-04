import math
import os
import random
import re
import sys

if __name__ == '__main__':
    S = input()
    try:
        l = int(S)
        print(l)
    except ValueError as v:
        print("Bad String")
    else:
        print(l)
