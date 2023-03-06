NAMES = ['arnold schwarzenegger', 'alec baldwin', 'daffy duck',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

li_names = []
temp = []
short = []

def dedup_and_title_case_names(names):
    names = set(names) # Remove duplicates
    for item in names:
        item = item.split(' ')
        li_names.append(item)

    # Sort in reverse by 2nd Item
        li_names.sort(key = lambda x: x[1])
        li_names.reverse()

    # Make Reverse List
    new_data = [' '.join(item) for item in li_names]
      
    # Title each word here
    for item in new_data:
        temp.append(item.title())
    names = temp
    return names  

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return names

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    #Setup the imported data
    for item in names:
        item = item.split(' ')
        li_names.append(item)
    names = li_names

    #Find shortest First Name
    for item in names: # Remove the first otem and append to a ne list
        tt = item[0]
        short.append(tt)
    short_low = sorted(short, key=len)   # Sort the list small -> large in length 
    short_smallest = short_low[0] # Extract the smallest item from the list
    names = short_smallest.title()
    return names


print(sort_by_surname_desc(NAMES))
