import pandas as pd
from getData import dataExtract
from Student_Performance import perfomance
from Subject_Analysis import sub_analysis


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
        print(f"\n{'Subject':<15}{'Marks':>2}{'Highest':>12}{'Lowest':>10}")
        for s,m,(h,l) in zip(subjects,marks,high_low):
            print(f"{s:<15}{m:>2}{h:12}{l:12}")
        print(f"\nAverage : {round(average,2)}\n")

    elif option==str(2):
        sub=input("Enter subject")
        term=input("Enter term")
        no_std,avg,high,low,Pass,failure=sub_analysis(sub,int(term))
        print(roun(avg,2))


    elif option == str(8) : 
        break
    input("Press any key to return")
    

