import random
import time
import random_date

f = open('names')
names = f.readlines()

f = open('last_names')
last_names = f.readlines()

f = open('addresses')
addresses = f.readlines()

f = open('blood_groups')
bg = f.readlines() 

date_r = str(random_date.random_date("1/1/1980", "1/1/2009", random.random()))

serialnum = 0
phone = 981999999



def mkstaff(tablename,rows):
    tblsql = str(tablename + '.sql')
    w = open(tblsql,'w')
    global serialnum
    global phone
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + 'VALUES (\n')
        w.write(str(serialnum) + ',' + names[random.randrange(len(names))] + ','+last_names[random.randrange(len(last_names))] + ',')
        w.write(date_r + ',' + addresses[random.randrange(len(addresses))] + ',')
        w.write(names[random.randrange(len(names))] + last_names[random.randrange(len(last_names))] + ',')
        w.write(bg[random.randrange(len(bg))] + ','+str(phone) + ',' + str(random.randrange(0,5)))
        w.write('\n );')
        serialnum +=1 
        phone -= 1

rows = int(input("rows"))
tablename = input("Table name")

mkstaff(tablename,rows)
print('Done')

#names[random.randrange(len(names))] + last_names[random.randrange(len(last_names))] 