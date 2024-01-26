#  Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# Pseudocode

number = 789056
print("The given number is:", number)

# Loop until the number becomes 0
while number > 0:
    # Get the last digit
    digit = number % 10
    
    # Remove the last digit and repeat the loop
    number = number // 10
    
    # Print the digit with a space (end=" ") to display them on the same line
    print(digit, end=" ")
