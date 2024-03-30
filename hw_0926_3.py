import sys  
oddSum = 0  
evenSum = 0  
  
while True:  
    try:  
        line = input()  
        if(int(line) % 2 == 1): oddSum += int(line)  
        if(int(line) % 2 == 0): evenSum += int(line)  
          
    except EOFError:  
        break  
      
print('odd:{} even:{}'.format(oddSum,evenSum)) 
