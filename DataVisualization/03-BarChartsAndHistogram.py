import matplotlib.pyplot as plt


x = [2,4,6,8,10]
y = [3,5,9,2,4]

x2 = [3,5,7,9,11]
y2 = [5,8,6,1,2]

# Ploting bars
plt.bar(x,y,label = "Bar1", color = 'b')
# Color could be given directly by name or hex value or like 'b' for Blue, 'r' for red
plt.bar(x2,y2, label = "Bar2", color = 'r')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Bar graph & Histogram')
plt.legend()
plt.show()
