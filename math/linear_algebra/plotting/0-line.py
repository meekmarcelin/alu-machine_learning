#!/usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3 
#Apply solid color red line
plt.plot(x, y, 'r-')
 #adding some lables
 plt.xlabels('X-axis')
 plt.ylabels('Y-axis')
 plt.title('a line with the solid red color')

 plt.show