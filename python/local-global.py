x = "global"

def foo():
          print("x inside",x)
          
foo()

print(100*"=")
print("Local Scope")

def local_scope():
          text_local  = "Ini Variabel local"
          print(text_local)
          
local_scope()

print(100*"=")
print("Local and Global Scope")

poin = 0

def tambahpoint():
          global poin
          poin+=1
          print(poin)

print (100*"=")
print("Overapping Variabel")

color = "red"
print(color)

def getcolor():
          color ="yellow"
          print('Ini dari fungsi getcolor', color)
          
          getcolor()
          print(color)