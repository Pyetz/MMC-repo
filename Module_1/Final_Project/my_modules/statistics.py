import numpy as np
from my_modules.data_handle import is_valid_line, grade, max_freq

def valid_st (df):
    '''
    This function takes a DataFrame as input
    Then prints the number of valid and invalid lines of data based on the task 2 requirements
    '''
    total_valid = 0
    total_invalid = 0
    print()
    print('**** ANALYZING ****')
    print()

    # Loop through each row (type series) in the DataFrame
    # Split the series in each row by comma to get a list of values
    # Check if the line is valid by calling the is_valid_line function
    # If the line is valid, increment the total_valid variable by 1
    # If the line is invalid, increment the total_invalid variable by 1

    # The detailed report about the invalid lines will be printed out in the is_valid_line function
    for i in range(len(df)):
        line = df.iloc[i, 0].split(',')
        valid = is_valid_line(line)
        if valid:
            total_valid += 1
        else:
            total_invalid += 1
    
    if total_invalid == 0:
        print('No errors found!')

    print()
    print('**** REPORT ****')
    print()
    print('Total valid lines of data:', total_valid)
    print('Total invalid lines of data:', total_invalid)
    print()
    print()

def score_st(df):
    '''
    This function takes a DataFrame as input
    Then prints the following statistics based on the task 3 requirements:
    '''

    # Create three empty numpy arrays to store the scores, skips, and incorrects
    scores = np.array([], dtype=int)
    skips = np.array([], dtype=int)
    incorrects = np.array([], dtype=int)
    # count the total number of valid lines for the ratio statistics
    total_valid_lines = 0

    # Loop through each row (type series) in the DataFrame
    # Split the series in each row by comma to get a list of values
    # Check if the line is valid by calling the is_valid_line function
    # If the line is valid:
    #   - Increment the total_valid_lines variable by 1
    #   - Append the corresponding (gotten from the grade function) to the scores, skips, and incorrects nparrays
    for i in range(len(df)):
        line = df.iloc[i, 0].split(',')
        if is_valid_line(line, print_noti = False):
            total_valid_lines += 1
            score, skip_idxs, incorrect_idxs = grade(line)
            scores = np.append(scores, score)
            skips = np.append(skips, skip_idxs)
            incorrects = np.append(incorrects, incorrect_idxs)

    print('Total student of highest score:', np.sum(scores >80))
    print()
    print('Mean (average) score:', format(np.mean(scores), '.2f'))
    print('Highest score:', np.max(scores))
    print('Lowest score:', np.min(scores))
    print('Range of scores:', np.max(scores) - np.min(scores))
    print('Median score:', int(np.median(scores)))
    print()
    print('Question that most people skip:', max_freq(skips, total_valid_lines))
    print('Question that most people answer incorrectly:', max_freq(incorrects, total_valid_lines))
    print()
    print()