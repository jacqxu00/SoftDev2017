#William S, Jacqueline X
#Pd. 9 Software Development
#05_occupy_flask_st

from flask import Flask, render_template
import csv
import random

occupations = {}
my_app = Flask(__name__)

#Creates a list of occupations, adding jobs based on their percentages, then chooses one.
def randChoices():
    choices = []
    for occ in occupations:
        weight = occupations[occ]
        while weight > 0:
            choices.append(occ)
            weight = weight - 1
    choice = random.choice(choices)
    return choice

#occupations route for the website. Reads in the csv file.

@my_app.route('/occupations')
def home():
    with open('templates/occupations.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            if (row[0]!='Total'):
                occupations[row[0]] = float(row[1])
        choice = randChoices()
    return render_template('occupation.html', var=occupations, choice=choice)

if __name__ == '__main__':
    my_app.debug == True
    my_app.run()
