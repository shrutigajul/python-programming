# prob:given list of numbers and a number,divde this list with the numbers
numbers=[1,2,3,4,5,6,7]
divisor = 3
# for number in numbers:
#     if number%3 ==0:
#         print(number)

# newlist = []
# for number in numbers:
#     if number%3 ==0:
#         newlist.append(number)
#         print(newlist)

#make a method for dividing the given list of numbers by 3 and give an output of the numbers in form of list
def numbersDivideBy3(number,divisor):
    return number/divisor
    
output = [numbersDivideBy3(number1,divisor) for number1 in numbers ]
print(output)

# why did it not need the NONE case??
# because we are not giving an if condition, we are printing every number which can be divided by 3 irrespespective if the remainder is 0 or not



    