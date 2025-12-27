class Student:
    def __init__(self,idno,name,branch,marks):
          self.idno=idno
          self.name=name
          self.branch=branch
          self.marks=marks
    def percentage(self):
        total=sum(self.marks)
        return total/len(self.marks)
    def grade(self):
        a=self.percentage()
        if(a>=90):
             print("Ex")
        elif(a<90 and a>=80):
             print("A")
        elif(a<80 and a>=70):
             print("B")
        elif(a<70 and a>=60):
             print("C")
        elif(a<60 and a>=50):
              print("D")
        elif(a<50 and a>=40):
              print("E")
        else:
              print("REMIDIAL")
    def display(self):
        print("ID:",self.idno)
        print("Name:",self.name)
        print("branch",self.branch)
        print("percentage:",self.percentage())
        print("grade:",self.grade())
s1=Student(101,"sruthi","cse",[90,96,80])
s2=Student(102,"Aswini","cse",[97,96,80])
s3=Student(103,"rushitha","cse",[99,70,80])
s1.display()
s2.display()
s3.display()

        