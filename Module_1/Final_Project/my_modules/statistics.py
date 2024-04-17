import numpy as np
from my_modules.data_handle import is_valid_line, grade, max_freq

def valid_st (df):
    total_valid = 0
    total_invalid = 0
    print()
    print('**** ANALYZING ****')
    print()
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
    scores = np.array([], dtype=int)
    skips = np.array([], dtype=int)
    incorrects = np.array([], dtype=int)
    total_valid_lines = 0
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