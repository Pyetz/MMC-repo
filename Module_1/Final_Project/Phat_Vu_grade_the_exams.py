# Built-in modules
import os

# My modules
import my_modules.file_handle as fh
import my_modules.statistics as stats
import my_modules.display_menu as display

def main():
    # Initialize global variables with default values
    screen = 1 # 1: Main menu, 2: Actions menu, None: Hidden
    choice = 0 # 1: Validate students, 2: Score students, 3: Write to file, 4: Return to main menu, 0: Hidden
    df = None # DataFrame to store the data of the choosen class
    path = None # Path to the choosen class

    # Main loop
    while True:
        # Clear the console after each iteration
        os.system('clear')

        # if screen is not None, display the appropriate menu, otherwise, handle the user's choice
        if screen is not None:
            match screen:
                case 1:
                    # The choice must be 1 or 2, otherwise, print an error message and ask the user to try again
                    display.main_menu()
                    choice = input('Enter your choice: ')
                    if choice == '1':
                        # change screen to actions menu, get user's choicen class by change df and path
                        screen = 2
                        df, path = fh.read_file(return_path = True)
                    elif choice == '2':
                        # Exit the program
                        print()
                        print('Exiting the program...')
                        os.system('sleep 1.5')
                        print()
                        print('Goodbye!')
                        break
                    else:
                        print('Invalid choice. Please try again.')
                        os.system('sleep 1')
                case 2:
                    # The choice must be 1, 2, 3 or 4, otherwise, print an error message and ask the user to try again
                    # if choice is valid, change screen to None to handle the user's choice
                    display.actions_menu()
                    choice = int(input('Enter your choice: '))
                    if 1 <= choice <= 4:
                        screen = None
                    else:
                        print('Invalid choice. Please try again.')
                case _:
                    pass
        else:
            # Handle the user's choice from the actions menu
            match choice:
                case 1:
                    # call valid_st function to display the valid and invalid lines of data
                    stats.valid_st(df)
                    print()
                    print('Press Enter to continue...')
                    os.system('read')
                    screen = 2
                    choice = None
                case 2:
                    # call score_st function to display the statistics of the scores in the class
                    stats.score_st(df)
                    print()
                    print('Press Enter to continue...')
                    os.system('read')
                    screen = 2
                    choice = None
                case 3:
                    # call write_file function to grade the exams and write the results to file
                    fh.write_file(df, path)
                    print()
                    print('Press Enter to continue...')
                    os.system('read')
                    screen = 2
                    choice = None
                case 4:
                    # Change screen to main menu and reset global variables
                    screen = 1
                    choice = None
                    df = None
                    path = None
                case _:
                    pass

# If this script is being run directly, call the main function
if __name__ == '__main__':
    main()