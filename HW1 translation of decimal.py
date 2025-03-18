# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:16:19 2025

@author: coco5
"""

def openingmessage():
    print("Entering the number between 0 ~ 255")
    print("You can get binery and hexadecimal based on the number you enter.\n")

def continuemessage():
    print("Press any key to continue")
    print("Press '1' to exit")
    enter = input("Continue or exit? \n")
    return enter
    
def decimal(number):
    print("Decimal = ", end="")
    print(number)

def binary(number, L=2):
    binarynumber = []
    if number == 0:
        j = 0
        binarynumber.append(str(j))
    else:  
        while number > 0:
            j = number % L
            binarynumber.append(str(j))
            number = number // L
        binarynumber.reverse()
    print("Binary = ", end="")    
    print("".join(binarynumber),)
        
def hexadecimal (number:int, K=16 ):
    hexadecimalnumber = []  
    if number == 0:
        j = 0
        hexadecimalnumber.append(str(j))
    else:  
        while number > 0:
            j = number % K
            number = number // K
            if j >= 10:
                j = chr(j+55)
            hexadecimalnumber.append(str(j))
        hexadecimalnumber.reverse()
    print("Hexadecimal = ",end="")
    print("".join(hexadecimalnumber),"\n")

def main():
    while True:
        openingmessage()
        try:
            number = int(input("Please enter the number between 0 ~ 255: "))
            if number >= 0 and number <= 255 :
                decimal(number)
                binary(number)
                hexadecimal(number)
                enter = continuemessage()
                if enter == "1":
                    break
                else:
                    continue
            else:
                print("Please enter the number in correct range 0 ~ 255 \n ")
        
        except ValueError:
            print("Please enter only number")
            print("Try again \n")
            continue

if __name__== "__main__" :
    main()
