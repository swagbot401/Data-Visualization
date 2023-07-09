import math
import random
import datetime
import pandas as pd
import numpy as np
import json

# https://www.kaggle.com/datasets/nathanlauga/nba-games 
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

print("Get Diffed")

arr = 0b0001_0000
print(f"{arr} in binary is {bin(arr)}")

def print_args(*args):
    for arg in args: 
        print(arg)

print_args(5)
