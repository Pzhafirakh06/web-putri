class Person:
       def __init__(self,name) :
         self.name = name

       def getInfo(self):
             print(f"This person's name {self.name}")

class Student(Person):
        def  __init__(self, Name,nis):
              super().__init__(Name)
              self.nis = nis

        def  study (self,subject):
                 print(f"{self.name}NIS : {self.nis} is studying {subject}")
       
person1= Person ("Putri")
person1.getInfo()

student1 = Student ("Zhafirah","2202124")
student1.getInfo()
student1.study("Sosiologi")

student2 = Student("Putri", "22020001")
student1.getInfo()
student2.study("Bisnis Digital")
