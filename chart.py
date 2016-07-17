import csv
from itertools import izip


def build_chart():
    with open('out_Students_2012.csv', 'rb') as score_csv, open('out_Students_When.csv', 'rb') as when_csv:
        header = []
        i = 0
        for score_row, when_row in izip(score_csv, when_csv):
            if i == 0:
                i += 1
                header = score_row.strip('\n').split(';')
                for i in range(4, len(header)):
                    with open('charts/chart_' + str(i - 3) + '.csv', 'a') as out_csv:
                        out_csv.write('Semester,Score,Score Range\n')
            else:
                score_arr = score_row.strip('\n').split(';')
                when_arr = when_row.strip('\n').split(';')
                for i in range(4, len(header)):
                    with open('charts/chart_' + str(i-3) + '.csv', 'a') as out_csv:
                        try:
                            if score_arr[i] != '' and score_arr[i] != ' ' and when_arr[i] != '' and when_arr[i] != ' ':
                                when_parse = when_arr[i].split('-')
                                # print(when_parse)
                                for idx in range(0, len(when_parse) - 1):
                                    if '.' in when_parse[idx]:
                                        when_parse[idx] += '-' + when_parse[idx+1]
                                for x in when_parse:
                                    if '.' not in x:
                                        when_parse.remove(x)
                                score_parse = score_arr[i].split('-')
                                for idx in range(0, len(score_parse)):
                                    # print(when_parse[idx], score_parse[idx])
                                    score_range = ''
                                    if 0 <= float(score_parse[idx]) < 5:
                                        score_range = '0to5'
                                    elif 5 <= float(score_parse[idx]) < 8:
                                        score_range = '5to8'
                                    elif 8 <= float(score_parse[idx]) <= 10:
                                        score_range = '8to10'
                                    out_csv.write(when_parse[idx] + ',' + score_parse[idx] + ',' + score_range + '\n')
                            else:
                                continue
                        except Exception:
                            pass

build_chart()
