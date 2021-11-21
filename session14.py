# -*- coding: utf-8 -*-

#%%

import math

print(math.pi)

#%% 

import utilities

print(utilities.i)
print(utilities.name)
print(utilities.add(5, 6))

# %%

import sys

for entry in sys.path:
    print(entry)




# %%

# import time

# while True:
#     time.sleep(0.3)
#     print("hello")

#%%

import math

print(math.ceil(4.4))
print(math.floor(4.4))

# %%

from math import ceil, floor, pi

print(ceil(pi))
print(floor(pi))

# %%

from math import *

print(sqrt(8))

#%%

import math

print(math.sqrt(3))

# %%

import math as potato

print(potato.sqrt(potato.pi))

# %%
# code/
#   __init__.py
#   utils/
#     __init__.py
#     data.py

from code.utils import data

print(data.dictionary)
# %%
