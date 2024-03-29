# -*- coding: utf-8 -*-
"""LAB02-Intro-to-Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gTxnbS13Ehwo7VqVOvHBueoCeguq8WAX
"""

!pip install numpy

import numpy as np

x1 = np.array([1,2,3,4,5])
print(x1)

np.array(3, dtype='float', ndmin=2) #object

np.array([[2,4],[5,6]])

# np array function:
np.zeros(3)

np.ones(3)

np.full(10, np.pi)

np.full(10, 3.0)

np.linspace(5,10,8) #start,end, totalnum      `

np.zeros((3,5), dtype='int') #dimension, arrayno.ofelemen

np.full((3,6), np.pi)

np.eye(3) #identity matrix

#special  function
np.random.random() #[0-1) tak flaot return

np.random.random(5)

np.random.random((2,3))

np.random.randint(23) #(random int num low , high, size, dtype) 23)

np.random.randint(20,100, 5)

np.random.randint(20,100,(2,3))

np.random.uniform()#(random int num low , high, size) default #0-1 also more themn 1

np.random.uniform(0.3,1,1)#(random int num low , high, size) default #0-1 also more themn 1

np.random.uniform(20,10, (2,3))#(random int num low , high, size) default #0-1 also more themn 1

np.random.choice(5)

np.random.choice((2,3,5), size=5)

np.random.choice(range(1,50), (2,3), False)

#random array may set bana k liyah seed
np.random.seed(15)
print(np.unifrom)

print(X1)