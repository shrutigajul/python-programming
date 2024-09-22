# prob:Creating a List of Lengths of Strings
words = ["word","happy","sad"]
# for word in words:
#     length = [len(word)]
#     print(length)

def lengthWords(number):
    length1 = [len(number)]
    return length1
count = [lengthWords(count1) for count1 in words]
print(count)

list1 = [len(number) for number in words ]
print(list1)


# doubt why not write number(defining) and then len(number) for number in words