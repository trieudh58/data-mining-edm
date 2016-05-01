import csv
import math

with open("cb_predictfile-2.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-2.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-2.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-3.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-3.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-3.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-4.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-4.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-4.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-5.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-5.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-5.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-6.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-6.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-6.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-7.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-7.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-7.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

with open("cb_predictfile-8.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open('combine-8.csv', 'wb') as csvout:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        sum = []
        for i in range(0, 9):
            sum.append(0)

        mae_sum = []
        for i in range(0, 9):
            mae_sum.append(0)

        count = 0
        for row in reader:
            count += 1
            for i in range(1,10):
                alpha = i*0.1
                beta = 1 - alpha
                combine = float(row[3])*alpha + float(row[4])*beta
                sum[i-1] += (combine-float(row[2]))*(combine-float(row[2]))
                mae_sum[i-1] += math.fabs(combine-float(row[2]))
                row.append(combine)
            line = ''
            for i in range(0, len(row)):
                if i != len(row) - 1:
                    line += str(row[i]) + ','
                else:
                    line += str(row[i]) + '\n'
            csvout.write(line)

        with open('rmse-mae-8.csv', 'wb') as csvrmse:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rmse = []
            mae = []
            for i in range(0, len(sum)):
                rmse.append(math.sqrt(sum[i]/count))
                mae.append(mae_sum[i]/count)
            csvrmse.write('RMSE:\n')
            for x in rmse:
                csvrmse.write(str(x) + '\n')
            csvrmse.write('MAE:\n')
            for x in mae:
                csvrmse.write(str(x) + '\n')

