class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if (isinstance(x, int) or isinstance(x, float)):
            return True
        return False

    
    def __getCoordX(self):
        print("вызов __getCoordX")
        return self.__x

    def __setCoordX(self, x): 
        #print("вызов __setCoordX")
        if Point.__checkValue(x):
                self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    def __deleCoordX(self):
        print("Удаление свойства")
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __deleCoordX)


pt = Point(1,2)

pt.coordX = 100  # запись значения
x = pt.coordX   # чтение значения
print(x)

del pt.coordX
#pt.coordX = 7
#print(pt.coordX)


