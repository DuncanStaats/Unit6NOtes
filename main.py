'''
Name: Duncan Staats
Date: 12/2/2024
Description: 
'''

name = "starla"
age = 5
description = f"{name} like wand toys and is {age}"
print(description)

descripitoin = name + " likes wand toys and is " + str(age)
print(description)

# Indexing - every character in a string has a location
# Starting at 0 from the beginining or -1 from the end

#  0  1  2  3  4  5
#  S  t  a  r  l  a
# -6 -5 -4 -3 -2 -1

first_letter = name[0]
print(first_letter)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1 * len(name)] # if you don't know the name
print(first_letter)

last_letter = name[-1] # always this one
print(last_letter)
last_letter = name[len(name)-1]
print(last_letter)

# use [ ] to access a character not ( ) - gives TypeError
# accessing an index that does not exist gives IndexError

# HW for lesson 1 is 7.1.5 - 7.1.6
def initials(first, last):
    first = first[-1 * len(first)]#first letter should always be "0", last letter should always be "-1"
    last = last[-1 * len(last)]
    return f"{first}.{last}."

print(initials("Duncan", "Staats"))
print(initials("Leyton", "Staats"))
print(initials("Hudson", "Staats"))

#Slicing - used to access 1 or more characters in a string
#Instead of name[0]+name[1]+name{2} we can do name[0:3]

#first three letters
first_three = name[0]+name[1]+name[2]
print(first_three)
first_three = name[0:3] # start at index 0, go up to but not inculde 3
print(first_three)

# format
# string_name[start:stop:step] - none are technically required

word_one = "Adventure"
word = word_one[3:60]
print(word)
word = word_one[:6]
print(word)
word = word_one[:]
print(word)
word = word_one[-3:]
print(word)
word = word_one[:-6]
print(word)

#HW for lesson 2, 7.2.6 - 7.2.8