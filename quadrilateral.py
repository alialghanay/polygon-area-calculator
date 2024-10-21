from abc import ABC, abstractmethod

class Quadrilateral(ABC):
    _width: float
    _height: float

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def __init_subclass__(cls):
       if not hasattr(cls, "_width"):
           raise NotImplementedError("Subclass must have _width attribute")
       if not hasattr(cls, "_height"):
            raise NotImplementedError("Subclass must have _height attribute")

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass
    
    @abstractmethod
    def get_diagonal(self):
        pass

    @abstractmethod
    def get_picture(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(width={self._width}, height={self._height})"

class Rectangle(Quadrilateral):
    _width = 0
    _height = 0
    def __init__(self, width, height):
        super().__init__(width, height)
    def get_area(self):
        return self._width * self._height
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    def get_diagonal(self):
        return (self._width ** 2 + self._height ** 2) ** 0.5
    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        return f"{'*' * self._width}\n" * self._height
    def get_amount_inside(self, shape):
        return (self._width // shape._width) * (self._height // shape._height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_side(self, side):
        self._width = side
        self._height = side
    def set_width(self, width):
        self.set_side(width)
    def set_height(self, height):
        self.set_side(height)
    def __str__(self):
        return f"{self.__class__.__name__}(side={self._width})"