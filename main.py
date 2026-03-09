from typing import List, Tuple

Point = Tuple[float, float]

def find_orientation(p, q, r):

    if p == () or q == () or r == ():
        return -1

    fin = ((q[1]-p[1]) * (r[0]-q[0]) - (r[1] - q[1]) * (q[0] - p[0])) 

    if fin == 0:    #collinear
        return 0
    elif fin > 0:   #
        return 1
    else:
        return 2
    
def convex_hull_jarvis(points: List[Point]) -> List[Point]:

    if points == []:
        return -1
    
    for i in range(points):
        

if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]