import numpy as np

def is_valid_line(line, print_noti = True):
    '''
    This function takes a list of strings as input
    Then checks if the line is valid or not
    You can choose to print the notification or not by setting print_noti to True or False

    A valid line must:
        - have exactly 26 values
        - the first value must start with 'N' and followed by 8 digits
    If the line is valid, return True
    Otherwise, return False
    '''

    if len(line) != 26: # check if the line has exactly 26 values
        if print_noti:
            print('Invalid line of data: does not contain exactly 26 values')
            print(','.join(line))
            print()
        return False
    elif not line[0].startswith('N'): # check if the first value starts with 'N'
        if print_noti:
            print('Invalid line of data: N# is invalid')
            print(','.join(line))
            print()
        return False
    elif not line[0][1:].isdecimal() or len(line[0][1:]) != 8: # check if the N# has 8 digits
        if print_noti:
            print('Invalid line of data: N# is invalid')
            print(','.join(line))
            print()
        return False
    
    return True

def grade (answer, just_return_score = False):
    '''
    This function takes a list of strings (a valid answer) as input
    Then grades the answers based on the answer key
    You can choose to get only the score by setting just_return_score to True
    Otherwise, return the total score, the index of the skipped questions, and the index of the wrong answers
    '''
    # standardize the answer key
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = np.array(answer_key.split(','))

    # remove the N# from the answer to get the answers only
    answer = np.delete(np.array(answer), 0)

    # grade the answers
    # if the answer is correct, the score is 4, otherwise -1
    score = np.where(answer == answer_key, 4, -1)
    # if the answer is empty, change the score from -1 to 0
    score = np.where(answer == '', 0, score)
    
    # if just_return_score is True, return only the total score
    if just_return_score:
        return np.sum(score)
    
    # otherwise, return the total score, the index of the skipped questions, and the index of the wrong answers
    return np.sum(score), np.where(score == 0), np.where(score == -1)

def max_freq (nparr, total_valid_lines):
    '''
    This function takes a numpy array and the total number of valid lines as input
    Then calculates the maximum frequency of the values in the array
    Returns a formatted string with the values that have the maximum frequency, the frequency, and the ratio
    '''

    # +1 to the all the nparr
    # -> nparr becomes an array with index is a number and value is the frequency of that number
    nparr += 1

    # get the maximum frequency
    max_freg = np.bincount(nparr).max()

    # calculate the ratio of the frequency
    ratio = max_freg / total_valid_lines

    # get all the values that have the same maximum frequency
    max_freq_vals = np.array(np.where(np.bincount(nparr) == max_freg)[0], dtype=str)

    # add the frequency and the ratio to each value in all the values in max_freq_vals for right formatting
    add_str = ' - ' + str(max_freg) + ' - ' + str(round(ratio, 3))
    max_freq_vals = np.char.add(max_freq_vals, add_str)

    # format the answer
    formated_answer = ' , '.join(max_freq_vals)
    return formated_answer