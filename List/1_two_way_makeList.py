#  make  a list 

print("List  Are  changable  \n orederd \n allow duplicate  value")

name = ["car" ,"i " ,"am", "posotive", "man"]
print(f"List :-{name} \n Type Fun :- {type(name)} ")

#  make a list using  constructor 

car  =list(("you", "are", "very","nice", "person"))
print(car)
print (type(car))

#  list insert()
car.insert(2,"dada")
print(car)

car. insert(-1,"are")
print(car)

car.insert(123 ,"tt")
print(car)


#  len ()
print(len(car))

# Access  the data  using index 
print(car[5])

# append()  tack  onlu one  arg
car.append("Dada")
print(car)

# try to add  two  or more item in append()
# car.append("dad ")  #   TypeError: list.append() takes exactly one argument (2 given)    
# print(car)

# extends()  aek thi vadhu item's
car.extend("hu")
print(car)










