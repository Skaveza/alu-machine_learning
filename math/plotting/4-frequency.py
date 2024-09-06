#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.hist(student_grades, edgecolor="black", bins=np.arangee(40,110,10))
plt.title("Project A")

plt.show()

