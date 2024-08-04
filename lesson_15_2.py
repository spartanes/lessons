import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.area + other.area
            side = math.sqrt(total_area)
            return Rectangle(side, side)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_area = self.area * n
            side = math.sqrt(new_area)
            return Rectangle(side, side)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)


if __name__ == "__main__":
    rect1 = Rectangle(2, 4)
    rect2 = Rectangle(3, 6)

    print(f"Прямокутник 1: {rect1}")
    print(f"Прямокутник 2: {rect2}")

    # Порівняння
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 > rect2: {rect1 > rect2}")

    # Додавання
    sum_rect = rect1 + rect2
    print(f"Сума: {sum_rect} з площею {sum_rect.area}")

    # Множення на число
    scaled_rect = rect1 * 2
    print(f"Множення rect1 на 2: {scaled_rect} з площею {scaled_rect.area}")

    # Множення з іншої сторони (rmul)
    scaled_rect_rmul = 3 * rect1
    print(f"Множення rect1 на 3 з іншої сторони: {scaled_rect_rmul} з площею {scaled_rect_rmul.area}")
