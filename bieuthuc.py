# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:10:33 2024

@author: Phạm Tuyết Nhung-23707091
"""
import math 
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
A= ((math.sqrt(a)) - (math.sqrt(b)))/ (math.pow(a, 0.25)) - (math.pow(b, 0.25))
B=((math.sqrt(a) + math.pow((a*b), 0.25))/ (math.pow(a, 0.25)) + math.pow(b, 0.25))
print("Kết quả biểu thức là:", A - B  )
