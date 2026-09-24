""" Given a Student ID: display name, class, subjects, marks, average, 
highest and lowest mark. """
import pandas as pd
from getData import dataExtract

df=dataExtract()

def Name_Class(ID):
    Name,Class=df.loc[df["StudentID"]==ID , "Name"].iloc[0] , df.loc[df["StudentID"]==ID , "Class"].iloc[0]
    return Name,Class

n,c=Name_Class("S001")
print(n)