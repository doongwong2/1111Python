import re

counter = 0
inputStr = input()

listNum = re.split(r"[a-z,]",inputStr)
print(listNum)

listNum = list(dict.fromkeys(listNum))
#print(listNum)


if("" in listNum):
    listNum.remove("")

print(listNum)

for i in listNum:
    if i.isdecimal():
        counter += 1
    elif float(i):
        counter += 1
        
#print(listNum,counter)
print(counter)
