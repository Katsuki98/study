from random import randint

def is_inside(point, rect):
    if point[0] < rect[0]:
        return False
    elif point[1] < rect[1]:
        return False
    elif point[0] > rect[0] + rect[2]:
        return False
    elif point[1] > rect[1] + rect[3]:
        return False
    else:
        return True

print(is_inside([100, 120], [140, 60, 100, 200]))
print(is_inside([200, 120], [140, 60, 100, 200]))
