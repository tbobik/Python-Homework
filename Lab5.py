#################################################################
# CS 21A Programming in Python Lab #5
#
# Constants, functions, if statements, print statements,
# for loop, lists.
# If Elif statements.
# Output the middle character, number of vowels, reverse order,
# and if the string is a palindrome or not, using functions.
#################################################################
# Defining functions to use in main

def middle(string):
    middleLetter = ""
    MIDDLELOC = int(len(string) / 2)
    if len(string) % 2 == 0 : 
        middleLetter = string[MIDDLELOC - 1] + string[MIDDLELOC]
    else:
        middleLetter = string[MIDDLELOC]

    return middleLetter

def reverse(string):
    reverseOrder = ""
    for i in range(len(string), 0, -1) :
        reverseOrder += string[i - 1]

    return reverseOrder

def countVowels(string):
    vowelCount = 0
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for i in range(len(string)) :
        if string[i] in vowels :
            vowelCount += 1
    return vowelCount

def isPalindrome(string):
    if len(string) == 0 or len(string) == 1 :
        return "That's a palindrome."
    elif string[0] != string[len(string)-1] :
        return "That's not a palindrome."
    else :
        return isPalindrome(string[1:len(string)-1])

# Main that loops through list of words, and prints out each defined function. 
def main():
    testcases = ['racecar', 'apple', 'civic', 'bottle', 'noon']
    for word in testcases :
        print("Enter a string:", word)
        print("The middle character(s) is/are:", middle(word))
        print("The string reversed is:", reverse(word))
        print("The string contains %d vowels." % countVowels(word))
        print(isPalindrome(word))
      

main()
   
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Enter a string: racecar
# The middle character(s) is/are: e
# The string reversed is: racecar
# The string contains 3 vowels.
# That's a palindrome.
# Enter a string: apple
# The middle character(s) is/are: p
# The string reversed is: elppa
# The string contains 2 vowels.
# That's not a palindrome.
# Enter a string: civic
# The middle character(s) is/are: v
# The string reversed is: civic
# The string contains 2 vowels.
# That's a palindrome.
# Enter a string: bottle
# The middle character(s) is/are: tt
# The string reversed is: elttob
# The string contains 2 vowels.
# That's not a palindrome.
# Enter a string: noon
# The middle character(s) is/are: oo
# The string reversed is: noon
# The string contains 2 vowels.
# That's a palindrome.
##################################################################
