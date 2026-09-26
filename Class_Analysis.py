'''Given a class: calculate number of students, class average and 
students passing all subjects.'''

import pandas as pd
from getData import dataExtract
from Student_Performance import perfomance

def class_analysis(cls,term):
    df=dataExtract()
    std_ids=set(df.loc[  (df["Class"]==cls) & ( df["Term"]==term),"StudentID"])
    no_std=len(std_ids)
    total=0
    allPass=0
    for std_id in std_ids:
        marks=perfomance(std_id,term)[1]
        total += sum(marks)
        for mark in marks:
            if mark>50:
                continue
            else:
                break
        else:
            allPass+=1
        average= total/(no_std*len(marks))

    return average , allPass , no_std

