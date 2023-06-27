import os
import platform

# Clear terminal command based on user's platform
def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')