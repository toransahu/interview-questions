'''
Created on 23-Oct-2016

@author: toran
'''
import json
import csv
from _io import open


salaryj=open('name_dob_salary.json')
salary_data=json.load(salaryj)
salaryj.close();
heightj=open('name_dob_height.json')
height_data=json.load(heightj)
heightj.close();

 
for i in range(len(salary_data)):
    for j in range(len(height_data)):
        if(salary_data[i]["First_name"]==height_data[j]["First_name"] and salary_data[i]["Last_name"]==height_data[j]["Last_name"] and salary_data[i]["Date_of_birth"]==height_data[j]["Date_of_birth"]):
            salary_data[i][u"Height"]=height_data[j]["Height"]
            

with open("Consolidated.csv", "wb+") as fstream:
    csvwriter = csv.writer(fstream)
    csvwriter.writerow(salary_data[0].keys())
    for rows in salary_data:
        csvwriter.writerow(rows.values())
       

csvreader=csv.reader(open("Consolidated.csv"))

sortedlist = sorted(csvreader, key=lambda row: (row[0], row[1],row[4]), reverse=True)
csvwriter=csv.writer(open("Consolidated.csv", "wb+"))
for row in sortedlist:
    csvwriter.writerow(row)
