# SET

'''
it is a collection of unordered data items, they store multiple items in a single variable

they are unchangable meaning, we can not change item once it is created
they do not contain duplicate items

set occuered in random order while printing hence they can not be accessed using indexing

for example:
set = {1,2,'jain',True,6}
not_a_set = {1,2,3,4,5,2,2,1}
'''

set_ex = {1,'ujjwal', True,'2',9}
print(set_ex)

# how to access the set - using loop

for i in set_ex:
    # it will print in random order as set is unordered and will not print duplicate values
    print(i)

# here it will not print the repeated values
not_a_set = {1,2,3,4,5,2,2,1}
print(not_a_set)

# ---------- empty set ----------
#  this becomes a dictonary
set_empt = {}
print(type(set_empt))

# this becomes a set
set_empt = set()
print(type(set_empt))


# ------------------- sets method -----------------------------

'''
sets method works the way set works in maths
'''
s = {1,2,3,4,5}
s2 = {3,6,7}

# Union() - this will return the new set, the original set are still the same and untouched
print(s.union(s2))
print(s,s2)

# update() 
# here we can update a particular set, unlike union this will update the current set
s.update(s2)
print(s)
print(s,s2)

# intersection()
#  here it returns the set where the values are same for both the sets means common elements between 2 sets
c = {'madrid', 'barca', 'liverpool', 'man city'}
c2 = {'madrid', 'barca','bayern', ' dortmund', 'csk', 'rcb'}

c3 = c.intersection(c2)
print(c3)

# intersection_update()
#  the set will be updated into the values where the elements are common between 2 sets other value were removed from the set
c.intersection_update(c2)
print(c)

# difference()
# this method will return the values from original set after removing the common value between 2 sets
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c2 = {'madrid', 'barca','bayern', ' dortmund', 'csk', 'rcb'}

c3 = c.difference(c2)
print(c3)

# difference_update
# same thing it will do as difference() but will update the orignial set instead of return inside the 3rd set
c.difference_update(c2)
print(c)


# isdisjoint()
# disjoint sets are those sets, which have no element in common

c = {'difference'}
c2 = {'madrid', 'barca'}

print(c.isdisjoint(c2))

# issuperset()
# if original set has all the elements of a particular set, then it will return true

c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c2 = {'madrid', 'barca'}

print(c.issuperset(c2))

# issubset()
# checks if the orignial set values contains in the particular sets
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c2 = {'madrid', 'barca'}

print(c2.issubset(c))

# symmentic_difference()
# basically all the unique values will be returned between the 2 sets, and common values will be removed, it returns inside the new set
c = {'madrid', 'barca', 'liverpool', 'man city'}
c2 = {'madrid', 'barca','bayern', ' dortmund', 'csk', 'rcb'}

c3 = c.symmetric_difference(c2)
print(c3)

# symmentic_difference_update()
# this will update the set whre we are performing the emthod as the set got updated with unique value between 2 sets , and whatever common value was there will be removed
# this updated the original set
c.symmetric_difference_update(c2)
print(c)


# add()
# it will add an item to a set
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c.add('Ujwal')

print(c)


# remove()
# use to remove teh items from the set, the main differenc is if the item is not present in the set then this will not raise error, but remove will raise it
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}   
c.remove('madrid')

print(c)

#  discard()
# use to remove teh items from the set, the main differenc is if the item is not present in the set then this will not raise error, but remove will raise it
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c.discard('madrid2')

print(c)

# pop()
# this method removes the last element in the set, but the thing is last order does not matter in this as set is unorderd
# but you can catch the popped item in a variable
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
item = c.pop()

print(c)
print(item)

# del - keyword, not method
# delete the set entirely, it will through an error as set will be delete, its output will always be namederror
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
del c

# print(c)


# clear()
# what if we domt want to delete the entire set but all the elements inside the set then we will use clear()
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
c.clear()

print(c)


# check if item exists - use in keyword to check the element in a set
c = {'difference','madrid', 'barca', 'liverpool', 'man city'}
if 'madrid' in c:
    print(True) 
