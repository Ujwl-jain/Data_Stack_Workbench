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

# Q19. Write a function that takes a list of lists and returns a set of
#      elements that appear in ALL of the sublists.

# Q20. Given a list of integers, use sets to find all pairs (a, b) where
#      a + b = target. Return unique pairs only (no duplicates like (1,3)
#      and (3,1)).
