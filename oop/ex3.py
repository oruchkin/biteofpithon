#https://proproprogs.ru/python_oop/rezhimy-dostupa-gettery-i-settery

class Point:
    def __init__(self, x=0, y=0):        
        self.__x = x
        self.__y = y


    def setCoords(self, x,y):
        if (isinstance(x, int) or isinstance(x, float)) and \
         (isinstance(y, int) or isinstance(y, float)):

            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self):
        return self.__x, self.__y

    


pt = Point(1, 2)
print( pt.getCoords())
pt.setCoords("10",20)
print( pt.getCoords())
