String = "My First python program string"
print("The given python string is: " + String)
print("\n")

#   We can access the any value in string
print("This will gives First char from string: " + String[0]) #  it will give first letter, value inside bracket we will call index ,it will starting with 0.
print("\n")

#   Slicing in Strings - if want some range of char from string we will use slcing  -
#   Syntax - Variabl[String_index: ending_index: steps] steps - in range if want skip some sequnce we can skip.
#   In slcing some basic condtions are Starting_index - it will consider, ending_index it will leave
print("The slicing Operation1: " + String[:]) # if we leave blank it will take first and last index
print("The slicing Operation2: " + String[1:5])
print("The slicing Operation3: " + String[1:5:2])
print("The slicing Operation4: " + String[::-1])
print("The slicing Operation5: " + String[::-2])
print("\n")

print("The index of char 'i':  " + str(String.index("i")))
print("The count python string in given string: " + str(String.count("python")))
print("The Find the value My in string: " + str(String.find("M")))
print("Change all char to upper case: " + String.upper())
print("Change all cahr to lower case: "+ String.lower())
#strtswith()
#endswith()
#   Strip, lstrip, rstrip  - is used to remove value which we given inside bracket if don't given any bracket will remove white space
#   split - it is used to split with delimetes
Strip_exp = "  pradeepa  pradeepa  "
print(Strip_exp.strip() )
print(Strip_exp.rstrip() )
print(Strip_exp.lstrip() )

Split_exp = "rpadeepa, pradeepna, pradeepa"
print(Split_exp.split(","))
Split_exp = "rpadeepa- pradeepna- pradeepa"
print(Split_exp.split("-"))

Join_exp = "pradeepa how are"
print("-".join(Join_exp.split()))
