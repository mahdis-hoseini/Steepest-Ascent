import numdifftools as nd 
import numpy as np
from sympy import symbols, solve
import numpy as np
import numpy.matlib 
import numpy as geek 
from sympy import *

#از آنجا که ممکن است (numdifftools) نصب نباشد بنابراین  در صورت نیاز قبل از اجرای برنامه می تواند آن را نصب کنید در نسخه ژوپیتر کد آن را گذاشتم
#pip install numdifftools

def rosen(x):
  f = -(x[0]-2)**2-(x[0])-(x[1])**2  
  return f
arrayX = np.array([2.5,1.5]) 
grad = nd.Gradient(rosen)(arrayX) 
print("Gradient of -(x1-2)^2-x1-(x2)^2 at (2.5,1.5) is ", grad) 

while True:
    if grad[0] !=0 and grad[1] !=0:
      t1 = symbols('t1')
      t2 = symbols('t2')
      arrayT = np.array([t1,t2])
      T=grad*arrayT
      arrayTotal = np.array(T)
      in_arr1 = geek.array([arrayX[0],arrayX[1]]) 
      in_arr2 = geek.array([arrayTotal[0] ,arrayTotal[1]])     
      ft0 = geek.add(in_arr1, in_arr2)  
      x1 = ft0[0]
      x2 = ft0[1]
      func = -(x1-2)**2-(x1)-(x2)**2
      t1 = symbols('t1') 
      t1=t2
      expr = func
      expr_diff = Derivative(expr,t1)   
      solveT = expr_diff.doit()
      c = solve(solveT,t1)
      arrayT = np.array(c,dtype=np.float) 
      arrayG = np.array(grad)
      newpoint = arrayX+(arrayT*arrayG)
      newpoint  = np.array(newpoint, dtype=np.float)
      list(map('{:.2f}'.format,newpoint))
      gradnewpoint = nd.Gradient(rosen)(newpoint) 
      break
print("Gradient of -(x1-2)^2-x1-(x2)^2 at (2.5,1.5) is ", grad)    
print("output array  T : " , arrayTotal)
print("output array after add T to func : ", ft0)
print("Derivative of expression : {}".format(expr_diff))   
print("Value of the derivative : {} ".format(expr_diff.doit())) 
print("Value of T0 : {} ".format(arrayT))
print("Value of New point : {} ".format(list(map('{:.2f}'.format,newpoint))))
print("Gradient of -(x1-2)^2-x1-(x2)^2 at (1.5,0) is ",gradnewpoint) 