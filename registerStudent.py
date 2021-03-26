

class Student:
    def __init__(self, UNIQUE_ID, NAME, BATCH_NAME):
        self.UNIQUE_ID = UNIQUE_ID
        self.NAME = NAME
        self.BATCH_NAME = BATCH_NAME
        self.STUDENT_DETAILS=(UNIQUE_ID,NAME,BATCH_NAME)




# YYYY-MM-DT


class batch:
    def __init__(self, Students):
        self.StudentsInfo = dict()
        for currentStudent in Students:
            self.StudentsInfo[currentStudent.UNIQUE_ID] = (currentStudent.NAME, currentStudent.BATCH_NAME)


def getAllStudents():
    f=open('.studentInfo.txt','r')
    dictonary=eval(str(f.read()))
    f.close()
    return dictonary

    pass
ALL_STUDENTS=dict()

try:
    ALL_STUDENTS=dict(getAllStudents())
    print(ALL_STUDENTS)
except:
    pass


def addStudent():
    print('Welcome To Allen Digital')
    name=input("Enter Student's name\n")
    BATCH=input('Enter the BATCH\n')
    Unique_ID=int(input('Enter the form number for the Student (Should be unique)\n'))
    current_student = Student(Unique_ID,name,BATCH)
    ALL_STUDENTS[current_student.UNIQUE_ID]=(current_student.NAME,current_student.BATCH_NAME)
    choice=input('Enter q to exit \n')
    if choice=='q' or choice=='Q':
        f=open('.studentInfo.txt','w')
        f.write(str(ALL_STUDENTS))
        f.close()
    else:
        addStudent()


# tez_student1 = Student(20160829, 'Deepak Kumar Dash', 'TEZ')
# tez_student2 = Student(20160324, 'Krishna Tripathy', 'TEZ')
# tez_student3 = Student(20160823, 'Yash Raj Tripathy', 'TEZ')
# tez_student4 = Student(20162342, 'Dibyadrasta Daxinray', 'TEZ')
# tej_student1 = Student(20160124, 'Bibhupada Pratihari', 'TEJ')
# tej_student2 = Student(20160899, 'Vivekananda Sahu', 'TEJ')
#
# ALL_STUDENTS = [tez_student1, tez_student2, tez_student3, tez_student4,tej_student1,tej_student2]
# ALL_BATCHES = batch(ALL_STUDENTS)
# print(ALL_BATCHES.StudentsInfo)

addStudent()



