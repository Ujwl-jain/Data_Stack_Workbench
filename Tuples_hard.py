# Q57. Write a function that takes a list of coordinate tuples (x, y)
#      and returns them sorted first by x, then by y, then returns only
#      the unique coordinates (no duplicates).

'''
My understanding(correct confirmed by claude): 
sort the list of cordinated tuples by x first and then y, here we can do this using lambda, then only return the unique cordinates 

for example lets say list of tuple = [(1,2),(4,2)(4,1),(2,3)(1,9)(9,7)]
then sort by x and then y which will become like this - [(1,2),(1,9),(2,3),(4,1),(4,2),(9,7)]
then return the unique coordinates since all are unique it will return all
for removing duplicate we can convert the list of tuples to set and then list again to remove the duplicates
and then sort
'''
def cordinator(coords):
    unique_coords = list(set(coords))  
    final_coords = sorted(unique_coords, key = lambda x: (x[0], x[1]))
    return final_coords
    
coords = [(1,2), (4,2), (4,1), (2,3), (1,2), (4,2), (1,9), (9,7)]
result = cordinator(coords)
print(f"the result for the coordinator question is {result}")

# without function creation
coords = [(1,2), (4,2), (4,1), (2,3), (1,2), (4,2), (1,9), (9,7)]
unique_coords = list(set(coords))  
print(f"the result for the unique coordinate is {unique_coords}")
final_coords = sorted(unique_coords, key = lambda x: (x[0], x[1]))
print(f"the result for the coordinator question is {result}")
