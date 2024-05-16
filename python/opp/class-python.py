class Animal:
       def   __init__(self,name,color) :
                self.name = name
                self.color = color
                
       def   eat(self,food):
           print(f"{self.name}with {self.color}color eating{food}")
                  
       def  makeSound(self, sound):
         print(f"{self.name} is making {sound}")


obj1 = Animal("Cat", "Yellow")
obj1.eat("fish")
obj1.makeSound("Miowing")

obj2 = Animal("Panda", "BlackWhite")
obj2.eat("Bamboo")
obj2.makeSound("uwoohcchh")

obj3= Animal("Merpati","Coklat")
obj3.eat("Jagung")
obj3.makeSound("krukkrukk")