str = input()  
str1 = input()  
wid = input()  
pad = input()  
  
print('{:{align}{width}}'.format(str ,align='>' ,width = wid))  
  
print('{:{align}{width}}'.format(str1 ,align='<' ,width = wid))  
  
print('{:{padding}{align}{width}}'.format(str , padding = pad ,align='^' ,width = wid))  
  
print('{:{padding}{align}{width}{grouping_option}}'.format(int(str1) , padding = pad ,align='^' ,width = wid ,grouping_option = ","))  