import csv
import ast
import linecache

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
                        if row[i] > 2:
                            record[i] = '?'
                        else:
                            record[i] = record[i] + ',' + str(2009 + row[i]) + '-01-01'
                else:
                    continue
                new_list.append(record)

        with open('when_1-2_sem.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # writer.writerow(when_first_row)
            # for row in new_list:
            #     writer.writerow(row)
            for row in new_list:
                for i in range(1, len(row)):
                    if row[i] != '?':
                        csvfile.write(row[0] + "," + first_row[i] + "," + row[i] + "\n")