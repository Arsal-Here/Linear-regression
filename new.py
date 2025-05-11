import matplotlib.pyplot as plt 
import numpy as np

x= np.array([1760,1652,1485,1390,1820,1665,1550,1700,1270]) #replace values with x-values
y = np.array([4300,4650,3200,3150,4950,4010,3810,4500,3008]) # replace values with y-values

print("mean of x is ",x.mean())
print("mean of y is ",y.mean())
print("sum of x is ",x.sum())
print("sum of y is ",y.sum())
n=0
for i in x:
    n+=1

sumXY=0.0
for i in range(0,n):
    sumXY+=x[i]*y[i]
print("sum of x*y is ",sumXY)

sumXX=0.0
for i in range(0,n): 
    sumXX+=x[i]*x[i]
print("sum of x*2 is ",sumXX)


val = ((n*sumXY)-(x.sum()*y.sum()))/((n*sumXX)-(x.sum()*x.sum()))
print("B1 = ",val)

b_0 =y.mean() - (val*x.mean())

print("B0 is ",b_0)

plt.scatter(x,y,color = 'red')
plt.legend()
plt.grid(True)
plt.show()

