f = open("sample.txt" , "r") # file object 

data = f.read()

print(type(data)) 
print(data)

f = open("sample.txt" , "w") # file object 
f.write("Text to the overwrite \n the complete data.")



f.close()
