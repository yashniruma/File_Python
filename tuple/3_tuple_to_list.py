#  Tuple  Converted In List

happy_typle =("dada", "mox", 111, 12,45)
print(f"{happy_typle} \t type :- {type(happy_typle)}")

print("*************************************************8")
happy_list =list(happy_typle)
print(f"{happy_list} \t type :- {type(happy_list)}")

# add a  value  in list  than   again convert list  to tuple 
happy_list.insert(4,"you are very  positve person")
print(f"{happy_list} \t type :- {type(happy_list)}")

#   list  to  tuple

change_tuple = tuple(happy_list)
print(f"{change_tuple} \t type :- {type(change_tuple)}")



