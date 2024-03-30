str = input()

listNum = str.split(",")
#print(listNum)

listNum.sort()
for i in listNum:
    print(i)
    
listNum.sort(reverse = True)
for i in listNum:
    print(i)
    
setNum = set(listNum)
#print(setNum)

listNum = list(setNum)
#print(listNum)

listNum.sort(reverse = True)
#print(listNum)

for i in listNum:
    print(i)
