# Write a function that takes a list of numbers and returns a tuple
#      of (min, max, sum, average) of the list.
# we can not append multiple elements together, need to do one by one, instead use extend()
def calculator(*numbers):
    cal_list = []
    sum = 0
    # a safety check just in case i sent a string for fun
    for n in numbers:    
        sum = sum + n

    avg = sum/len(numbers)
    cal_list.append(min(numbers))
    cal_list.append(max(numbers))
    cal_list.append(sum)    
    cal_list.append(avg)

    return tuple(cal_list)
result = calculator(5,10,2,51,24,12)
print(f"the result for this problem is {result}, and the type of result is {type(result)}")

# More enhaned version
# here if you return multiple things in bracket using comma separated it will return as tuple 
# even if bracket is not there and return is comma separated it will still return as tuple
def calculator(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return (min(numbers), max(numbers), total, avg)

result = calculator(5, 10, 2, 51, 24, 12)
print(f"Result: {result}, Type: {type(result)}")
