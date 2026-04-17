# Q30 [Medium] Given mixed input (int, float, str), convert all to float and sum them. Handle errors gracefully.

# manual approach
v_int = 10
v_str = '10'
v_float = 9.9 

try:
    result = float(v_int) + v_float + float(v_str)
    print(result)

except ValueError as e:
    print(f'one of the value is not converted: {e}')


# actual problem
lst_of_items = [10,'9.9', 11.3, True, 'ABC']
result = 0
for item in lst_of_items:
    try:
        result = result + float(item)
    except ValueError as e:
        print(f'Ignoring the value as the value can not be convert to deired value - {item} -> {e}')

print(result)

# Q31 [Medium] Convert a decimal number to binary, octal, and hexadecimal without using bin/oct/hex.

# Q59. Write a function that reads a string like "10 20 30 40 50",
#      splits it by spaces, converts each to int, and returns the
#      min, max, and average as a tuple of floats.

def conversion(str1):
    sum = 0
    element_list = []
    for item in str1:
        try:
            i = int(item)
            sum = sum + i
            element_list.append(i)
        except ValueError:
            print(f'cant convert {item}')
    
    return float(min(element_list)), float(max(element_list)), float(sum/len(element_list))

str1 = "10 20 30 40 50 ABC"
list_str = str1.split()
result = conversion(list_str)
print(result)
