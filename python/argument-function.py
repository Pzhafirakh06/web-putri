def addtion (a,b):
    add = a + b
    print(add)
    
addtion(21,10)
addtion(12,10)

print("==Arbitraty Argument==")

def  tambah (*numbers):
          result = 0
          for num in numbers:
                    result += num
          return(result)
          
add1= tambah (3,2,5,7,8,9)
print(add1)

add2  = tambah (10,32,54)
print(add2)

print("==Keyword Argument==")

def fullname(fname , lname):
 print(fname , lname)
    
fullname (fname="Zhafira", lname="Putri")

print("==Arbitrary Keyword Argument==")

def namaLengkap(**fullname):
      result = fullname.values()
      print(".".join (result))
      
namaLengkap(
          fname="Putri",
          mname="Zhafira",
          lname="Khairani",
          )

print("==Default Value Argument==")

def SayHello(name,message="Helo"):
      print(message, name)

SayHello("Assamualaikum")