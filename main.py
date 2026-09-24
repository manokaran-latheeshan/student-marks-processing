import pandas as pd
from getData import dataExtract
from Student_Performance import perfomance


while True:
    print("===========================")
    print("         M E N U")
    print("===========================")

    print(f"1. Student Performance\n2. Subject Analysis\n3. Class Analysis\n4. Top 5 Students\n5. At-Risk Students\n6. Subject Difficulty\n7. Search\n8. Exit")
    
    print("Choose one of the above (ex: 4)")
    option=input("Enter here...\n")

    if option==str(1):
        ID=input("Enter student ID\n").upper()
        term=int(input("Enter Term\n"))
        df=dataExtract()
        subjects,marks,average,high_low,Name,Class=perfomance(ID,term)
        
        print(f"\nStudent ID: {ID}\nStudent Name: {Name}")
        print(f"Subject   || Marks  || Highest || Lowest")

        
    elif option == str(8) : 
        break
    input("Press any key to return")
    

