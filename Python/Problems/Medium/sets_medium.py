# Q17. Given a sentence, find all unique words using a set (case-
#      insensitive). Return them as a sorted list.

# Q17. Given a sentence, find all unique words using a set (case-
#      insensitive). Return them as a sorted list.


input = "The quick brown fox jumps over the lazy dog and Fox is dog "

# though no strip is needed as spaces can be handled by split()
set_words = set(input.lower().strip().split())

sort_list = sorted(set_words)

print(sort_list)

# using functions - enhanced and beautiful
def get_unique_words(sentence):
    if not sentence or not sentence.strip():
        return []
    
    # Convert to lowercase, split into words, use set for uniqueness
    words_set = set(sentence.lower().split())
    
    # Convert set to sorted list
    sorted_words = sorted(words_set)
    
    return sorted_words


# ==================== Test Cases ====================
test_sentences = [
    "The quick brown fox jumps over the lazy dog and Fox is dog",
    "Hello hello HELLO world World",
    "Python is python and PYTHON is great",
    "   ",              
    ""                        
]

for sent in test_sentences:
    result = get_unique_words(sent)
    print(f"'{sent}' → {result}")

# Q18. Given two lists of student names (class A and class B), find:
#      (a) students in both classes, (b) students only in class A,
#      (c) students in either class but not both.

class_a = ["Alice", "Bob", "Charlie", "David", "Eve"]
class_b = ["Bob", "David", "Frank", "Grace", "Eve"]

# a.
both_class = set(class_a).intersection(set(class_b))

# b
only_a = set(class_a).difference(class_b)

# c
not_both = set(class_a).symmetric_difference(set(class_b))

print(f"a: {both_class}, b: {only_a}, c: {not_both}")


# Q19. Write a function that takes a list of lists and returns a set of
#      elements that appear in ALL of the sublists.

'''
My understanding:

function that takes a list of list - [[1,2,3], [2,3,4], [2,3,5]]
elements which are common between each list is 2,3 -> return as set{2,3}
'''

def common_set(LoL):
    sets = set(LoL[0])
    for element in LoL[1:]:
        if type(element) == list:
            sets = set(element).intersection(sets)
        else:
            pass
    return sets


LoL = [[1,2,3], [2,3,4], [2,3,5]]
result = common_set(LoL)
print(result)

# Q20. Given a list of integers, use sets to find all pairs (a, b) where
#      a + b = target. Return unique pairs only (no duplicates like (1,3)
#      and (3,1)).

'''
my understanding:

nums = [1, 3, 2, 4, 5]
target = 6

pairs where a + b = 6:
1+5=6 , 2+4=6 , 3+3=6 ✅ (but 3 appears once!)
Output: {(1,5), (2,4)}

'''
def unique_pairs(lst, tar):
    lst_pair = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == tar:
                lst_pair.append((lst[i],lst[j]))
    return set(lst_pair)

lst = [1,2,3,4,5,6]
target = 6
result = unique_pairs(lst, target)
print(result)
