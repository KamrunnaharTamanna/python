# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JapbRxI2yfU8O8hYCgVWd5cu4-8qwL-Y
"""

def calculator():
  print("select operaton")
  print("Addition")
  print("Subtract")
  print("Multiply")
  print("Divider")

choice= input("enter choice(1/2/3/4)")
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
if choice== '1':
  print(f"the result is :{num1+num2}")
elif choice== '2':
  print(f"the result is:{num1-num2}")
elif choice== '3':
  print(f"the result is:{num1*num2}")
elif choice== '4':
  print(f"the result is:{num1/num2}")
else :
  print("invald result")