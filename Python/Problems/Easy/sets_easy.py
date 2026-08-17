# Q46. Write a function using sets that takes a string and returns True
#      if all characters in it are unique (no repeats).

def unique(str1):
    str_set = set(list(str1))
    if len(str_set) == len(str1):
        return True
    else:
        return False

str1 = 'Ujjwal'
result = unique(str1)
print(f'the output for the uniqueness of the string is : {result}')

# Q47. Given a list of integers, use a set to find and return all numbers
#      that appear more than once (duplicates only). Return sorted list.

def sorted_duplicate(lst):
    set_int = set(lst)
    duplicate_list = []
    for i in set_int:
        if lst.count(i) > 1:
          duplicate_list.append(i)  
        else:
            pass
    return sorted(duplicate_list)

list_int = [99,1,2,3,5,6,2,3,1,99,10]
result = sorted_duplicate(list_int)
print(f'the output  is : {result}')


# Q48. Write a function that takes two sets of tags (like blog post tags)
#      and returns: common tags, tags only in first set, tags only in
#      second set — as three separate sets.

def set_tags(t1,t2):
    common = t1.intersection(t2)
    only_t1 = t1.difference(t2)
    only_t2 = t2.difference(t1)
    return common, only_t1, only_t2


tags1 = {'python', 'coding', 'tutorial', 'beginner', 'django'}
tags2 = {'python', 'tutorial', 'advanced', 'flask', 'coding', 'api'}
result_common, result_onlyt1, result_onlyt2 = set_tags(tags1,tags2)

print(f'the common tags are : {result_common}')
print(f'the tags in set 1 : {result_onlyt1}')
print(f'the tags in set 2 : {result_onlyt2}')

# Expected:
# Common:       {'python', 'coding', 'tutorial'}
# Only in tags1: {'beginner', 'django'}
# Only in tags2: {'advanced', 'flask', 'api'}
