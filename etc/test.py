class Object:
    pass

class Point(Object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(' + str(self.x) + ', '+ str(self.y) + ')'

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

if __name__ == '__main__':
    p = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(4, 3)
    print(p == p2)
    print(p2 == p3)

