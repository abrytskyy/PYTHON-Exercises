string = input("Enter a word:")
if string == string[::-1]:
    print (string, " is a palindrome")
else:
    print("It's not a palindrome")