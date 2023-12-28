from lab_python_oop.circle import Circle
from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

if __name__ == "__main__":
    print(Rectangle(5, 5, Color("Blue")))
    print(Circle(5, Color("Green")))
    print(Square(5, Color("Red")))

    rectangle = Rectangle(15, 15, "Pink")
    print(rectangle.get_area())
