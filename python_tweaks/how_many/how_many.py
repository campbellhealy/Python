# The how_many function determine if it's one of or more than 1
# Giving the correct English sentence
def how_many(list):
    if list[0] == 1:
        return "There is one " + list[1] + "."
    else:
        return "There are " + str(list[0]) + " " + list[1] + "."


# change the value of fish between 1 and 10 to test the function works as expected
# List could be pulled in from somewhere else then ran through this function
def each_list():
    List = [[1, "Pie"], [10, "Fish"], [5, "apples"]]
    for p in List:
        l = how_many(p)
        print(l)


# this is the main command triggering each_list to use each list in the array
# to insert the entries into the how_many function and return the string to the
#  each_list function for printing

# See the difference encasing the function in a print() does to the output
# print(each_list())
each_list()