#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

x=["Farrah", "Fred", "Felicia"]
y1=np.array([2,15,12])
y2=np.array([9,30,25])
y3=np.array([18,32,30])
y4=np.array([35,50,48])

plt.bar(x,y1, color='r', width=0.5)
plt.bar(x,y2, bottom=y1, color='y', width=0.5)
plt.bar(x,y3, bottom=y1+y2, color='#ff8000', width=0.5)
plt.bar(x,y4, bottom=y1+y2+y3, color='#ffe5b4', width=0.5)

plt.legend(["apples", "bananas", "oranges", "peaches"])
plt.ylabel("Quantity of Fruit")

plt.yticks(np.arange(0,90,10))
plt.title("Number of Fruit per Person")

plt.show
