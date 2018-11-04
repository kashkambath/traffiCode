import csv
import os
from datetime import datetime
    
def join_csv(dir):
    ls = []
    count = 0
    for file in os.listdir(dir):
        if(file.split('.')[-1] != 'csv'):
            continue
        f = open(dir + '/' + file, errors='replace')
        your_list = list(csv.reader(x.replace('\0', '') for x in f))
        header = your_list[0]
        rest = your_list[1:]
        var = True
        if(count != 0):
            if(len(header) != len(ls[0])):
                print(len(header), len(ls[0]), header, ls[0])
                print("Failed on %s" % file)
                var = False
                continue
            i = 0
            for i in range(len(header)):
                if(header[i] != ls[0][i]):
                    print("Failed on %s on column %d" % (file, i))
                    var = False
                    break
        else:
            print(len(your_list))
            print(len(your_list[0]))
            ls.append(header)
        if(var):
            for r in rest:
                ls.append(r)
        count += 1

    with open('output.csv', 'w') as g:
        writer = csv.writer(g, lineterminator="\n")
        writer.writerows(ls)
    g.close()
    return ls

def date_time(file):
    f = open(file, errors='replace')
    ls = list(csv.reader(f))
    i = 0
    for row in ls[1:]:
        date = row[3]
        time = row[4]
        time = "%04d" % int(row[4])
        dt = "%s %s" % (date, time)
        dt = datetime.strptime(dt, "%m/%d/%y %H%M")
        row.insert(5, dt)
    ls[0].insert(5, 'COLLISION_DATE')
    with open('edit_cleaned.csv', 'w') as g:
        writer = csv.writer(g, lineterminator="\n")
        writer.writerows(ls)

date_time('cleaned.csv')
#join_csv('./csv')

