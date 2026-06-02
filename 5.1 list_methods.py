# ============================================================
#                     LIST METHODS IN PYTHON
# ============================================================
# A list is a mutable, ordered collection of items.
# Lists support duplicate values and mixed data types.
# Syntax: my_list = [item1, item2, item3]
# ============================================================


# ------------------------------------------------------------
# 1. append()
# ------------------------------------------------------------
# Adds a SINGLE item to the END of the list.
# Modifies the original list in-place (returns None).
# NOTE: appending a list adds it as ONE nested element.

list_example = [1, 12, 45, 11, 2, 0, 6]
list_example.append(9)
print(list_example)        # [1, 12, 45, 11, 2, 0, 6, 9]

list_example.append([10, 11])   # adds as a nested list
print(list_example)        # [1, 12, 45, 11, 2, 0, 6, 9, [10, 11]]


# ------------------------------------------------------------
# 2. sort()
# ------------------------------------------------------------
# Sorts the list IN-PLACE in ascending order by default.
# Use reverse=True for descending order.
# Returns None — it does NOT create a new list.
# TIP: Use sorted(list) if you want a NEW sorted list instead.

list_sort = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_sort.sort()                    # ascending order
print(list_sort)           # [1, 3, 3, 3, 4, 4, 4, 12, 45, 512]

list_sort.sort(reverse=True)        # descending order
print(list_sort)           # [512, 45, 12, 4, 4, 4, 3, 3, 3, 1]

# sorted() → returns a new list, original stays unchanged
original = [5, 2, 8, 1]
new_sorted = sorted(original)
print(original)            # [5, 2, 8, 1]   ← unchanged
print(new_sorted)          # [1, 2, 5, 8]   ← new sorted list


# ------------------------------------------------------------
# 3. reverse()
# ------------------------------------------------------------
# Reverses the list IN-PLACE (does NOT sort — just flips order).
# Returns None.
# ⚠️  COMMON MISTAKE: forgetting () makes it do nothing!

list_rev = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
# list_rev.reverse    ← ❌ WRONG: just references method, does nothing
list_rev.reverse()                  # ✅ correct
print(list_rev)            # [4, 3, 4, 3, 1, 45, 512, 4, 12, 3]


# ------------------------------------------------------------
# 4. index()
# ------------------------------------------------------------
# Returns the INDEX of the FIRST occurrence of a given item.
# Raises ValueError if the item is not found.

list_index = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_index.index(1))          # 5  (1 is at position 5)
print(list_index.index(3))          # 0  (first 3 is at position 0)

# Optional: index(item, start, end) — search within a slice
print(list_index.index(3, 1))       # 6  (next 3 after index 1)


# ------------------------------------------------------------
# 5. count()
# ------------------------------------------------------------
# Returns the NUMBER OF TIMES an item appears in the list.
# Returns 0 if item is not found (does NOT raise an error).

list_count = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_count.count(3))          # 3  (3 appears 3 times)
print(list_count.count(4))          # 3  (4 appears 3 times)
print(list_count.count(99))         # 0  (not in list)


# ------------------------------------------------------------
# 6. copy()
# ------------------------------------------------------------
# Returns a SHALLOW COPY of the list.
# Changes to the copy do NOT affect the original list.
# ⚠️  SHALLOW means: nested lists/objects are still SHARED.
#     Use copy.deepcopy() for a fully independent copy.

list_copy = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
m_copy = list_copy.copy()
m_copy[0] = 'ujjwal'
print(m_copy)              # ['ujjwal', 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_copy)           # [3, 12, 4, 512, 45, 1, 3, 4, 3, 4] ← unchanged

# Shallow copy warning with nested lists:
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99
print(nested)              # [[99, 2], [3, 4]] ← inner list IS affected!

deep = copy.deepcopy(nested)
deep[0][0] = 0
print(nested)              # [[99, 2], [3, 4]] ← inner list NOT affected ✅


# ------------------------------------------------------------
# 7. insert()
# ------------------------------------------------------------
# Inserts an item at a SPECIFIC INDEX.
# All elements from that index onward shift to the right.
# Syntax: list.insert(index, item)

list_insert = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_insert.insert(3, 'yayaya')     # insert at index 3
print(list_insert)         # [3, 12, 4, 'yayaya', 512, 45, 1, 3, 4, 3, 4]

# insert at start
list_insert.insert(0, 'start')
print(list_insert)         # ['start', 3, 12, 4, 'yayaya', 512, ...]

# insert at end (same as append)
list_insert.insert(len(list_insert), 'end')
print(list_insert[-1])     # 'end'


# ------------------------------------------------------------
# 8. extend()
# ------------------------------------------------------------
# Adds ALL ITEMS from another iterable (list, tuple, set, etc.)
# to the END of the existing list.
# Modifies the original list in-place (returns None).
# ⚠️  DIFFERENCE from append():
#     append([4,5]) → adds [4,5] as ONE element (nested)
#     extend([4,5]) → adds 4 and 5 as SEPARATE elements

list_extend = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_extended = ['a', 'b', 'c']
list_extend.extend(list_extended)
print(list_extend)         # [3, 12, 4, 512, 45, 1, 3, 4, 3, 4, 'a', 'b', 'c']

# extend works with any iterable:
list_extend.extend((10, 20))        # tuple
list_extend.extend("XY")           # string → adds 'X', 'Y' separately
print(list_extend[-4:])    # [10, 20, 'X', 'Y']


# ------------------------------------------------------------
# 9. Concatenation using + operator
# ------------------------------------------------------------
# Joins two lists and returns a BRAND NEW list.
# Original lists remain UNCHANGED.
# Unlike extend(), this does NOT modify either list in-place.

a = [1, 2, 4]
b = [3, 4, 6]
c = a + b
print(a)                   # [1, 2, 4]       ← unchanged
print(b)                   # [3, 4, 6]       ← unchanged
print(c)                   # [1, 2, 4, 3, 4, 6] ← new list


# ------------------------------------------------------------
# 10. remove()
# ------------------------------------------------------------
# Removes the FIRST OCCURRENCE of a given item from the list.
# Modifies the list in-place (returns None).
# ⚠️  Raises ValueError if the item is NOT found in the list.
# ⚠️  Only removes the FIRST match — not all duplicates.

list_remove = [3, 12, 4, 3, 45, 1, 3]
list_remove.remove(3)               # removes first 3 only
print(list_remove)         # [12, 4, 3, 45, 1, 3] ← only first 3 is gone

# to remove ALL occurrences, use a loop or list comprehension:
list_remove2 = [3, 12, 4, 3, 45, 1, 3]
list_remove2 = [x for x in list_remove2 if x != 3]
print(list_remove2)        # [12, 4, 45, 1] ← all 3s removed

# ⚠️  ValueError example (commented out to avoid crashing):
# list_remove.remove(999)  # ❌ ValueError: list.remove(x): x not in list


# ------------------------------------------------------------
# 11. pop()
# ------------------------------------------------------------
# Removes AND RETURNS the item at the given index.
# Defaults to the LAST item if no index is provided.
# ⚠️  Raises IndexError if the index is out of range.
# KEY DIFFERENCE from remove():
#     remove(x) → finds item by VALUE, returns None
#     pop(i)    → finds item by INDEX, returns the removed item

list_pop = [3, 12, 4, 512, 45, 1]
popped = list_pop.pop()             # removes & returns last item
print(popped)              # 1
print(list_pop)            # [3, 12, 4, 512, 45]

popped_at = list_pop.pop(2)         # removes & returns item at index 2
print(popped_at)           # 4
print(list_pop)            # [3, 12, 512, 45]

# common use case: pop() is used to implement stacks (LIFO)
stack = [1, 2, 3, 4]
stack.append(5)             # push
print(stack.pop())          # pop → 5  (last in, first out)


# ------------------------------------------------------------
# 12. clear()
# ------------------------------------------------------------
# Removes ALL items from the list.
# The list still EXISTS — it just becomes empty [].
# ⚠️  DIFFERENCE from del:
#     list.clear() → empties the list, list object still exists
#     del list      → deletes the entire list variable completely

list_clear = [3, 12, 4, 512, 45, 1]
list_clear.clear()
print(list_clear)          # []  ← empty list, variable still exists

# del comparison (commented out):
# del list_clear            # after this, accessing list_clear raises NameError


# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Method/Op        Modifies Original?   Returns              Use When
#  ──────────────────────────────────────────────────────────────────────
#  append(x)        ✅ Yes               None                 Add 1 item to end
#  sort()           ✅ Yes               None                 Sort in-place
#  sorted()         ❌ No                New list             Sort without changing original
#  reverse()        ✅ Yes               None                 Flip order in-place
#  index(x)         ❌ No                Index (int)          Find position of item
#  count(x)         ❌ No                Count (int)          Count occurrences
#  copy()           ❌ No                Shallow copy         Duplicate list safely
#  insert(i, x)     ✅ Yes               None                 Add item at specific index
#  extend(iter)     ✅ Yes               None                 Add many items to end
#  list1 + list2    ❌ No                New list             Merge into new list
#  remove(x)        ✅ Yes               None                 Remove first match by value
#  pop(i)           ✅ Yes               Removed item         Remove & retrieve by index
#  clear()          ✅ Yes               None                 Wipe list completely
#
# ============================================================
