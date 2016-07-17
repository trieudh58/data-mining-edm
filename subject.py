import csv
import ast
import linecache
import random


def subject(subj_index):

    def to_alphabet(dec_score):
        dec_score = float(dec_score)
        if dec_score < 0 or dec_score > 10:
            return 0
            # return 'F'
        elif dec_score < 4.0:
            return 5
            # return 'F'
        elif 4.0 <= dec_score < 5.5:
            return 4
            # return 'D'
        elif 5.5 <= dec_score < 7.0:
            return 3
            # return 'C'
        elif 7.0 <= dec_score < 8.4:
            return 2
            # return 'B'
        else:
            return 1
            # return 'A'

    with open("out_Students_2012.txt", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        # print type(spamreader)
        count = 1
        list_blank_items = []
        list_rows = []
        first_row = []

        for row in reader:
            if(count == 1):
                count = 2
                for i in range(0, len(row)):
                    if row[i] == "" or row[i] == " ":
                        list_blank_items.append(i)  # find blank column
                pop = 0
                for index in list_blank_items:
                    row.pop(index-pop)
                    pop = pop+1
                for i in range(0, 3):
                    row.pop(1)
                    first_row = row
                # list_rows.append(row)
                break
        for row in reader:
            pop = 0
            for index in list_blank_items:
                row.pop(index-pop)
                pop=pop+1
            for i in range(0, 3):
                 row.pop(1)
            for i in range(0, len(row)):
                if row[i] == "" or row[i] == " ":
                    row[i] = '?'
                    continue
                data = row[i].split('-')  # split to array of rates
                row[i] = data[-1]  # get the last rate
                # row[i] = data[0]    #get the 1st grade
                # avg = 0
                # for x in data:
                #     avg += float(x)
                # row[i] = avg/len(data)
            # for x in row[:]:
            #     if x == "?":
            #         row.remove(x)
            list_rows.append(row)
            # print ";".join(row)

        with open('subj_1st_sem.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(first_row)
            for row in list_rows:
                writer.writerow(row)

        with open("out_Students_When.txt", 'rb') as when_csvfile:
            when_reader = csv.reader(when_csvfile, delimiter=';', quotechar='|')
            # print type(spamreader)
            when_count = 1
            when_list_blank_items = []
            when_list_rows = []
            when_first_row = []

            for row in when_reader:
                if (when_count == 1):
                    when_count = 2
                    for i in range(0, len(row)):
                        if row[i] == "" or row[i] == " ":
                            when_list_blank_items.append(i)  # find blank column
                    pop = 0
                    for index in when_list_blank_items:
                        row.pop(index - pop)
                        pop = pop + 1
                    for i in range(0, 3):
                        row.pop(1)
                        when_first_row = row
                    # list_rows.append(row)
                    break
            for row in when_reader:
                pop = 0
                for index in when_list_blank_items:
                    row.pop(index - pop)
                    pop = pop + 1
                for i in range(0, 3):
                    row.pop(1)
                for i in range(0, len(row)):
                    if row[i] == "" or row[i] == " ":
                        row[i] = '?'
                        continue
                    data = row[i].split('-')  # split to array of rates
                    min_year = str(int(data[-1]) - 1)
                    add_sem = 0
                    for x in data:
                        if x.find(min_year) > 0:
                            if x.find('.') > 0:
                                add_sem = x.split('.')[0]

                    tmp = str(row[0])
                    if int(tmp[0]) == 1:
                        start_year = 2000 + int(tmp[0])*10 + int(tmp[1])
                    else:
                        start_year = 2000 + int(tmp[0])
                    sem = int(add_sem) + (int(min_year) - start_year)*2
                    # print(sem)
                    if i != 0:
                        row[i] = sem  # get the last rate
                        continue

                when_list_rows.append(row)
            new_list = []

            for row in when_list_rows:
                for record in list_rows:
                    if record[0] == row[0]:
                        for i in range(1, len(row)):
                            if row[i] > 100 or row[i] == '0':
                                record[i] = '?'
                            else:
                                record[i] = str(row[i]) + "-" + record[i]
                            # else:
                            #     record[i] = record[i] + ',' + str(2009 + row[i]) + '-01-01'
                    else:
                        continue
                    new_list.append(record)

            # with open('all_' + str(first_row[subj_index]) + '_' + str(subj_index) + '.csv', 'wb') as csvfile:
            #     writer = csv.writer(csvfile, delimiter=',',
            #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
            student = []
            for row in new_list:
                # for k in range(1, len(row)):
                #     if row[k] != '?':
                #         row[k] = row[k].split('-')[-1]
                #         if row[k] == '0':
                #             row[k] = '?'
                #         # csvfile.write(row[0] + ',' + str(k) + ',' + str(row[k]) + '\n')
                # # writer.writerow(row)
                if row[subj_index] != '?':
                    student.append(row[0])
                    # csvfile.write(row[0] + '\n')
                else:
                    continue
            random.shuffle(student)
            chunks = []
            fold_size = int(len(student)/10)
            # csvfile.write(str(fold_size) + '\n')
            if fold_size > 1:
                for i in range(0, len(student), fold_size):
                    chunks.append(student[i:i+fold_size])

                count = 0
                if len(student) % 10 != 0:
                    for j in range(0, len(chunks[10])):
                        chunks[count].append(chunks[10][j])
                        count += 1
                    chunks.remove(chunks[10])

                for w in range(0, len(chunks)):
                    with open('ABCDF_SCORE_NO_FOLLOWING/train_' + str(subj_index) + '_fold_' + str(w+1) + '.csv', 'wb') as trainfile:
                        train_writer = csv.writer(trainfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        # train_writer.writerow(chunks[w])
                        with open('ABCDF_SCORE_NO_FOLLOWING/test_' + str(subj_index) + '_fold_' + str(w+1) + '.csv', 'wb') as testfile:
                            test_writer = csv.writer(testfile, delimiter=',',
                                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            for row in new_list:
                                if row[subj_index] != '?' and int(row[subj_index].split('-')[0]) > 1:
                                    if row[0] in chunks[w]:
                                        testfile.write(row[0] + ',' + str(subj_index) + ',' + str(to_alphabet(row[subj_index].split('-')[-1])) + '\n')
                                        for k in range(1, len(row)):
                                            if row[k] == '0':
                                                row[k] = '?'
                                            if row[k] != '?' and k != subj_index:
                                                if int(row[k].split('-')[0]) < int(row[subj_index].split('-')[0]):
                                                    # row[k] = row[k].split('-')[-1]
                                                    trainfile.write(row[0] + ',' + str(k) + ',' + str(row[k].split('-')[-1]) + '\n')
                                                else:
                                                    continue
                                    elif row[0] in student:
                                        for k in range(1, len(row)):
                                            if row[k] == '0':
                                                row[k] = '?'
                                            if row[k] != '?' and int(row[k].split('-')[0]) < int(row[subj_index].split('-')[0]):
                                            # if row[k] != '?':
                                                # row[k] = row[k].split('-')[-1]
                                                trainfile.write(row[0] + ',' + str(k) + ',' + str(to_alphabet(row[k].split('-')[-1])) + '\n')
                                else:
                                    continue

    return


# for i in range(27, 32):
#     subject(i)
# for i in range(40, 66):
#     subject(i)
# for i in range(69, 79):
#     subject(i)

for i in range(1, 79):
    subject(i)

# subject(5)
