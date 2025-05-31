# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
myList = [0, 1, "two", 3.2, False]
# print(len(myList))

# to access a member of a sequence type, use []
# print(myList[2])
# print(myList[-1])
# myList[0] = 10
# print(myList)


# add a list to another list
# another_list = [6,7,8]
# myList = myList + another_list
# print(myList)

# use slices to get parts of a sequence
print(myList[1:4:2])
print(myList[::2])
print(myList[::-1])

# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable
mytuple = (0, 1, 2, "three")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 2, "hey"}
print(myset)
# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in myList)
print(3 in mytuple)
print(5 in myset)
