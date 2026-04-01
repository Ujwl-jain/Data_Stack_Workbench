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
# intersection_update()

# difference()
# isdisjoint()
# issuperset()
# symmentic_difference()
# issubset()
# add()
# remove()
#  discard()
# pop()
# del - keyword, not method
# clear()
# check if item exists



