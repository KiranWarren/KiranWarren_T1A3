# Clear Terminal Function
#
# This function clears the current contents of the terminal.

# Import modules
import os
import platform


def clear_terminal():
    '''Clear the terminal command based on the user's platform'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
