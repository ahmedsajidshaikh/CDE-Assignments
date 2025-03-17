# 1 Program to count the number of vowels in a string

# # Accept input from the user
# user_input = input("Enter a string: ")

# # Convert the string to lowercase to simplify checking
# vowels = "a","e","i","o","u"
# # Initialize a counter for vowels
# count = 0
# # Loop through each character in the string
# for char in user_input:
#     # Check if the character is a vowel
#     if char in vowels:
#         # If it is, increment the counter
#         count += 1
# print(count)

# 2 Program that accept sting from user. your program should create and display a new sting where the first and last character have been changed.
# Accept input from the user
user_input = input("Enter a string: ")
# Check if the string has at least two characters
if len(user_input) > 1:
    # Swap the first and last characters
    user_input = user_input[-1] + user_input[1:-1]
    0
    print(user_input)
    
    