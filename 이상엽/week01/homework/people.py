class Person():
    
    def __init__(self, name='', age=0, department=''):
        self.name = name
        self.age = age
        self.department = department
        
    def get_name(self):
        return self.name
    
              
class Professor(Person):
    
    def __init__(self, name='', age=0, department='', position='', laboratory='', student=[]):
        Person.__init__(self, name, age, department)
        self.position = position
        self.laboratory = laboratory
        self.student = student
        
    def print_info(self):
        print ("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도학생은 %s 입니다." %(self.name, self.age, self.department, ', '.join([stu.get_name() for stu in self.student]))) 
        
    def reg_student(self, student):
        self.student.append(student)
        
        
class Student(Person):
    
    def __init__(self, name='', age=0, department='', id=0, GPA=0.0, advisor=Professor()):
        Person.__init__(self, name, age, department)
        self.id = id
        self.GPA = GPA
        self.advisor = advisor
        
    def print_info(self):
        print("'제 이름은 %s, 나이는 %d, 학과는 %s, 지도교수님은 %s 입니다'" %(self.name, self.age, self.department, self.advisor.name))
        
    def reg_advisor(self, advisor):
        self.advisor = advisor
        
def main():
    stu1 = Student('Kim', 30, 'Computer', 20001234, 4.5)
    stu2 = Student('Lee', 22, 'Computer', 20101234, 0.5)
    prof1 = Professor('Lee', 55, 'Computer', 'Full', 'KLE')

    stu1.reg_advisor(prof1)
    stu2.reg_advisor(prof1)
    prof1.reg_student(stu1)
    prof1.reg_student(stu2)

    stu1.print_info()
    stu2.print_info()
    prof1.print_info()
    
    
if __name__ == "__main__":
    main()