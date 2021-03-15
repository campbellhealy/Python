# Program to find the ASCII value of the given character
# Add reverse as double check
def checkEqusl(x, y):
    if len(x) == len(y):
        print("Pass")
    else: 
        print("Fail")


# Lists  chr is the starting list, num is the convert to ASCII, 
# asst is convert back to chr to compare against original
list_chr = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
list_num = []
list_asst = []


# ASCII value for character
for item in list_chr:
    d = item
    e = str(ord(d))
    list_num.append(e) # Building the list for the second test
    print("The ASCII value of '" + d + "' is"' '+ e)

# character for ASCII value
for item in list_num:
    f = item
    g = f
    f = int(f)
    h = chr(f)
    list_asst.append(g) # Building the assert to compare against the original list
    print("The Char value of '" + g + "' is"' '+ h)

# The assertion Double Check
checkEqusl(list_chr, list_asst)
