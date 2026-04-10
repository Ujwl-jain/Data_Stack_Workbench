# Q9.  Write a lambda function that takes a list of tuples (name, score)
#      and returns the list sorted by score in descending order.

data = [('alice', 'maths', 85), ('matter', 'english', 98), ('alice', 'ciene', 18), ('matter', 'hindi', 99), ('harry', 'sst', 77), ('DJ', 'sports', 99)]

# this code will male sure to sort the score and name in descending order but in case of tiebreaker name will sort as well to make sure name does not be in descending oreder
final_list  = sorted(data, key = lambda x: (x[2], x[0]), reverse = True)

#  use this : below code is used to make sure name will not be in descending order, In simple terms, '-' before score indexing also means score in descending
#  cause the score then will be in minus like -99, which is auto matically a smaller number and operating will perform in ascending order: -99, -98,-18,-7
# since inside key all elements are used for temperroray basis '-' will be thrown and it will return the same order but with out minus hence sorted in descending, only works on number
# key=lambda x: (-x[2], x[0])  # ← negative score = descending, name stays ascending!
print(final_list)
