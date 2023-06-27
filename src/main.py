from main_menu import *
from replace_function import *
from double_space_function import *
from encrypt_function import *
from decrypt_function import *
from word_count_function import *
from top_occurrences_function import *
from occurrence_function import *


while True:
    # Present application functions.
    main_menu()

    # Request a selection from the user.
    task = int(input('Enter selection: '))

    # Run functions based on user selection.
    if task == 1:
        replace()
    if task == 2:
        double_space()
    if task == 3:
        encrypt()
    if task == 4:
        decrypt()
    if task == 5:
        word_count()
    if task == 6:
        top_occurrences()
    if task == 7:
        occurrence()
    else:
        break
clear_terminal()
print('')
print('Application Closed')