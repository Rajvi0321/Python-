# SCHOOL ADMINISTRATION PROGRAM PROJECT
import csv

# FOR CSV FILE
def add_into_csv(info_list):
    with open('student_profile.csv','a',newline='') as file:     
        w=csv.writer(file)
        if file.tell()==0:                                    
            w.writerow(['Name','Admission no','class','dob'])  
        w.writerow(info_list)
        
#FETCHING THE INFORMATION OF THE STUDENT
def takes_info():
    while True:
        info=input('Enter infomation in following format(Name, Admission_no, Class, DOB): ')
        info_list=info.split(' ')                           
        print('Info entered is- \nName: {} \nAdmission no: {} \nClass: {} \ndob:{}'.format(info_list[0],info_list[1],info_list[2],info_list[3]))       
        ch=input('Is the infomation correct[Y/N]: ')              
        if ch=='y':
            add_into_csv(info_list)                         
            print('Info added')
            break
        else:
            continue                                        
print('School Administration Program\n')
takes_info()
ch=input('Want to add more students? [Y/N]: ')                       
if ch=='y':
    takes_info()