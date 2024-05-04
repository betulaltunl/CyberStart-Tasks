import math

# Noktaları tanımlama
points = [(0,0),(3,4),(5,12),(1,1)]

# Öklid mesafesini hesaplayan fonksiyon 
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    calculation_1 = x1-x2
    dimension_x = pow(calculation_1,2)
    calculation_2 = y1-y2
    dimension_y = pow(calculation_2,2)
    euclideCalculation = math.sqrt(dimension_x+dimension_y)
    return euclideCalculation

# Mesafeleri hesaplama
distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Minimum mesafeyi bulma ve yazdırma
min_distance = min(distances)
print("Minimum mesafe:", min_distance)


