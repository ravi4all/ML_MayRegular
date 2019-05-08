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


##import matplotlib.pyplot as plt
##
##
x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
y = [795,898,642,533,382,205,102,0,0,0,0,0,0,0,0]

x2 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
y2 = [146596557,146596567,146596957,146596427,146596578,146596512,146596599,
      142805088,142742350,142785342,142849449,142960868,143201676,143506911,143819569]

# Ploting bars
plt.bar(x,y,label = "Malarial Effect", color = 'b')
# Color could be given directly by name or hex value or like 'b' for Blue, 'r' for red
plt.bar(x2,y2, label = "Population", color = 'r')

plt.xlabel('Years')
plt.ylabel('Total Population')
plt.title('Bar graph & Histogram')
plt.legend()
plt.show()
