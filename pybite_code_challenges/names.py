# parse a list of names
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    li_names = []
    temp = []
    names = set(names) # Remove duplicates
    for item in names:
        item = item.split(' ')
        li_names.append(item)
        names = li_names

    # Sort in by 2nd Item
    names.sort(key = lambda x: x[1])

    # Make List
    names = [' '.join(item) for item in names]
      
    # Title each word here
    for item in names:
        temp.append(item.title())
    names = sorted(temp)
    return names  

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    temp = []
    ss_temp=[]
    names = set(dedup_and_title_case_names(names))
    names = list(names)
    for item in names:
        item = item.split(' ')
        temp.append(item)
        names = temp

    # Sort in reverse by 2nd Item
    names.sort(key = lambda x: x[1])
    names.reverse()

    # Make Reverse List
    names = [' '.join(item) for item in names]
      
    # Title each word here
    for item in names:
        ss_temp.append(item.title())
    names = ss_temp
    return names 

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    short = []
    li_names =[]
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
    return str(names)


print(f' No duplicates and Titled \n{dedup_and_title_case_names(NAMES)} \n')
print(f'Surname Dec \n {sort_by_surname_desc(NAMES)} \n')
print(shortest_first_name(NAMES),'\n')
print(f' No duplicates and Titled \n{dedup_and_title_case_names(PY_CONTENT_CREATORS)} \n')
print(f'Surname Dec \n {sort_by_surname_desc(PY_CONTENT_CREATORS)} \n')
print(shortest_first_name(PY_CONTENT_CREATORS))
    # print(f'test {names}')