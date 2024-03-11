import math
x=float(input("Enter a positive number: "))
t=0.000001
est=1.0
while True:
    est=(est+x/est)/2
    d=abs(x-est**2)
    if d<=t:
        break
print("The program's estimate: ",est)
print("Python's estimate:      ",math.sqrt(x))