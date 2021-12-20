# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:25:41 2021

@author: SELAB
"""

def Encryption(text,shift):
    Result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            Result = Result+ chr((ord(char) + shift-65) % 26 + 65)
 
        else:
            Result= Result+ chr((ord(char) + shift - 97) % 26 + 97)
 
    return Result
##################################################################### 
text = input("Enter the text::::::::")

shift=int(input("Enter the number of shift:::"))

print ("Text of the cypher is : " + text)

print ("Shift of the cypher is : " + str(shift))

print ("Cipher is: " + Encryption(text,shift))





###########################################################################


def decryption(text,shift):
    Result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            Result = Result+ chr((ord(char) - shift-65) % 26 + 65)
 
        else:
            Result= Result+ chr((ord(char) - shift - 97) % 26 + 97)
 
    return Result
##################################################################### 
text = input("Enter the text::::::::")

shift=int(input("Enter the number of shift:::"))

print ("Text of the cypher is : " + text)

print ("Shift of the cypher is : " + str(shift))

print ("Cipher is: " + decryption(text,shift))