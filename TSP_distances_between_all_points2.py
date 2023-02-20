import numpy as np

cities = ['Argos', 'Ephicos', 'Satea', 'Hublosmelo', 'Hapithesia', 'Anionti', 'Muirotipo', 'Neapopnia', 'Komissos', 'Sukiea', 'Halelion', 'Icrearchia', 'Skyla', 'Emnos']

coordinates = [(0,0), (1.25, -2.05), (-2.81, -2.3), (-1.94, -1.33), (-1.6, 0.05), (2.2, -1.6), (1, 0.7), (2, 1.77),
       (-0.77, 2.2), (-4.5, 1.53), (-1.9, 2.25), (-2.3, 2.6), (-2.45, 2.97), (0.65, 3.2), (4.3, 0.8), (3.15, -0.55),
       (4.1, -2.4)]

def calculate_distances(coordinates):
    n = len(coordinates)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            distance = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            distances[i][j] = distances[j][i] = distance
    return distances

distances = calculate_distances(coordinates)
print(distances)
