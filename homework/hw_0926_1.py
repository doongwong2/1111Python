stringX = input()  
stringY = input()  
stringZ = input()  
  
if(stringY in stringX):  
    print("True")  
else:  
    print("False")  
      
print(stringX.find(stringY))  
  
listX = stringX.split(",")  
print(listX)  
  
print("---".join(listX))  
  
print(stringX.startswith(stringY))  
print(stringX.endswith(stringY))  
  
print(stringX.upper())  

listX_up = [i.capitalize() for i in listX]

print(",".join(listX_up))
  
print(stringY.isnumeric())  
  
print(stringX.replace(stringY,stringZ))  
