#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig=plt.figure()

ax1=fig.add_subplot(3,2,1)
ax1.plot(y0,c="red")
ax1.set_xlim(0,11)

ax2=fig.add_subplot(3,2,2)
ax2.set_xlabel("Height(in)", fontsize='x-small')
ax2.set_ylabel("Weight(lbs)", fontsize='x-small')
ax2.set_title ("Men\'s Height vs. Weight", fontsize='x-small')
ax2.scatter(x1,y1, c="magenta")

ax3=fig.add_subplot(3,2,3)
ax3.set_xlabel("Time(years)",fontsize='x-small' )
ax3.set_ylabel("Fraction Remaining", fontsize='x-small')
ax3.set_title("Exponential Decay of C-14", fontsize='x-small')
ax3.set_yscale('log')
ax3.set_xlim(0,28650)
ax3.plot(x2,y2, c="blue")

ax4=fig.add_subplot(3,2,4)
ax4.set_xlabel("Time(years)", fontsize='x-small')
ax4.set_ylabel("Fraction Remaining", fontsize='x-small')
ax4.set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
ax4.set_xlim(0,20000)
ax4.set_ylim(0,1)
ax4.plot(x3,y31, linestyle="dashed", c="red", label="C-14")
ax4.plot(x3,y32, c="green", label="Ra-226")

ax4.legend()

ax5=fig.add_subplot(3,1,3)
ax5.set_xlabel("Grades", fontsize='x-small')
ax5.set_ylabel("Number of Students",fontsize='x-small' )
ax5.hist(student_grades, edgecolor="black", bins=np.arange(40,110,10))
ax5.set_title("Project A", fontsize='x-small')

fig.suptitle("All in One")
plt.tight_layout()
plt.show

