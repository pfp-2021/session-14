# -*- coding: utf-8 -*-

#%%

import math

print(math.pi)

#%% Exercise 1

# import the utitities.py file, let's see what happens

import utilities

print(utilities.i)
print(utilities.name)

#%% sys.path

import sys

for dir in sys.path:
    print(dir)

#%% escaping
    
print("this is \"escaping\"")

#%% modifying sys.path. VERY BAD IDEA
    
import sys

# sys.path.append("/Users/pepe/Desktop")

sys.path = []

print(sys.path)

import utilities

#%% time

import time


while True:
    
    time.sleep(1)
    
    print("wake up everybody!")

#%%
    
from json import dumps

print(dumps([3,2,1]))















#%% Exercise 2

#1. use the module located in code/utils/data.py
#2. print the second element from the list

from code.utils.data import dictionary


print(dictionary)













