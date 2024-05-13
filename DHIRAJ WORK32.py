#------------AUTHOR DHIRAJ----------#

#-------------FUCK CALCULATOR ------------#
import random
import os
def add (x,y):
	return x+y
logo = ('''
   ___   _   _    ___ _   _ _      _ _____ ___ 
  / __| /_\ | |  / __| | | | |    /_\_   _| __|
 | (__ / _ \| |_| (__| |_| | |__ / _ \| | | _| 
  \___/_/ \_\____\___|\___/|____/_/ \_\_| |___|
''')
print(logo)
	
#------------SUBTRACT--------------#
def sub(x,y):
	return x-y
	
print("CHOOSE WHICH YOU WANT")
print("1.ADD")
print("2.SUBTRACT")

choice = input ("ENTER CHOICE (1/2): ")

num1 = int(input("ENTER FIRST NUMBER:"))
num2 = int(input("ENTER SECOND NUMBER:"))
if choice == '1':
    print("Result: ", add(num1, num2,))
elif choice == '2':
    print("Result: ", subtract(num1, num2))