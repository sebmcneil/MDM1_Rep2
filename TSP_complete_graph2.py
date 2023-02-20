

import matplotlib.pyplot as plt

def plotline(p1, p2):
   x=(p1[0],p2[0]) #x values
   y=(p1[1],p2[1])#y values
   plt.plot(x, y, "-b", label="x,y") #plot the points in graph

data = [(1.25, -2.05), (-2.81, -2.3), (-1.94, -1.33), (-1.6, 0.05), (2.2, -1.6), (1, 0.7), (2, 1.77),
       (-0.77, 2.2), (-4.5, 1.53), (-1.9, 2.25), (-2.3, 2.6), (-2.45, 2.97), (0.65, 3.2), (4.3, 0.8), (3.15, -0.55),
       (4.1, -2.4)]

for i, xy in enumerate(data):
   for xy2 in data[i+1:]:
       plotline(xy, xy2)

x = [d[0] for d in data]
y = [d[1] for d in data]
plt.plot(x, y, 'o',color='r')
plt.show()

