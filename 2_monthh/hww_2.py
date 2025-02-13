class Figure:
   def calculate_area(self):
       pass
   def calculate_perimeter(self):
       pass
   def info(self):
       pass
class Square(Figure):
   def __init__(self, side_length):
       self.side_length = side_length
       self.perimeter = self.calculate_perimeter()
   def calculate_area(self):
       return self.side_length ** 2
   def calculate_perimeter(self):
       return 4 * self.side_length
   def info(self):
       area = self.calculate_area()
       print(f"Square side length: {self.side_length}cm, perimeter: {self.perimeter}cm, area: {area}cm")
class Rectangle(Figure):
   def __init__(self, length, width):
       self.__length = length
       self.__width = width
       self.perimeter = self.calculate_perimeter()
   def calculate_area(self):
       return self.__length * self.__width
   def calculate_perimeter(self):
       return 2 * (self.__length + self.__width)
   def info(self):
       area = self.calculate_area()
       print(f"Rectangle length: {self.__length}cm, width: {self.__width}cm, perimeter: {self.perimeter}cm, area: {area}cm")
square1 = Square(5)
square2 = Square(10)
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(6, 10)
rectangle3 = Rectangle(4, 7)
figures = [square1, square2, rectangle1, rectangle2, rectangle3]
for figure in figures:
   figure.info()
