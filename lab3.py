import matplotlib.pyplot as plt


labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [25, 30, 20, 25]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # custom color codes

plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Pie Chart')
plt.show()


categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.bar(categories, values, color='green')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()


data = [12, 15, 13, 15, 17, 18, 21, 20, 22, 25, 28, 29, 30, 30, 32]
plt.hist(data, bins=5, color='blue', edgecolor='orange')
plt.title('Histogram')
plt.xlabel('Value Ranges')   
plt.ylabel('Frequency')
plt.show()


x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]
plt.scatter(x, y, color='red')
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
