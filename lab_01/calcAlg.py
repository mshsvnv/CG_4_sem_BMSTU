import numpy as np
EPS = 10**(-4)

def oneLine(point_1:list, point_2:list, point_3:list):
    
    if abs((point_3[0] - point_1[0]) * (point_2[1] - point_1[1]) - \
    (point_2[0] - point_1[0]) * (point_3[1] - point_1[1])) <= EPS:
        return True # лежат на одной прямой
    
    return False # не лежат на одной прямой

def circleCenter(point_1:list, point_2:list, point_3:list):

    fact = 2 * np.array(
        [[point_1[0], point_1[1], 1],
        [point_2[0], point_2[1], 1],
        [point_3[0], point_3[1], 1]])

    xValue = np.array(
        [[point_1[0] ** 2 + point_1[1] ** 2, point_1[1], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[1], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[1], 1]])
    
    yValue = np.array(
        [[point_1[0] ** 2 + point_1[1] ** 2, point_1[0], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[0], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[0], 1]])

    xValue = np.linalg.det(xValue) / np.linalg.det(fact)
    yValue = (-1) * np.linalg.det(yValue) / np.linalg.det(fact)

    return [xValue, yValue]

def lenBetwPoints(point_1:list, point_2:list):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** (1/2)

def interPointCoord(radius_1, point_1:list, radius_2, point_2:list):
    
    fact = radius_1 / radius_2

    xValue = (point_1[0] + fact * point_2[0]) / (1 + fact)
    yValue = (point_1[1] + fact * point_2[1]) / (1 + fact)

    return [xValue, yValue]

def circlesIntersection(mainCircle, interPoint):

    xCenterSide = (mainCircle[0][0] + interPoint[0]) / 2
    yCenterSide = (mainCircle[0][1] + interPoint[1]) / 2

    radiusSide = lenBetwPoints([xCenterSide, yCenterSide], interPoint)
    d  = lenBetwPoints([xCenterSide, yCenterSide], mainCircle[0])

    a = (mainCircle[1] ** 2 - radiusSide ** 2 + d ** 2) / 2 * d

    h = (mainCircle[1] ** 2 - a ** 2) ** (1/2)

    p_2 = list()
    p_3 = list()
    p_4 = list()

    for i in range(2):
        p_2.append(mainCircle[0][i] + a * (interPoint[0] - mainCircle[0][i]) / d)

        p_3.append(p_2[i] + h * (interPoint[1 - i] - mainCircle[0][1 - i]) / d)

        p_4.append(p_2[i] - h * (interPoint[1 - i] - mainCircle[0][1 - i]) / d)

        h *= -1
    # p_2 = [mainCircle[0][0] + a * (interPoint[0] - mainCircle[0][0]) / d,
    #        mainCircle[0][1] + a * (interPoint[1] - mainCircle[0][1]) / d]
    
    # p_3 = [p_2[0] + h * (interPoint[1] - mainCircle[0][1]) / d,
    #        p_2[1] - h * (interPoint[0] - mainCircle[0][0]) / d]
    
    # p_4 = [p_2[0] - h * (interPoint[1] - mainCircle[0][1]) / d,
    #        p_2[1] + h * (interPoint[0] - mainCircle[0][0]) / d]
    
    return p_3, p_4

def triangleSquare(point_1: list, point_2: list, point_3: list):
    
    s = np.array([[point_1[0], point_1[1], 1],
                [point_2[0], point_2[1], 1],
                [point_3[0], point_3[1], 1]])
    
    return np.linalg.det(s)
           
