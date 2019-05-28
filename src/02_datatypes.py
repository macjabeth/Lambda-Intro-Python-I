"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Display the values we're working with

print('x:', x, 'y:', y)

# Write a print statement that combines x + y into the integer value 12

print('combine `x + y` to integer:', x + int(y))

# Write a print statement that combines x + y into the string value 57

print('combine `x + y` to string:', str(x) + y)
