"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

# use a for loop
for arg in sys.argv: print(arg)

# use string join method
print('\n'.join(sys.argv))

# Print out the OS platform you're using:
print('os platform:', sys.platform)

# Print out the version of Python you're using:
print('python version:', sys.version[:5])


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('current process:', os.getpid())

# Print the current working directory (cwd):
print('current directory:', os.getcwd())

# Print out your machine's login name
print('machine login name:', os.getlogin())
