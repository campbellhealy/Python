ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print('Lexicographic sort')
print(sorted(ids))

print('Integer sort')
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # removes the first 2 chars prior to sort
print (sorted_ids)
