"""Write a program to check for palindrome"""

userInput = input("Enter any word: ")
word = userInput[::-1]
if word == userInput:
    print("Its is palindrome")
else:
    print("It is not palindrome")