import ast
  
input0 = input()  
inputDict = ast.literal_eval(input0)  
print(len(inputDict))  
search0 = int(input())  
if search0 in inputDict:  
    print("True")  
else:  
    print("False")
    
    
search1 = int(input())  
if search1 in inputDict:  
    if inputDict[search1] == 0:  
        print("True")  
    else:  
        print("False")  
else:  
    print("Notexisting")  

input1 = input()  
inputTuple = ast.literal_eval(input1)  
inputDict[inputTuple[0]] = inputTuple[1]  

list0 = list(inputDict.keys())  
list0.sort()  
for i in list0: print(i)  

list1 = list(inputDict.values())  
list1.sort()  
for i in list1: print(i)  

list2 = list(inputDict.items())  
list2.sort()  
tuple0 = tuple(list2)  
for i in tuple0:print(i)