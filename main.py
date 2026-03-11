from typing import List, Tuple

Point = Tuple[float, float]

def find_orientation(p, q, r):

    if p == () or q == () or r == ():
        return -1

    fin = ((q[1]-p[1]) * (r[0]-q[0]) - (r[1] - q[1]) * (q[0] - p[0])) 

    if fin == 0:    #Collinear
        return 0
    elif fin > 0:   #Counter Clockwise
        return 1
    else:           #Clockwise
        return 2
    
def convex_hull_jarvis(points: List[Point]) -> List[Point]:

    if points == []:
        return -1

    points.sort()
    hull = [points[0]]
    
    p, q = 0, 0

    q = p + 1
    for i in range(1, len(points)):
        if find_orientation(points[p], points[q], points[i]) == 2:
            q = i
    hull.append(points[q])
    p = q
    
    while points[p] != hull[0]:
        q = p + 1
        for i in range(0, len(points) - 1):
            if find_orientation(points[p], points[q], points[i]) == 2:
                q = i
        hull.append(points[q])
        p = q
    
    return hull
    
if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]