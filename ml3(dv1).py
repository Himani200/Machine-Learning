#!usr/bin/python3


import matplotlib.pyplot as plt
import csv
import pandas as pd

row=[['Student_name','Marks','Age','Contact','Study_hours'],
     ['Himani','95','19','978433981','4'],
     ['Kush','80','18','7765901209','6'],
     ['Nikita','89','19','9571895500','5'],
     ['Himanshu','55','20','8907556712','2']]

with open('student.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(row)
csvFile.close()

df = pd.read_csv('/home/hagarwal/Desktop/ML/student.csv')
Marks_obt=df["Marks"]
Name=df["Student_name"]
print(df)
plt.pie(Marks_obt,labels=Name,autopct='%1.1f%%',shadow=True)
plt.title("Marks obtained by the following students")
plt.show()
