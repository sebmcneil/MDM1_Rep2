import numpy as np

cities = ['Argos', 'Ephicos', 'Satea', 'Hublosmelo', 'Hapithesia', 'Anionti', 'Muirotipo', 'Neapopnia', 'Komissos', 'Sukiea', 'Halelion', 'Icrearchia', 'Skyla', 'Emnos']

coordinates = [(0, 0), (1.1, -1), (1.4, 1), (-0.2, 1.3), (-0.55, 2), (-3.25, 1.76), (-3.9, 0.9), (-4.75, -0.6), (-5.4, -1.18), (-5.2, -2.2), (-4.15, -1.2), (-1.7, -2.1), (-0.8, -1.9), (-0.4, -2.1)]

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


