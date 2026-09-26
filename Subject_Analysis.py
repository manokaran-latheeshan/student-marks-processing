'''Given a subject: display number of students, average, highest, lowest, 
passes and failures '''

import pandas as pd
from getData import dataExtract


def sub_analysis(sub,term):
    df=dataExtract()
    marks=df.loc[(df["Subject"].str.lower()==sub.lower()) & (df["Term"]==term) , "Marks"].tolist()
    no_std=len(marks)
    high,low=max(marks),min(marks)
    avg=sum(marks)/len(marks)
    Pass,failure=0,0
    for mark in marks:
        if mark>=50:
            Pass+=1
        else:
            failure+=1
    return no_std,avg,high,low,Pass,failure
