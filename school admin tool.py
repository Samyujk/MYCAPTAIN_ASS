import csv

def wcsv(info):
    with open('studinfo.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["NAME","AGE","CONTACT NUMBER","EMAIL ID"])

        writer.writerow(info)


if __name__=='__main__':
    condition=True
    studnum=1

while(condition):
    studinfo=input("Enter student's information for student %d in the following format (NAME AGE CONTACT_NUMBER E-MAIL ID): "%(studnum))

    info=studinfo.split(' ')
    print("\nEntered information:\nNAME:{}\nAGE:{}\nCONTACT_NUMBER:{}\nE-MAIL ID:{}".format(info[0],info[1],info[2],info[3]))

    check=input("Is the entered information correct? (yes/no): ")

    if check=="yes":
        wcsv(info)

        condition_check=input("Enter (yes/no) if you want to enter information of another student: ")

        if condition_check=="yes":
            condition=True
            studnum+=1
        elif condition_check=="no":
            condition=False
            
    elif check=="no":
        print("\nPlease re-enter the values!")

    

        
