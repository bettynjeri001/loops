#  Create a for loop that iterates over the list [-1, 2, 3, 0, -4] and checks whether each number is positive or negative

numbers = [-1, 2, 3, 0, -4, -5] 
  
for number in numbers:
    if number > 0:
        print(number, "is a positive number")
    elif number < 0:
        print(number, "is a negative number")
    else:
        print(number, "is neither positive nor negative")