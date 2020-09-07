#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Name:        Word_Game
# Purpose:     Simple Gaming
#
# Author:      Ranjith A V
#
# Created:     07/09/2020
#-------------------------------------------------------------------------------

import random
Mylist = ['apple', 'mango', 'orange', 'pineapple', 'banana', 'grapes']
random.shuffle(Mylist)
sampleStr = Mylist[0]
char_list = list(sampleStr)
random.shuffle(char_list)
finalStr = ''.join(char_list)
uservalue = str( input("I have shuffled the letters of one Fruit to \"" + finalStr + "\".  Can you find Fruit name ?  You have total 5 attempts:  " ))
count = 1
while uservalue != sampleStr:
       uservalue = input("Sorry Wrong answer! Please try again :  ")
       if count <= 3:
            count = count + 1
       else:
            print("Maximum attempt completed, Corrrect answer is", sampleStr)
            break;

if uservalue == sampleStr:
    print("Superb, you found the word:", sampleStr)
