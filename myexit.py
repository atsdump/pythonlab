#!/usr/bin/env python3
import sys
args = sys.argv

user_input = input("Please enter Y to quit and anything else to continue:")
if user_input.lower() == "y" or user_input.lower() == "yes":
  exit()
else:
  print("Continue") 

#user_nampy = input("What is your full name? ")
#print(user_nampy.split(" "))

user_nampy = args[1]
unl = user_nampy.split(" ")
#print(unl[0])
#print(unl[1])
#print(unl[2])

for nampy in unl:
  print(nampy)

for charcount in "Python Class":
  print(charcount)
