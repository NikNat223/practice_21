from rectangle import Rectangle,Square,Circle
# далее создаем два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())
# здесь создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)
# вывод площади квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())
# создадим два круга радиуса r
circle_1 = Circle(1)
circle_2 = Circle(4)
# выведем площади наших кругов
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())


figures = [rect_1,rect_2,square_1,square_2,circle_1,circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

