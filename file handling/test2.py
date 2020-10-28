# Create a Class ‘FileOperation’ with member functions: ‘save’ that performs file write operation and ‘read’ that performs file read operation.  
# Create Student and Employee and initialize relevant data of those classes. 
# Write information of student and employee in separate file (i.e. ‘StudentRecord.txt’ and ‘EmployeeRecord.txt’). 
# Later retrieve those information and display in console.
from tabulate import tabulate

class Student():
    def __init__(self,studentId,studentName):
        self.__studentID = studentId
        self.__studentName = studentName
    
    def getStudentName(self):
        return self.__studentName
    
    def getStudentID(self):
        return self.__studentID          


class Employee():
    def __init__(self,employeeID,employeeName,employeeDepartment):
        self.__employeeName=employeeName
        self.__employeeID=employeeID
        self.__employeeDepartment=employeeDepartment

    def getEmployeeName(self):
        return self.__employeeName

    def getEmployeeID(self):
        return self.__employeeID        

    def getEmployeeDepartment(self):
        return self.__employeeDepartment        




class FileOperation:
    def __init__(self,db_name):
        self._db_name = db_name

    def read(self,object_type):
        if(object_type == 'employee'):
            content = []
            with open(self._db_name,'r') as f:
                content = f.readlines()
            content = [x.strip() for x in content] 
            for employee in content:
                b = employee.split(",")
                message = [
                    ["employee ID" , b[1]], 
                    ["employee Name " , b[0]],
                    ["employee Department" ,b[2]],
                ]
                print(tabulate(message))
        else:
            content = []
            with open(self._db_name,'r') as f:
                content = f.readlines()
            content = [x.strip() for x in content] 
            for student in content:
                b = student.split(",")
                message = [
                    ["student ID" , b[0]], 
                    ["student Name " , b[1]],
                ]
                print(tabulate(message))
        
        
    def write(self,obj,object_type):
        if(object_type == 'employee'):
            employeeName= obj.getEmployeeName()
            employeeID = obj.getEmployeeID()
            employeeDepartment=obj.getEmployeeDepartment()
            with open(self._db_name,'a') as f:
                t = f"{employeeID},{employeeName},{employeeDepartment}\n"
                f.write(t)
        else:
            studentName= obj.getStudentName()
            studentID = obj.getStudentID()
            with open(self._db_name,'a') as f:
                t = f"{studentID},{studentName}\n"
                f.write(t)

def main():
    while(True):

    
        user_input = str(input("do u want to enter employee or students records?  e/s"))
        if user_input == "s":


            student_Name = str(input("enter student name:"))
            student_ID = int(input("enter student ID:"))
            student1 = Student(student_Name,student_ID)
            studentFileOperation = FileOperation("studentRecord.txt")
            studentFileOperation.write(student1,"student")
            studentFileOperation.read("student")
        
        elif user_input=="e":
            employee_name = str(input("enter employee name:"))
            employee_ID = int(input("enter employee ID:"))
            employee_Department = str(input("enter employee Department:"))
            employee1 = Employee(employee_name,employee_ID,employee_Department)
            employeeFileOperation = FileOperation("employeeRecord.txt")
            employeeFileOperation.write(employee1,"employee")
            employeeFileOperation.read("employee")
        else: print (" please enter again") 
        
        quit_program = str(input("enter q if u want to quit"))
        if (quit_program == "q"):
            break
        else:
            continue   

if __name__ =="__main__":
    main()    