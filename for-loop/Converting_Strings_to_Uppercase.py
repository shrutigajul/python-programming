# prob:Converting Strings to Uppercase 
words = ["fun","tv","mobile"]
for word in words:
    swaped_string = word.swapcase()
    print(swaped_string)


def stringUppercase(letters):
    swaped_string1 = letters.upper()
    return(swaped_string1)
converted_string = [stringUppercase(word1) for word1 in words]
print(converted_string)


swap_word = [word.upper() for word in words]
print(swap_word)
    
    

# swap.case converts lowercase to upper case but does not modify original string 
# so to assess the new converted string assign it to new variable and then print


    