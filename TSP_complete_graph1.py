

import matplotlib.pyplot as plt

def plotline(p1, p2):
   x=(p1[0],p2[0]) #x values
   y=(p1[1],p2[1])#y values
   plt.plot(x, y, "-b", label="x,y") #plot the points in graph

data = [(0, 0), (1.1, -1), (1.4, 1), (-0.2, 1.3), (-0.55, 2), (-3.25, 1.76), (-3.9, 0.9), (-4.75, -0.6),
       (-5.4, -1.18), (-5.2, -2.2), (-4.15, -1.2), (-1.7, -2.1), (-0.8, -1.9), (-0.4, -2.1)]

for i, xy in enumerate(data):
   for xy2 in data[i+1:]:
       plotline(xy, xy2)

x = [d[0] for d in data]
y = [d[1] for d in data]
plt.plot(x, y, 'o',color='r')
plt.show()

