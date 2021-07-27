class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Styles:
    def __init__(self):
        print("Конструктор Styles")

        super().__init__()


class Pos:
    def __init__(self):
        print("Конструктор Pos")
        
        super().__init__()

class Line(Pos, Styles):

    def __init__(self, sp: Point, ep: Point, color="red", width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(
            f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


l = Line(Point(10, 10), Point(100, 100), "green", 5)
l.draw()

print(Line.__mro__)
