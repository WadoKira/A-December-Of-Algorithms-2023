# -*- coding: utf-8 -*-
"""python_kiran_babyblocks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BsofeH2TD6fsWw1GSaYJ38RLUo_ZWsuQ
"""

import math
def rectangleincirlce(value_list):
  diagonal_square=(value_list[0]**2)+(value_list[1]**2)
  diagonal=math.sqrt(diagonal_square)
  diameter=2*value_list[2]
  if(diagonal<=diameter):
    return True
  else:
    return False
string_list=input("Enter the width,height of the rectangle and then enter the radius of the circle:")
value_list=string_list.split()
for i in range(len(value_list)):
  value_list[i]=int(value_list[i])
if rectangleincirlce(value_list):
  print("True")
else:
  print("False")

