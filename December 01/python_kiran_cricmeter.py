# -*- coding: utf-8 -*-
"""python_kiran_cricmeter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z15xW2oRI3T_rRCzIzZgguBH7lg9WcUi
"""

n=int(input("Enter the no. of players in team:"))
get_list=input("Enter the scores of players separated by spaces:")
scores_list=get_list.split()
for i in range(n):
  scores_list[i]=int(scores_list[i])
sum_list=sum(scores_list)
print("Sum:",sum_list)
max_score=max(scores_list)
for i in range(n):
  if(scores_list[i]==max_score):
    print("Max score player number:",i)
    break

