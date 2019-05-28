'''
Jackie Xu and William Soe
SoftDev Pd9
HW10 Select
10.18.2017
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="school.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#create courses table

ids = [] # create list of all ids
scores = {} #create dictionary for all scores per person, KEY = person, VALUE = list of scores
names = {} #create dictionary of all names and associated ids, KEY = name, VALUE = id

#Only run once
def create_avg_table():
    c.execute("CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average INTEGER)")
 
#Returns all scores for an id
def get_score(id):
    return scores[id]

#Returns a student's average
def get_average(id):
    sum = 0
    divide_by = 0
    for grade in scores[id]:
        sum = sum + grade
        divide_by = divide_by + 1
    return sum/divide_by
       
#Creates the data structures 
def create_data():
    del ids[:]
    scores.clear()
    names.clear()
    
    all_ids = c.execute("SELECT id FROM peeps;") #pulls all student ids
    for person in all_ids:
        #add each id to a list of ids
        ids.append(person[0])
    
    for each in ids:
        #for each id in the ids list, scores[id] = a list of marks
        grades = c.execute("SELECT mark FROM courses WHERE id = %d;" %each)
        marks = []
        for course in grades:
            marks.append(course[0])
        scores[each] = marks
        
    #Create a dictionary with names and id keys
    peeps = c.execute("SELECT name, id FROM peeps;")
    for peep in peeps:
        names[peep[0]] = peep[1]
        
    
#To display names, ids, and avgs
def print_avg():
    for name in names:
        print "%s (%s) has an average of %s" %(name,names[name],get_average(names[name]))

#peeps_avg table creation
def insert_table():
    for id in ids:
        c.execute('INSERT INTO peeps_avg VALUES('+str(id)+','+str(get_average(id))+');')        
def update_average(student_id,avg):
    command = "UPDATE peeps_avg SET average = %d WHERE id = %d" % (average, student_id)
    c.execute(command)
    db.commit()
        
def add_record(code,id,mark):
    command = 'INSERT INTO courses VALUES (%s,%d, %d)' %(code,int(id),int(mark))
    c.execute(command)
    db.commit()
        
'''
#update the table with new info   
def update_rows():
    #find out length of courses table
    courses = c.execute("SELECT mark FROM courses")
    num_entries = 0
    for entry in courses:
        num_entries += 1
    
    #find length of csv file 
    with open('courses.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_entries = 0
        for row in reader:
            csv_entries += 1
    
        #if csv file is longer than courses table, then update
        i = 0
        while (i <= csv_entries):
            if i <= num_entries:
                reader.next()
                i += 1
            else:
                c.execute('INSERT INTO courses VALUES("%s", %d, %d);' %(to_add['code'],to_add['mark'],to_add['id']))

def update_avgs():
    create_data()
    for each in names:
        new_avg = get_average(names[each])
        c.execute('UPDATE peeps_avg SET average = %d WHERE id = %d' %(new_avg, names[each]))

'''        
def main():
    create_avg_table()
    create_data()
    insert_table()
    print_avg()
    update_avg(1,85)
    print_avg()
    
main()
'''   
#==========================================================
db.commit() #save changes
db.close()  #close database
