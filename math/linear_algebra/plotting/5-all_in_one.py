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


fig, axes = plt.subplots(3, 2, figsize=(10, 10))


plt.rc('axes', labelsize='x-small')
plt.rc('axes', titlesize='x-small')


axes[0, 0].plot(y0)
axes[0, 0].set_title('Plot 1')
axes[0, 0].set_xlabel('X-axis Label 1')
axes[0, 0].set_ylabel('Y-axis Label 1')


axes[0, 1].scatter(x1, y1, color='magenta', label='Data')
axes[0, 1].set_title('Plot 2')
axes[0, 1].set_xlabel('X-axis Label 2')
axes[0, 1].set_ylabel('Y-axis Label 2')
axes[0, 1].legend()


axes[1, 0].plot(x2, y2, color='green')
axes[1, 0].set_title('Plot 3')
axes[1, 0].set_xlabel('X-axis Label 3')
axes[1, 0].set_ylabel('Y-axis Label 3')


axes[1, 1].plot(x3, y31, label='y31', color='blue')
axes[1, 1].plot(x3, y32, label='y32', color='red')
axes[1, 1].set_title('Plot 4')
axes[1, 1].set_xlabel('X-axis Label 4')
axes[1, 1].set_ylabel('Y-axis Label 4')
axes[1, 1].legend()


axes[2, 0].hist(student_grades, bins=10, edgecolor='black', alpha=0.7)
axes[2, 0].set_title('Plot 5')
axes[2, 0].set_xlabel('X-axis Label 5')
axes[2, 0].set_ylabel('Y-axis Label 5')


axes[2, 1].axis('off') 
axes[2, 1].set_title('Plot 6')

plt.tight_layout()

fig.suptitle('All in One', fontsize='x-small')
plt.show()
