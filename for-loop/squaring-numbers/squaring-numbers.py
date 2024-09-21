# prob:given a list of numbers print their squares
list = [1,2,3,4,5]
square_numbers = []    
# type1:
for number in list:
    square = number**2
    print(square)

# for printing the output in a list
for number in list:
    square = number**2
    square_numbers.append(square)
    print(square_numbers)


# type2:defining a method and calling the function
def squares(number):
    squares = number**2
    return squares

square_numbers = [squares(num1) for num1 in list]
print(square_numbers)

# type3

square_numbers1 = [num2**2 for num2 in list]
print("the square numbers are ",square_numbers1)


    

    






# need to be assigned only when you need output in form of list
# i did not understand how to append again

