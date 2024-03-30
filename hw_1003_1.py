import collections
  
list0 = input()  
list1 = input()  
  
print(len(list0))  
  
set0 = set(list0)  
set1 = set(list1)  
  
print(len(set0))  
  
print(list0)  
 
print("".join(sorted(list(set0.intersection(set1))))) 

print(len(set0 | set1))  
print(len(set0 - set1))  
  
mostFreq = collections.Counter(list0 + list1).most_common(1)
print("{}:{}".format(mostFreq[0][0],mostFreq[0][1]))
