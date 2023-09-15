#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Define the fruit labels and colors
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create a stacked bar graph
fig, ax = plt.subplots()

# Calculating the position of the bars for each person
x = np.arange(len(fruits))

# Plotting the stacked bars for each person
for i in range(fruit.shape[1]):
    bottom = 0
    for j in range(fruit.shape[0]):
        ax.bar(x[i], fruit[j, i], width=0.5, bottom=bottom, label=fruits[j], color=colors[j])
        bottom += fruit[j, i]

# Labeling the axes and set the title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Setting the y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Setting the legend
plt.legend()

ax.set_xticks(x)
ax.set_xticklabels(['Farrah', 'Fred', 'Felicia'])

plt.show()
