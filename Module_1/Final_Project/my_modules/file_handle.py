import os
import pandas as pd
from my_modules.data_handle import is_valid_line, grade

Data_Folder = 'Data/'
Grade_Folder = 'Grades/'

def read_file(return_path = False):
    while True:
        os.system('clear')
        path = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
        print('Reading file...')
        os.system('sleep 0.5')
        os.system('clear')
        if not path.startswith(Data_Folder):
            path = Data_Folder + path
        if not path.endswith('.txt'):
            path += '.txt'
        try:
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
            print('Successfully opened', path.replace(Data_Folder, ''))
            break
    if return_path:
        return df, path
    return df

def write_file(df, path):
    df['Grade'] = None
    for i in range(len(df)):
        line = df.iloc[i, 0].split(',')
        if is_valid_line(line, print_noti = False):
            score, _, _ = grade(line)
            df.iloc[i, 0] = line[0]
            df.iloc[i, 1] = score

    df = df.dropna()
    path = path.removeprefix(Data_Folder).removeprefix(Grade_Folder).removesuffix('.txt')

    path = Grade_Folder + path + '_grades.txt'
    df.to_csv(path, sep = ',', index=False, header=False)

    print('Grading and saving the file...')
    os.system('sleep 1')
    os.system('clear')
    print('=========== Grading completed! ===========')
    print('Grades saved to', path.replace(Grade_Folder, ''))