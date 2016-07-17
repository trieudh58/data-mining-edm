import csv
import ast
import linecache
from itertools import izip
import math

def ceiling_floor(float_score):
    x = int(float_score)
    if float_score - x >= 0.5:
        return x + 1
    else:
        return x

def rate(input_rate):
    with open("combine_rate_" + str(input_rate) + ".csv", 'w') as res:
        res_reader = csv.reader(res, delimiter=',', quotechar='|')

        def combine(subject, fold):
            try:
                subject = str(subject)
                fold = str(fold)
                with open("ABCDF_PREDICT/CF/alphabet_prediction_all/prediction_" + subject + "_fold_" + fold + ".csv", 'rb') as cf_predict:
                # with open("CF/prediction_all_no_following_sems/prediction_" + subject + "_fold_" + fold + ".csv", 'rb') as cf_predict:
                    cf_reader = csv.reader(cf_predict, delimiter='\t', quotechar='|')
                    RATE = input_rate
                    with open("ABCDF_PREDICT/SVM/predict_all/output_" + subject + "_" + fold, 'rb') as svm_predict:
                    # with open("ABCDF_PREDICT/SVM/predict_no/output_" + subject + "_" + fold, 'rb') as svm_predict:
                        svm_reader = csv.reader(svm_predict, delimiter=';', quotechar='|')
                        with open("ABCDF_SCORE/test_" + subject + "_fold_" + fold + ".csv", 'rb') as test:
                            test_reader = csv.reader(test, delimiter=',', quotechar='|')
                            n = 0
                            sum = 0
                            abs_sum = 0
                            for (cf_row, svm_row, test_row) in izip(cf_predict, svm_predict, test):
                                n += 1
                                cf_score = float(cf_row.split('\t')[-1])
                                svm_score = float(svm_row)
                                test_score = float(test_row.split(',')[-1].strip('\n'))

                                combine_score = RATE * cf_score + (1 - RATE) * svm_score
                                # Ceiling / Floor
                                # combine_score = ceiling_floor(combine_score)

                                sum += (combine_score - test_score) ** 2
                                abs_sum += math.fabs(combine_score - test_score)
                            RMSE = math.sqrt(sum/n)
                            MAE = abs_sum/n
                            # print(RMSE, MAE)
                            res.write(subject + ',' + fold + ',' + str(RMSE) + ',' + str(MAE) + '\n')
                            return str(RMSE) + '-' + str(MAE)
            except Exception:
                pass
        for subject in range(1, 79):
            try:
                rmse_list = []
                mae_list = []
                for fold in range(1, 11):
                    return_str = combine(subject, fold)
                    rmse_list.append(float(return_str.split('-')[0]))
                    mae_list.append(float(return_str.split('-')[-1]))
                avg_rmse = sum(rmse_list)/float(len(rmse_list))
                avg_mae = sum(mae_list)/float(len(mae_list))
                res.write(str(subject) + ',AVERAGE,' + str(avg_rmse) + ',' + str(avg_mae) + '\n')
            except Exception:
                pass

rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for x in rates:
    rate(x)
