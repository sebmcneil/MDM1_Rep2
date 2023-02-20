import numpy as np
from scipy.spatial.distance import cdist


x = np.array([(0,0)])
print(x)
y = np.array([(1.1, -1), (1.4, 1), (-0.2, 1.3), (-0.55, 2), (-3.25, 1.76), (-3.9, 0.9), (-4.75, -0.6),
       (-5.4, -1.18), (-5.2, -2.2), (-4.15, -1.2), (-1.7, -2.1), (-0.8, -1.9), (-0.4, -2.1)])

d = cdist(x,y)
idx = np.argmin(d)
print(y[int(idx)])



# the village with a cable connected to it
x_2 = np.array([y[int(idx)]])
# print(x_2)

# the rest of the villages
y_2 = np.delete(y, idx, 0)
# print(y_2)

d_2 = cdist(x_2,y_2)
idx_2 = np.argmin(d_2)
print(y_2[int(idx_2)])



# the village with a cable connected to it
x_3 = np.array([y_2[int(idx_2)]])
# print(x_3)

# the rest of the villages
y_3 = np.delete(y_2, idx_2, 0)
# print(y_3)

d_3 = cdist(x_3,y_3)
idx_3 = np.argmin(d_3)
print(y_3[int(idx_3)])



# the village with a cable connected to it
x_4 = np.array([y_3[int(idx_3)]])
# print(x_4)

# the rest of the villages
y_4 = np.delete(y_3, idx_3, 0)
# print(y_4)

d_4 = cdist(x_4,y_4)
idx_4 = np.argmin(d_4)
print(y_4[int(idx_4)])




# the village with a cable connected to it
x_5 = np.array([y_4[int(idx_4)]])
# print(x_5)

# the rest of the villages
y_5 = np.delete(y_4, idx_4, 0)
# print(y_5)

d_5 = cdist(x_5,y_5)
idx_5 = np.argmin(d_5)
print(y_5[int(idx_5)])




# the village with a cable connected to it
x_6 = np.array([y_5[int(idx_5)]])
# print(x_6)

# the rest of the villages
y_6 = np.delete(y_5, idx_5, 0)
# print(y_6)

d_6 = cdist(x_6,y_6)
idx_6 = np.argmin(d_6)
print(y_6[int(idx_6)])




# the village with a cable connected to it
x_7 = np.array([y_6[int(idx_6)]])
# print(x_6)

# the rest of the villages
y_7 = np.delete(y_6, idx_6, 0)
# print(y_5)

d_7 = cdist(x_7,y_7)
idx_7 = np.argmin(d_7)
print(y_7[int(idx_7)])




# the village with a cable connected to it
x_8 = np.array([y_7[int(idx_7)]])
# print(x_8)

# the rest of the villages
y_8 = np.delete(y_7, idx_7, 0)
# print(y_8)

d_8 = cdist(x_8,y_8)
idx_8 = np.argmin(d_8)
print(y_8[int(idx_8)])





# the village with a cable connected to it
x_9 = np.array([y_8[int(idx_8)]])
# print(x_9)

# the rest of the villages
y_9 = np.delete(y_8, idx_8, 0)
# print(y_9)

d_9 = cdist(x_9,y_9)
idx_9 = np.argmin(d_9)
print(y_9[int(idx_9)])





# the village with a cable connected to it
x_10 = np.array([y_9[int(idx_9)]])
# print(x_8)

# the rest of the villages
y_10 = np.delete(y_9, idx_9, 0)
# print(y_8)

d_10 = cdist(x_10,y_10)
idx_10 = np.argmin(d_10)
print(y_10[int(idx_10)])





# the village with a cable connected to it
x_11 = np.array([y_10[int(idx_10)]])
# print(x_11)

# the rest of the villages
y_11 = np.delete(y_10, idx_10, 0)
# print(y_10)

d_11 = cdist(x_11,y_11)
idx_11 = np.argmin(d_11)
print(y_11[int(idx_11)])





# the village with a cable connected to it
x_12 = np.array([y_11[int(idx_11)]])
# print(x_12)

# the rest of the villages
y_12 = np.delete(y_11, idx_11, 0)
# print(y_12)

d_12 = cdist(x_12,y_12)
idx_12 = np.argmin(d_12)
print(y_12[int(idx_12)])




# the village with a cable connected to it
x_13 = np.array([y_12[int(idx_12)]])
# print(x_13)

# the rest of the villages
y_13 = np.delete(y_12, idx_12, 0)
# print(y_13)

d_13 = cdist(x_13,y_13)
idx_13 = np.argmin(d_13)
print(y_13[int(idx_13)])



D = np.sort(d)
D_ = float(D[0, 0])

D2 = np.sort(d_2)
D_2 = float(D2[0, 0])

D3 = np.sort(d_3)
D_3 = float(D3[0, 0])

D4 = np.sort(d_4)
D_4 = float(D4[0, 0])

D5 = np.sort(d_5)
D_5 = float(D5[0, 0])

D6 = np.sort(d_6)
D_6 = float(D6[0, 0])

D7 = np.sort(d_7)
D_7 = float(D7[0, 0])

D8 = np.sort(d_8)
D_8 = float(D8[0, 0])

D9 = np.sort(d_9)
D_9 = float(D9[0, 0])

D10 = np.sort(d_10)
D_10 = float(D10[0, 0])

D11 = np.sort(d_11)
D_11 = float(D11[0, 0])

D12 = np.sort(d_12)
D_12 = float(D12[0, 0])

D13 = np.sort(d_13)
D_13 = float(D13[0, 0])

Total_distance = D_ + D_2 + D_3 + D_4 + D_5 + D_6 + D_7 + D_8 + D_9 + D_10 + D_11 + D_12 + D_13


print(Total_distance)















