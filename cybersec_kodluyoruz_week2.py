import matplotlib.pyplot as plt
import numpy
import math

points = [[5,5],[8,5],[8,9]]
distances = []
def euclideanDistance(**points):
    
    """dist_x = int(points[0][0][0]) - int(points[0][1][0])
    dist_y = int(points[0][0][1]) - int(points[0][1][1])
    euclid = math.sqrt((dist_x**2)+(dist_y**2))
    return euclid"""
    dist_x = int(points[0][0][0]) - int(points[0][1][0])
    dist_y = int(points[0][0][1]) - int(points[0][1][1])
    euclid = math.sqrt((dist_x**2)+(dist_y**2))
    return euclid

plt.figure(figsize=(50,50))
plt.xlim(0, 20)
plt.ylim(0, 20)


for i in points:
    x1 = i[0]
    y1 = i[1]

    for j in points:
        x2 = j[0]
        y2 = j[1]
        dist_x = x2-x1
        dist_y = y2-y1
        dist =  math.sqrt((dist_x**2)+(dist_y**2))
        if(j != i):
            xcoord=(i[0],j[0])
            ycoord = (i[1],j[1])
            plt.plot(x1, y1, marker ='o')
            plt.plot(x2, y2, marker ='o')
            plt.plot(xcoord,ycooord, color ="red", linewidth=3)
            distances.append(dist)

"""plt.fill((points[0],points[1],points[2]), color = '#3f9be3')"""

min_distance = min(distances)
print(min_distance)
        

"print(euclideanDistance(5,8,5,5))"



plt.show()
