import csv
from itertools import izip


def statistic(subject_index):
    label_01 = 0
    label_12 = 0
    label_23 = 0
    label_over3 = 0

    for i in range(1, 11):
        with open('real/all/test_' + str(subject_index) + '_fold_' + str(i) + '.csv', 'rb') as test_csv, open('CF/prediction_all/prediction_' + str(subject_index) + '_fold_' + str(i) + '.csv', 'rb') as pred_csv:
            for test_row, pred_row in izip(test_csv, pred_csv):
                test_score = str(test_row).split(',')[2].replace('\n', '')
                pred_score = str(pred_row).split('\t')[2].replace('\n', '')
                diff = abs(float(test_score) - float(pred_score))

                if 0 <= diff < 1:
                    label_01 += 1
                elif 1 <= diff < 2:
                    label_12 += 1
                elif 2 <= diff < 3:
                    label_23 += 1
                else:
                    label_over3 += 1
    return str(subject_index) + ',' + str(label_01) + ',' + str(label_12) + ',' + str(label_23) + ',' + str(label_over3) + '\n'

with open('statistic/result.csv', 'a') as st_csv:
    st_csv.write('subject,0-1,1-2,2-3,>3\n')
    for i in range(0, 79):
        try:
            st_csv.write(statistic(i))
        except Exception:
            pass
