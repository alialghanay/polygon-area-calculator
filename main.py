from quadrilateral import Rectangle, Square
def main():
    print(f'{"a Polygon Area Calculator":-^32}\n\n')
    print("\n\nCreating a Rectangle object with width 10 and height 20\n\n")
    rect = Rectangle(6, 3)
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter():^32.2f}")
    print(f"Diagonal: {rect.get_diagonal():^32.2f}")
    print(f"Picture:\n{rect.get_picture()!s:^32}")
    print(f"String Representation: {rect!s:^32}")
    print("\nCreating a Rectangle object with width 5 and height 10")
    rect.set_width(5)
    rect.set_height(10)
    print(f"String Representation: {rect!s:^32}")
    print("\nCreating a Square object with side 10")
    square = Square(10)
    square.set_side(5)
    print(f"Area: {square.get_area()}")
    print(f"Perimeter: {square.get_perimeter():^32.2f}")
    print(f"Diagonal: {square.get_diagonal():^32.2f}")
    print(f"Picture:\n{square.get_picture()!s:^32}")
    print(f"String Representation: {square!s:^32}")
    print("\nCreating a Square object with side 5")
    

if __name__ == "__main__":
    main()