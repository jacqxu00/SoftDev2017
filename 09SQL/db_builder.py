'''
Jackie Xu
SoftDev Pd9
HW09 SQLite
10.14.2017
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="school.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#create courses table
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = 'INSERT INTO courses VALUES("'+str(row["code"])+'",'+str(row['mark'])+","+str(row['id'])+");"
        c.execute(command)
            
#create people table
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = 'INSERT INTO peeps VALUES("'+str(row["name"])+'",'+str(row['age'])+","+str(row['id'])+");"
        c.execute(command)
    
#==========================================================
db.commit() #save changes
db.close()  #close database
