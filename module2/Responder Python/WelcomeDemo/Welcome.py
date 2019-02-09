# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:47:06 2019

@author: Deepika
"""

# Initialization of variables
fname = lname = wel_msg = gen = mpname = wa_msg=''

#Initializing welcome message
wel_msg = "Good Morning !!! Welcome to the Varun Academy \n"
print(wel_msg)

# inputing user information

fname = input("May I know your first name please?\n")
lname = input("May I know your last name please?\n")
gen = input("May I know your Gender Please\n")

if gen== "MALE" or gen == "male" :
    
   
    mpname = input("May I know the name of the person whom you want to meet ?\n")
    wa_msg = '''Mr.{} is in meeting , Mr. {} {} please wait for the 5 minutes
    and enjoy the cup of cofee \n'''.format(mpname,fname,lname)
    print(wa_msg)
     
    
elif gen == "FEMALE" or gen == "female":
    
    
    mpname = input("May I know the name of the person whom you want to meet ?\n")
    wa_msg = '''Mr.{} is in meeting , Mr. {} {} please wait for the 5 minutes
    and enjoy the cup of cofee \n'''.format(mpname,fname,lname)
    print(wa_msg)
    
    
elif gen == '' :
    
    
    print("please enter gender details")
    
    
else :
    
    print("please enter the valid gender")