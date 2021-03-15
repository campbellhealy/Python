# loop_dict_named_tuples.py

from collections import namedtuple
from functools import reduce

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

more_belts = dict(brown=BeltStats(400, 2),
                    black=BeltStats(600, 5))

ninja_belts_updated = {**ninja_belts, **more_belts}

def get_total_points(belts=ninja_belts):
    j = 0
    total_score = 0
    for item in belts:

        data=[]
        stats =[]
        i = 0

        # Gets all the figures
        for _,v in belts.items():
        # Extract all the values
            for item in v:
                data.append(item)
        # iterate through the values as pairs, multiple the pair and add to the subtotal
        while  i < 2:
            for item in data:
                stats.append(data[j])
                j += 1   # This keeps the count going through the list 
                i +=1    # This prevent more tet the pairs gettting multiplied
                break
        total_score = total_score + reduce(lambda a,b: a*b, stats)
    return total_score


print(f"The total score is for ninja belts: {get_total_points(ninja_belts)}")
print(f"The total score is for ninja belts: {get_total_points(ninja_belts_updated)}")