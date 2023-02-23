import numpy as np
EPS = 10**(-4)

def oneLine(point_1:list, point_2:list, point_3:list):
    
    if abs((point_3[0] - point_1[0]) * (point_2[1] - point_1[1]) - \
    (point_2[0] - point_1[0]) * (point_3[1] - point_1[1])) <= EPS:
        return True # лежат на одной прямой
    
    return False # не лежат на одной прямой

def circleCenter(point_1:list, point_2:list, point_3:list):

    fact = np.array(
        [[point_1[0], point_1[1], 1],
        [point_2[0], point_2[1], 1],
        [point_3[0], point_3[1], 1]])
    
    fact = 2 * np.linalg.det(fact)

    xValue = np.array(
        [[point_1[0] ** 2 + point_1[1] ** 2, point_1[1], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[1], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[1], 1]])
    
    yValue = np.array(
        [[point_1[0] ** 2 + point_1[1] ** 2, point_1[0], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[0], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[0], 1]])

    xValue = np.linalg.det(xValue) / fact
    yValue = (-1) * np.linalg.det(yValue) / fact

    return [xValue, yValue]

def lenBetwPoints(point_1:list, point_2:list):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** (1/2)

def interPointCoord(radius_1, point_1:list, radius_2, point_2:list):
    
    fact = radius_1 / radius_2

    xValue = (point_1[0] + fact * point_2[0]) / (1 + fact)
    yValue = (point_1[1] + fact * point_2[1]) / (1 + fact)

    return [xValue, yValue]

def circlesIntersection(mainCircle, interPoint):

    centerSide = [(mainCircle[0][0] + interPoint[0]) / 2,
                (mainCircle[0][1] + interPoint[1]) / 2]
   
    radiusSide = lenBetwPoints(centerSide, interPoint)
    
    d  = radiusSide
    
    a = (mainCircle[1] ** 2) / (2 * d)
   
    h = (mainCircle[1] ** 2 - a ** 2) ** (1/2)
    
    p_2 = list()
    p_3 = list()
    p_4 = list()

    for i in range(2):
        p_2.append(mainCircle[0][i] + a * (centerSide[i] - mainCircle[0][i]) / d)

        p_3.append(p_2[i] + h * (centerSide[1 - i] - mainCircle[0][1 - i]) / d)

        p_4.append(p_2[i] - h * (centerSide[1 - i] - mainCircle[0][1 - i]) / d)

        h *= -1

    return [p_3, p_4]

def triangleSquare(point_1: list, point_2: list, point_3: list):
    
    s = np.array([[point_1[0], point_1[1], 1],
                [point_2[0], point_2[1], 1],
                [point_3[0], point_3[1], 1]])
    
    return np.linalg.det(s)
           
