import numpy as np

def is_valid_line(line, print_noti = True):
    if len(line) != 26:
        if print_noti:
            print('Invalid line of data: does not contain exactly 26 values')
            print(','.join(line))
            print()
        return False
    elif not line[0].startswith('N'):
        if print_noti:
            print('Invalid line of data: N# is invalid')
            print(','.join(line))
            print()
        return False
    elif not line[0][1:].isdecimal() or len(line[0][1:]) != 8:
        if print_noti:
            print('Invalid line of data: N# is invalid')
            print(','.join(line))
            print()
        return False
    return True

def grade (answer):
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = np.array(answer_key.split(','))
    answer = np.delete(np.array(answer), 0)

    score = np.where(answer == answer_key, 4, -1)
    score = np.where(answer == '', 0, score)
    
    return np.sum(score), np.where(score == 0), np.where(score == -1)

def max_freq (nparr, total_valid_lines):
    nparr += 1
    max_freg = np.bincount(nparr).max()
    ratio = max_freg / total_valid_lines
    max_freq_vals = np.array(np.where(np.bincount(nparr) == max_freg)[0], dtype=str)
    add_str = ' - ' + str(max_freg) + ' - ' + str(round(ratio, 3))
    max_freq_vals = np.char.add(max_freq_vals, add_str)

    formated_answer = ' , '.join(max_freq_vals)
    return formated_answer