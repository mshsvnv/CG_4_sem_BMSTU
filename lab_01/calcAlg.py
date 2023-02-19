import numpy as np
EPS = 10**(-4)

def oneLine(point_1:list, point_2:list, point_3:list):
    
    if abs((point_3[0] - point_1[0]) * (point_2[1] - point_1[1]) - \
    (point_2[0] - point_1[0]) * (point_3[1] - point_1[1])) <= EPS:
        return False
    
    return True

def circleCenter(point_1:list, point_2:list, point_3:list):

    fact = 2 * np.array(
        [point_1[0], point_1[1], 1],
        [point_2[0], point_2[1], 1],
        [point_3[0], point_3[1], 1])

    xValue = np.array(
        [point_1[0] ** 2 + point_1[1] ** 2, point_1[1], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[1], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[1], 1])
    
    yValue = np.array(
        [point_1[0] ** 2 + point_1[1] ** 2, point_1[0], 1],
        [point_2[0] ** 2 + point_2[1] ** 2, point_2[0], 1],
        [point_3[0] ** 2 + point_3[1] ** 2, point_3[0], 1])
    
    xValue = np.linalg.det(xValue) / fact
    yValue = (-1) * np.linalg.det(yValue) / fact

def lenBetwPoints(point_1:list, point_2:list):
    return (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2
