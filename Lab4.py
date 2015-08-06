#################################################################
# CS 21A Programming in Python Lab #4
#
# Constants, Input, while loop, if statements, Print statements,
# for loop.
# If Elif statements.
# Reveieve user password input, check to see the if they are
# the same, greater than 8 characters, contain at least
# 1 upper and 1 lower case character, and 1 at least digit. 
# 
#################################################################
# Initialize constant variable and boolean variables.
NUM_CHARACTERS = 8
valid = False
upper = False
lower = False 
digits = False

# Read users password and check if they are valid.
while (not valid) :
    PASSWORD_1 = input("Enter your password: ")
    PASSWORD_2 = input("Re-enter your password: ")
    if PASSWORD_1 == PASSWORD_2 and len(PASSWORD_2) >= NUM_CHARACTERS :
        for letter in PASSWORD_2 :
            if letter.islower() :
                lower = True
            if letter.isupper() :
                upper = True
            if letter.isnumeric():
                digits = True
    if upper == True and lower == True and digits == True:
        valid = True
        print ("That pair of passwords will work.")
    else:
        print ("That password didn't have the required properties.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Enter your password: hello
# Re-enter your password: hello    
# That password didn't have the required properties.
# Enter your password: hello1234
# Re-enter your password: hello1234
# That password didn't have the required properties.
# Enter your password: HELLO1234
# Re-enter your password: HELLO1234
# That password didn't have the required properties.
# Enter your password: helooooooH
# Re-enter your password: helooooooH
# That password didn't have the required properties.
# Enter your password: HeLLO1234
# Re-enter your password: HeLLO1234
# That pair of passwords will work.
##################################################################
