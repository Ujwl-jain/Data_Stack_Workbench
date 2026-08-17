# SLICING - WORKS WITH List, tuples, string, range not with dictonary, sets
s = 'python'

# 1. basic forward slicing (step is default = 1)
# s[start:end]

print(s[1:4])   # yth


# 2. reverse entire string
# s[::-1]

print(s[::-1])  # nohtyp


# 3. reverse part of string
# s[5:2:-1]

print(s[5:2:-1])  # noh


# 4. skip characters
# s[::2] -> movement -> 0 → 2 → 4
# step = 2 means take every second character

print(s[::2])   # pto


# 5. reverse with skipping
# s[::-2]
# start from end and move left by 2 steps

print(s[::-2])  # nhy


# MASTER RULE

# if step > 0 → move right
# if step < 0 → move left
# s[:]      → copy
# s[1:]     → remove first
# s[:-1]    → remove last
# s[-1]     → last element
# s[::-1]   → reverse
# s[::2]    → skip characters
# s[::-2]   → reverse with skip

# ----------------------------- Slicing with string-----------------------------
name1 = 'i am ujjwal jain'
print(len(name1))

# this works
print(name1[0:2])

# this works cause it will by default take 0 in [:2]
print(name1[:2])

# --------- negative slicing ----------------

# it means as - name1[0:len(name1) - 6]
# by default there is len() before the indexing

# both are same and works 0 is by default
print(name1[:len(name1)-6])
print(name1[:-6])

# here same thing will happen as len() func is by default will be before indexing
# this indexing will work

#  when doing negetive indexing like below before indexing should be lower than the after indexing like below
print(name1[-6:-2])


# ------reverse a string------

# [::-1] means
# start = default
# end   = default
# step  = -1 -> backwards or 1 -> forward


print(name1[::-1])

# ------------------slicing with list--------------------------
lst = ['p','y','t','h','o','n']

# 1. basic forward slicing
print(lst[1:4])      # ['y','t','h']

# 2. reverse entire list
print(lst[::-1])     # ['n','o','h','t','y','p']

# 3. reverse part
print(lst[5:2:-1])   # ['n','o','h']

# 4. skip characters
print(lst[::2])      # ['p','t','o']

# 5. reverse with skipping
print(lst[::-2])     # ['n','h','y']

# -------------------------slicing with tuples -----------------
t = ('p','y','t','h','o','n')

# 1. basic forward slicing
print(t[1:4])      # ('y','t','h')

# 2. reverse entire tuple
print(t[::-1])     # ('n','o','h','t','y','p')

# 3. reverse part
print(t[5:2:-1])   # ('n','o','h')

# 4. skip characters
print(t[::2])      # ('p','t','o')

# 5. reverse with skipping
print(t[::-2])     # ('n','h','y')

# ---------------------sliciing with range ------------------------
t = ('p','y','t','h','o','n')

# 1. basic forward slicing
print(t[1:4])      # ('y','t','h')

# 2. reverse entire tuple
print(t[::-1])     # ('n','o','h','t','y','p')

# 3. reverse part
print(t[5:2:-1])   # ('n','o','h')

# 4. skip characters
print(t[::2])      # ('p','t','o')

# 5. reverse with skipping
print(t[::-2])     # ('n','h','y')


