# =============================================================================
# Q47, Q48, Q49 - Dictionary Problems
# =============================================================================


# -----------------------------------------------------------------------------
# Q47. Word Lengths Dictionary
# Takes a list of words, returns {word: length}
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict
# 2. Loop through words
# 3. dict[word] = len(word)
# 4. Return dict

def word_count(word_c):
    dict_final = {}
    for word in word_c:
        dict_final[word] = len(word)   # key=word, value=its length
    return dict_final

word_c = ['Mango', 'potato', 'sabji', 'yellow', 'ramen']
print(word_count(word_c))
# Output: {'Mango': 5, 'potato': 6, 'sabji': 5, 'yellow': 6, 'ramen': 5}


# -----------------------------------------------------------------------------
# Q48. Total Amount Spent Per Person
# List of {'name', 'amount'} dicts → {name: total}
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict
# 2. Loop through each transaction
# 3. Extract name and amount directly using known keys
# 4. If name NOT in dict → create new key with amount
# 5. If name already exists → add to existing total
# 6. Return dict

def transaction(banking):
    final_dict = {}
    for current_dict in banking:
        name   = current_dict['name']
        amount = current_dict['amount']
        if name not in final_dict:
            final_dict[name] = amount    # first time → create
        else:
            final_dict[name] += amount   # repeat → accumulate!
    return final_dict

banking = [
    {'name': 'Ujjwal', 'amount': 500},
    {'name': 'Rahul',  'amount': 300},
    {'name': 'Ujjwal', 'amount': 200},
    {'name': 'Rahul',  'amount': 100},
    {'name': 'Priya',  'amount': 400},
]
print(transaction(banking))
# Output: {'Ujjwal': 700, 'Rahul': 400, 'Priya': 400}

# KEY PATTERN — first time vs repeat:
#   if key not in dict → dict[key] = value       (create)
#   else               → dict[key] += value       (accumulate)
# This pattern appears everywhere in dictionary problems!


# -----------------------------------------------------------------------------
# Q49. Common Keys with Tuple Values
# Two dicts → keys common to both → {key: (val_from_dict1, val_from_dict2)}
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict
# 2. Loop through dict2 keys and values using .items()
# 3. If key exists in dict1 → common key found!
# 4. Store as tuple → result[key] = (dict1[key], dict2_value)
# 5. Return dict

def dict_filter(a, b):
    filter_dict = {}
    for k, v in b.items():
        if k in a:
            filter_dict[k] = (a[k], v)   # tuple of both values!
    return filter_dict

dict1 = {'name': 'Ujjwal', 'Human': 'No',    'Class': 'No class'}
dict2 = {'name': 'Karan',  'Age':   24,       'Class': 'Interview'}
print(dict_filter(dict1, dict2))
# Output: {'name': ('Ujjwal', 'Karan'), 'Class': ('No class', 'Interview')}

# KEY CONCEPTS:
#   if k in dict       → checks keys only ✅
#   if k in dict.items()→ checks key-value pairs ❌ wrong for this!
#   (a[k], v)          → tuple — just wrap two values in ()!
#   No else needed     → if condition fails, nothing happens automatically!
