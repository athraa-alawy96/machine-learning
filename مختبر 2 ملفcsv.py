import csv
with open ('D:\ABc.csv') as cv:
    f=csv.reader(cv,delimiter=',')
    name=[]
    age=[]
    color=[]
    for row in f:
        print (row)
        name.append(row[2])
        age.append(row[1])
        color.append(row[0])
print(name)        
print(age)
print(color)