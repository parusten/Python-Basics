# map = each element of iterable is passed to function and changes to returned value
#syntax of map = 
                #  map(function_name, iterable used)
# How it works:

# i)You provide a function and an iterable (e.g., list).
# ii)map() applies the function to each item in the iterable.
# iii)It returns a map object (which you can convert to a list)


numbers = [1, 2, 3, 4]

# Define a function to square a number
def square(x):
    return x * x

# Use map to apply the function to each item in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16]
