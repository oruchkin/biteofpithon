class Point:
    "Класс для представления координат точек на плоскости"
    x = 1
    y = 1

pt = Point()

pt.x = 5
pt.y = 10

print(f"{isinstance(pt, Point)} isinstance")

print( getattr(pt, "x", False))
print( hasattr(pt, "y"))
print( setattr(pt, "z", 7))
print(pt.__dict__)
delattr(pt, "z")

print( pt.__dict__)

setattr(Point, "k", 9)
setattr(Point, "k", 9)

Point.z = 100
pt.msg = "hello"
print(pt.msg)
print(Point.z)



#Point.x = 100

#print( pt.x, pt.y)
#print( id(pt), id(Point), sep="\n")


#print(Point.__doc__)
#print(Point.__name__)
#print(dir(Point))
