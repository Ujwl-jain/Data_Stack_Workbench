# Q54 [Medium] Print a formatted table of products (name, qty, price) using f-strings with alignment.

products = [
    ('Apple',  10000, 'Rs 10/piece'),
    ('Laptop', 5,     'Rs 80000'),
    ('Pen',    500,   'Rs 10/piece'),
]

print(f"{'Name':<12} {'Qty':<10} {'Price':<12}")
print("-" * 45)
for name, qty, price in products:    # tuple unpacking!
    print(f"{name:<12} {qty:<10} {price:<12}")

# Q55 [Medium] Use f-string to display a progress bar: '████░░░░ 50%' dynamically based on a value.