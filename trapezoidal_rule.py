#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:25:19 2023

@author: sudipto3331
"""

def fnc(x):
 return ((x*x))

a = float(input("Enter lower limit:"))
b = float(input("Enter upper limit:"))
n = int(input("Enter the number of N:"))

area = 0
a_i = a
diff = ((b-a)/n)

for i in range (1, n+1):
    b_i = a_i+((diff)*i)
    h = ((b_i-a))
    area = area + (h*((fnc(a)+fnc(b_i))/2))
    a = b_i


print(area)
