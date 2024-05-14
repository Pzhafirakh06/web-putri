def up_name(name):
          return name.upper()


names= ["andy","Putri","beny"]
proper_name= []

for name in names:
    proper_name.append(up_name(name))
    print(proper_name)
    
    
print("===MAP===")
proper_name= map(up_name,names)
print(list(proper_name))