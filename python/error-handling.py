student = {
          "name": "Akhtar",
          "Age": 15
}

#print(student)

try :
       print(student)
except NameError:
           print("Name is not defined")
except:
          print("An error occured!")
else:
          print("Code Success")
finally:
          print("Done")

print("code selanjutnya")


print ("I like Python App")
print(50*"=")

loop = int(input("Enter number loop:"))

if loop <= 2: 
   raise Exception ('Number must be >2')
else:
   for i  in range (loop):
     print ("I like Python")