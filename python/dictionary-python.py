student1 ={
          "name" : "Azrul",
          "Age" : 20,
          "Address": "Kendari"
}

print(student1)
print(type(student1))

print(student1.keys())
print(student1["Address"])

# add  new item
student1["grade"]=12
student1["Gender"] ="Male"
print(student1)

# ubah value
student1["Age"]  = 17
print(student1)

student1.update({'email':'azrul@gmail.com'})
print(student1)

student1.pop('Gender')
print(student1)

student1.popitem()
print(student1)