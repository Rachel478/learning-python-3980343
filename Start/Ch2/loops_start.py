# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# answer = input("Should I stop?")
# while answer != "yes":
#   print(answer)
#   answer = input("Should I stop?")

# define a for loop
# days = ["Mon","Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
# for d in days:
#   if (d == "Thur"):
#     #break
#     continue
#   print(d)

# using the enumerate() function to get an index and an item
days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i,d in enumerate(days):
  print(i,d)