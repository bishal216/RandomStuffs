# -*- coding: utf-8 -*-
"""Simulation labs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vF1Z29ElMGYl_nRH-82wihajD9W6Cv_A
"""

import matplotlib.pyplot as plt
import numpy as np
from math import log

# Variables
a = 17
b = 23
P = 256
r=[17] #seed
N = 100

for i in range (1,N-1):
    r.append((r[i-1]*a+b) % P)

x = [ i for i in range(len(r))]
fig = plt.figure()
plt.plot(r)
plt.scatter(x,r)
plt.show()

n = 8
Ei = N/n
Oi = [0] * n
h = P/n 
x2=0
for i in range(0,N-1):
    j = int(r[i]/h)
    Oi[j]= Oi[j]+1

x2 = 0
for item in Oi:
    x2 = x2 + (pow(item - Ei,2))/Ei
print(x2)