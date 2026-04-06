# =============================================================================
# Q54 [Medium] - Formatted Table using f-strings
# Print a formatted table of products (name, qty, price) with alignment
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Print a clean, aligned table like this:
#
# Name            Qty          Price
# -------------------------------------------
# Apple           10000        Rs 10/piece
# Laptop          5            Rs 80000
# Pen             500          Rs 10/piece
#
# Without formatting → messy unaligned output
# With formatting    → clean columns that line up!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — f-string Alignment Syntax
# -----------------------------------------------------------------------------
# {value:<width}  → LEFT align   (convention for text)
# {value:>width}  → RIGHT align  (convention for numbers)
# {value:^width}  → CENTER
#
# width = how many characters wide the column is
#
# Example:
#   f"{'apple':<15}"  → 'apple          '  (padded to 15 chars)
#   f"{'apple':>15}"  → '          apple'
#   f"{'apple':^15}"  → '     apple     '
#
# RULE: Header and rows MUST use SAME width — or columns shift and break!
#
#   Header: f"{'Name':<15} {'Qty':^10}"
#   Row:    f"{name:<15}   {qty:^10}"   ← same 15 and 10!
#
# Convention (not a rule):
#   Text   → left align  (<)
#   Numbers→ right align (>)
#   Just use what looks good to you!


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

products = [
    ('Apple',  10000, 'Rs 10/piece'),
    ('Laptop', 5,     'Rs 80000'),
    ('Pen',    500,   'Rs 10/piece'),
]

print(f"{'Name':<15} {'Qty':^15} {'Price':<15}")   # header
print("-" * 45)                                     # separator
for name, qty, price in products:                   # tuple unpacking!
    print(f"{name:<15} {qty:^15} {price:<15}")      # same widths as header!

# Output:
# Name            Qty          Price
# ---------------------------------------------
# Apple           10000        Rs 10/piece
# Laptop          5            Rs 80000
# Pen             500          Rs 10/piece


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. {value:<width} → left, {value:>width} → right, {value:^width} → center
# 2. Header and rows MUST have same column widths — or table breaks!
# 3. Convention → text left, numbers right — but no strict rule!
# 4. "-" * 45 → repeats "-" 45 times — clean separator line!
# 5. Tuple unpacking in loop → for name, qty, price in products
