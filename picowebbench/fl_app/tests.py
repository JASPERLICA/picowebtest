from django.test import TestCase

# Create your tests here.
# from matplotlib import pyplot as plt

# # import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[t**2 for t in x]
# plt.plot(x,y)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# s = pd.Series([1, 2, 3])
# fig, ax = plt.subplots()
# s.plot.bar()
# fig.savefig('my_plot.png')

x=np.linspace(-1,1,50)#-1到1中画50个点
print(x)
print(type(x))
y=x**2
print(y)
print(type(y))
plt.plot(x,y,color='green')
plt.tick_params(axis='x',colors='blue')
plt.tick_params(axis='y',colors='red')
# fig, ax = plt.subplots()
plt.savefig('jasper.png')
plt.show()
# jasper = plt.show()
# jasper.savefig('jasper.png')
