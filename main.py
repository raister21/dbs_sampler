import random
import time
import random_date
import listcleaner


f = open('strings/names')
names = f.readlines()
names = listcleaner.cleaner(names)

f = open('strings/last_names')
last_names = f.readlines()
last_names = listcleaner.cleaner(last_names)

f = open('strings/addresses')
addresses = f.readlines()
addresses = listcleaner.cleaner(addresses)

f = open('strings/blood_groups')
bg = f.readlines()
bg = listcleaner.cleaner(bg)

f = open('strings/certified')
certified = f.readlines()
certified = listcleaner.cleaner(certified)

f = open('strings/job')
job = f.readlines()
job = listcleaner.cleaner(job)

f = open('strings/Medicines')
medicine = f.readlines()
medicine = listcleaner.cleaner(medicine)
not_chosen = medicine
chosen_med=[]

f = open('strings/treatments')
treatment = f.readlines()
treatment = listcleaner.cleaner(treatment)
not_chosen_t = treatment
chosen_t=[]

f = open('strings/departments')
department = f.readlines()
department = listcleaner.cleaner(department)
not_chosen_d = department
chosen_d = []

f = open('strings/department_type')
department_type = f.readlines()
department_type = listcleaner.cleaner(department_type)


serialnum = 1
phone = 981999999




def mkstaff(tablename,rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global serialnum
    global phone
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(serialnum) + ', ')
        w.write("'" + names[random.randrange(len(names))] + "', ")
        w.write("'" +last_names[random.randrange(len(last_names))]+ "', ")
        w.write("'" + str(random_date.random_date("1/1/1980", "1/1/2009", random.random())) + "'" + ', ')
        w.write("'" + job[random.randrange(len(job))]+"', ")
        w.write("'" + addresses[random.randrange(len(addresses))] + "', ")
        w.write(str(phone) + ', ') 
        w.write("'" + certified[random.randrange(len(certified))]+"', ")
        w.write(str(random.randrange(0,5)) + ',')
        w.write(str(random.randrange(10,80)*1000) + ',')
        w.write(str(random.randint(0,12)))
        w.write(');\n')
        serialnum +=1 
        phone -= 1

def mkpatient(tablename, rows, no_null):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    number_null = no_null
    w = open(tblsql,'w')
    global serialnum
    global phone
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(serialnum) + ', ')
        if i > no_null-1:
            w.write(str(random.randrange(1, staff_end-1)) + ',')
        else:
            w.write("'" + 'NULL'+ "',")
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

def mkbilling(tablename, rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global serialnum
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(serialnum) + ', ')
        w.write("'" + str(random_date.random_date("1/1/2000", "1/1/2019", random.random())) + "'" + ', ')
        w.write(str(random.randrange(staff_end, patient_end)) + ',')
        w.write(str(random.randrange(0,10)*100))
        w.write(');\n')
        serialnum +=1 

def mkmedicine_batch(tablename, rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global chosen_med
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        input_med = medicine[random.randrange(len(not_chosen))]
        w.write("'" + str(input_med) + "', ")
        not_chosen.remove(input_med)
        chosen_med.append(input_med)
        w.write("'" + str(random_date.random_date("1/1/2019", "1/1/2025", random.random())) + "'")
        w.write(');\n')

def mkmedicine_bill(tablename, rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(random.randrange(staff_end, patient_end)) + ',')
        w.write("'" + str(chosen_med[random.randrange(len(chosen_med))]) + "', ")
        w.write(str(random.randint(0,9)*100))
        w.write(');\n')


def mktreatment(tablename, rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global chosen_t
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        input_t = not_chosen_t[random.randrange(len(not_chosen_t))]
        w.write("'" + str(input_t) + "', ")
        not_chosen_t.remove(input_t)
        chosen_t.append(input_t)
        w.write(str(random.randint(0,8)*125))
        w.write(');\n')

def mkdepartment(tablename,rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global phone
    global chosen_d
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        input_d = not_chosen_d[random.randrange(len(not_chosen_d))]
        w.write("'" + str(input_d) + "', ")
        not_chosen_d.remove(input_d)
        chosen_d.append(input_d)
        w.write("'" + str(department_type[random.randrange(len(department_type))]) + "', ")
        w.write(str(phone))
        w.write(');\n')
        phone -=1

def mkappointment(tablename,rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global serialnum
    global chosen_d
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(serialnum) + ", ")
        w.write(str(random.randrange(1, staff_end)) + ", ")
        w.write(str(random.randrange(staff_end, patient_end))+", ")
        w.write(str("'" + chosen_d[random.randrange(len(chosen_d))]) + "', ")
        w.write("'" + str(random_date.random_date("1/1/2017", "1/1/2019", random.random())) + "'" + ', ')
        w.write(str(random.randint(1,13)*125))
        w.write(');\n')
           

def mkappointmentitem(tablename, rows):
    tblsql = str("/'sqlfiles/"+tablename + ".sql")
    w = open(tblsql,'w')
    global serialnum
    global chosen_t
    for i in range(rows):
        w.write('INSERT INTO ' + tablename + ' VALUES (\n')
        w.write(str(random.randrange(billing_end, Appointment_end)) + ", ")
        w.write("'"+ str(chosen_t[random.randrange(len(chosen_t))])+ "'")
        w.write(');\n')

print("Staff")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkstaff(tablename,rows)
print('\n')

staff_end = serialnum + rows -1

print("Patient")
rows = int(input(" Rows "))
no_null = int(input("number of patients who are only patient"))
tablename = input(" DBS TABLE name ")
mkpatient(tablename,rows,no_null)
print('\n')
patient_end = staff_end + rows

print("Billing")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkbilling(tablename, rows)
print('\n')
billing_end = patient_end + rows

print("Medicine Batch")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkmedicine_batch(tablename, rows)
print('\n')
print("Medicine Bill")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkmedicine_bill(tablename, rows)
print('\n')

print("Treatment")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mktreatment(tablename, rows)
print('\n')

print("Department")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkdepartment(tablename, rows)
print('\n')
print("Appointment")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkappointment(tablename, rows)
print('\n')
Appointment_end = billing_end + rows

print("appointed items")
rows = int(input(" Rows "))
tablename = input(" DBS TABLE name ")
mkappointmentitem(tablename, rows)
print('\n')