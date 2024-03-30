import decimal

m = decimal.Decimal(input("本金："))     #principal
r = decimal.Decimal(input("利率："))     #rate
y = decimal.Decimal(input("存幾年:"))     #years
final = m * pow(1+r,y)           #m*(1+r)^y 

print("本利和：",final)
