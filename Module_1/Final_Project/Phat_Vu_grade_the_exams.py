import my_modules.file_handle as fh
import my_modules.statistics as stats
import my_modules.display_menu as display
import os

def main():
    screen = 1
    choice = 0
    df = None
    path = None
    while True:
        os.system('clear')
        match screen:
            case 1:
                display.main_menu()
                choice = input('Enter your choice: ')
                if choice == '1':
                    screen = 2
                    df, path = fh.read_file(return_path = True)
                elif choice == '2':
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
                display.actions_menu()
                choice = int(input('Enter your choice: '))
                if 1 <= choice <= 4:
                    screen = None
                else:
                    print('Invalid choice. Please try again.')
            case _:
                pass

        os.system('clear')

        match choice:
            case 1:
                stats.valid_st(df)
                print()
                print('Press Enter to continue...')
                os.system('read')
                screen = 2
                choice = None
            case 2:
                stats.score_st(df)
                print()
                print('Press Enter to continue...')
                os.system('read')
                screen = 2
                choice = None
            case 3:
                fh.write_file(df, path)
                print()
                print('Press Enter to continue...')
                os.system('read')
                screen = 2
                choice = None
            case 4:
                screen = 1
                choice = None
            case _:
                pass

if __name__ == '__main__':
    main()