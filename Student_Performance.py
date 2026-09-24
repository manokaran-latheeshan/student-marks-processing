""" Given a Student ID: display name, class, subjects, marks, average, 
highest and lowest mark. """
import pandas as pd
from getData import dataExtract

df=dataExtract()

def perfomance(ID,term):
    Name,Class=df.loc[df["StudentID"]==ID , "Name"].iloc[0] , df.loc[df["StudentID"]==ID , "Class"].iloc[0]
    subjects=df.loc[(df["StudentID"]==ID) & (df["Term"]==term) , "Subject"].tolist()
    marks=df.loc[(df["StudentID"]==ID) & (df["Term"]==term) , "Marks"].tolist()
    average=sum(marks)/len(marks)
    high_low=[]
    for sub in subjects:
        high=df.loc[    (df["Term"]==term)  & (df["Subject"]==sub) , "Marks" ].max()
        low=df.loc[ (df["Term"]==term)  & (df["Subject"]==sub) , "Marks" ].min()
        high_low.append(  (high,low)  )

    return subjects,marks,average,high_low,Name,Class



