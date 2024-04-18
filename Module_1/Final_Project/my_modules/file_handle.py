import os
import pandas as pd
from my_modules.data_handle import is_valid_line, grade

# Define the data and grade folders
Data_Folder = 'Data/'
Grade_Folder = 'Grades/'

def read_file(return_path = False):
    '''
    This function reads a file and returns a DataFrame.
    If you want to return the file path, set return_path to True.
    If the file does not exist, the user will be prompted to try again until a valid file is entered.
    '''
    while True:
        os.system('clear')
        path = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
        print('Reading file...')
        os.system('sleep 0.5')
        os.system('clear')

        # standardize the path
        if not path.startswith(Data_Folder):
            path = Data_Folder + path
        if not path.endswith('.txt'):
            path += '.txt'

        # using try-except to prevent the program from crashing if there is an error while reading the file
        try:
            # read the file using pandas, not separated
            # -> each line is a series in a single column with no header
            df = pd.read_fwf(path, header=None)
        except FileNotFoundError:
            print('The file does not exist. Please try again.')
            os.system('sleep 2')
            continue
        except Exception as e:
            print('An error occurred: ', e)
            os.system('sleep 2')
            continue
        else:
            # if the file is successfully read, break the loop and print the success message
            print('Successfully opened', path.replace(Data_Folder, ''))
            break

    # return the DataFrame and the path if return_path is True
    if return_path:
        return df, path
    
    # by default, return only the DataFrame
    return df

def write_file(df, path):
    '''
    This function takes a DataFrame and a path as input
    Then writes the DataFrame to the file at the given path, add '_grades' to the end of the file name
    '''

    # create a new column for the grades and set all values to None
    df['Grade'] = None

    # iterate through each row (type series) in the DataFrame
    # -> each row is a series in single line in the file
    # split the line by comma and check if it is a valid line
    # if it is valid:
    #    - grade the line by calling the grade function, set just_return_score to True to get only the score
    #    - remove all the answers and just keep the N# in the DataFrame
    #    - set the grade to the score
    for i in range(len(df)):
        line = df.iloc[i, 0].split(',')
        if is_valid_line(line, print_noti = False):
            score = grade(line, just_return_score = True)
            df.iloc[i, 0] = line[0]
            df.iloc[i, 1] = score

    # remove all the invalid lines
    df = df.dropna()

    # standardize the path
    path = path.removeprefix(Data_Folder).removeprefix(Grade_Folder).removesuffix('.txt')
    path = Grade_Folder + path + '_grades.txt'

    # save the DataFrame to the file
    df.to_csv(path, sep = ',', index=False, header=False)

    # print the success message
    print('Grading and saving the file...')
    os.system('sleep 1')
    os.system('clear')
    print('=========== Grading completed! ===========')
    print('Grades saved to', path.replace(Grade_Folder, ''))