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
        '''Given a subject: display number of students, average, highest, lowest, 
passes and failures '''
        sub=input("Enter subject\n")
        term=input("Enter term\n")
        no_std,avg,high,low,Pass,fail=sub_analysis(sub,int(term))

        print(f"\n{sub.upper() :<15}{'Term: '}{term}\n")
        print(f"{'No Of Students':<20}{': '}{no_std:<4}\n")
        print(f"{'Average':<20}{': '}{round(avg,4):<5}\n")
        print(f"{'Highest':<20}{': '}{high:<4}\n")
        print(f"{'Lowest':<20}{': '}{low:<4}\n")
        print(f"{'No of Pass':<20}{': '}{Pass:<4}\n")
        print(f"{'No of fail':<20}{': '}{fail:<4}\n")

    elif option==str(3):
        

    elif option == str(8) : 
        break
    input("Press any key to return")
    

