def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
#end function
word = str(input("Enter the string to be reversed: "))
print(reverse(word))
