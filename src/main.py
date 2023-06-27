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
    # Handle empty string error, interpret as wanting to close application
    try:
        task = int(input('Enter selection: '))
    except:
        task = 0

    # Run functions based on user selection.
    if task == 1:
        replace()
    elif task == 2:
        double_space()
    elif task == 3:
        encrypt()
    elif task == 4:
        decrypt()
    elif task == 5:
        word_count()
    elif task == 6:
        top_occurrences()
    elif task == 7:
        occurrence()
    else:
        break

# Close application
clear_terminal()
print('Application Closed')