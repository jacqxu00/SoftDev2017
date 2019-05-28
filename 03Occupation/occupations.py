import csv
import random

occupations = {}

with open('occupations.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        if (row[0]!='Total'):
            occupations[row[0]] = float(row[1])

#print occupations
#print len(occupations)

#method 1
def randChoices():
    choices = []
    for occ in occupations:
        reps = occupations[occ]
        while reps > 0:
            choices.append(occ)
            reps = reps - 1
    choice = random.choice(choices)
    return choice

results = {}
for occ in occupations:
    results[occ] = 0
reps = 1000
while reps > 0:
    choice = randChoices()
    for occ in results:
        if choice == occ:
            results[occ] = results[occ] + 1
    reps = reps - 1

print results
    

'''
#method 2

percentiles = {}
sofar = 0
for occ in occupations:
    percentiles[occ] = sofar + (occupations[occ]*10)
    sofar += (occupations[occ]*10)
    
#print percentiles

choose = random.randint(0,998)
for perc in percentiles:
    if (choose <= percentiles[perc] and choose > 0):
        print 'method 2 : ' + perc
        break'''
