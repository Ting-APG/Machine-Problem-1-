import matplotlib.pyplot as plt
import numpy as np
def f(n):
    if n<= 9:
         return (n**2)-7
    else:
         return f(n-10)
x = []
y = []
for n in range(0,100):
   x.append(n)
   y.append(f(n))
   print(x)
   print(y)
   plt.stem(x,y)
   plt.xlabel('n')
   plt.ylabel('f(n)')
   plt.title( 'The graph for f(n)' )
   plt.show()
