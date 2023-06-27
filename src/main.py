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
        break
print('Application Closed')