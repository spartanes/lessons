import math


class ProperFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = math.gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <=
                other.numerator * self.denominator)

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator +
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator -
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return ProperFraction(new_numerator, new_denominator)

if __name__ == "__main__":
    fraction1 = ProperFraction(1, 2)
    fraction2 = ProperFraction(3, 4)

    print(f"Дріб 1: {fraction1}")
    print(f"Дріб 2: {fraction2}")

    # Додавання
    sum_fraction = fraction1 + fraction2
    print(f"Сума: {sum_fraction}")

    # Віднімання
    diff_fraction = fraction1 - fraction2
    print(f"Різниця: {diff_fraction}")

    # Множення
    product_fraction = fraction1 * fraction2
    print(f"Добуток: {product_fraction}")

    # Порівняння
    print(f"fraction1 == fraction2: {fraction1 == fraction2}")
    print(f"fraction1 < fraction2: {fraction1 < fraction2}")
    print(f"fraction1 <= fraction2: {fraction1 <= fraction2}")
    print(f"fraction1 > fraction2: {fraction1 > fraction2}")
    print(f"fraction1 >= fraction2: {fraction1 >= fraction2}")
