#extract data from csv and make a DataFrame
import pandas as pd
def dataExtract():
    df=pd.read_csv("student_data.csv")
    return df