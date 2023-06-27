import os

def import_file():
    # Determine folder path of 'inputs' folder.
    # Need to use join method in case of Windows OS.
    inputs_folder_path = os.path.join(os.path.dirname(__file__), "inputs")

    # Create list of files within 'inputs' folder.
    file_list = []
    for (path, folders, files) in os.walk(inputs_folder_path):
        file_list.extend(files)

    # Remove non-.txt files from file_list
    for i in range(0, len(file_list)):
        if file_list[i][-4:] != ".txt":
            file_list.remove(file_list[i])
    
    # If no relevant files are in the 'inputs' folder, exit to main menu.
    if len(file_list) == 0:
        print("There are no .txt files in the 'inputs' folder. Please place a .txt file in this directory before running this application.")
        return

    # Show the user the available text files within the 'inputs' folder.
    print('Here are all the .txt files in the inputs folder:')
    for i in range(1, len(file_list) + 1):
        print(f"{i}     {file_list[i - 1]}")
    print('')

    # Ask the user which file they want to import.
    print('Which file would you like to choose? In the console, input the corresponding number of the file you want to import.')
    print('Or press 0 to return to the main menu.')
    print('')
    file_num = int(input('File number: '))

    # Exit back to the main menu if user inputs 0
    if file_num == 0:
        return

    # Ensure that the user has entered a number within the expected range.
    while not file_num in range(1, len(file_list) + 1):
        file_num = int(input('Sorry, please try again or press 0 to return to the main menu: '))
        if file_num == 0:
            return
        
    # Return the file that the user has specified.
    return os.path.join(inputs_folder_path, file_list[file_num - 1])
    

