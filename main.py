import random
import time
import random_date
import listcleaner

f = open('names')
names = f.readlines()
names = listcleaner.cleaner(names)

f = open('last_names')
last_names = f.readlines()
last_names = listcleaner.cleaner(last_names)

f = open('addresses')
addresses = f.readlines()
addresses = listcleaner.cleaner(addresses)

f = open('blood_groups')
bg = f.readlines()
bg = listcleaner.cleaner(bg)
 
serialnum = 1
phone = 981999999



def mkstaff(tablename,rows):
    tblsql = str(tablename + '.sql')
    w = open(tblsql,'w')
    global serialnum
    global phone
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(serialnum) + ', ')
        w.write("'" + names[random.randrange(len(names))] + "', ")
        w.write("'" +last_names[random.randrange(len(last_names))]+ "', ")
        w.write("'" + str(random_date.random_date("1/1/1980", "1/1/2009", random.random())) + "'" + ', ')
        w.write("'" + addresses[random.randrange(len(addresses))] + "', ")
        w.write("'" + names[random.randrange(len(names))] + " " + last_names[random.randrange(len(last_names))] + "', ")
        w.write("'" + bg[random.randrange(len(bg))] + "', ")
        w.write(str(phone) + ', ') 
        w.write(str(random.randrange(0,5)))
        w.write(');\n')
        serialnum +=1 
        phone -= 1


rows = int(input("rows"))
tablename = input("Table name")

mkstaff(tablename,rows)



