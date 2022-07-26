# Finding Positive number from the list

# Taking input from user
User_list = list(map(int, input("Enter your list with sapce between numbers : ").split()))

# Printing Positive numbers.
for el in User_list:
    if el > 0:
        print(el, end=", ")