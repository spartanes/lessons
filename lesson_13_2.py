class DigitalCounter:
    def __init__(self, initial_value=0, min_value=0, max_value=10):
        self.initial_value = initial_value
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = initial_value

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_initial_value(self, initial_value):
        if initial_value < self.min_value or initial_value > self.max_value:
            raise ValueError("Початкове значення повинно бути між мінімальним і максимальним значенням.")
        self.initial_value = initial_value
        self.current_value = initial_value

    def step_up(self):
        if self.current_value >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current_value += 1

    def step_down(self):
        if self.current_value <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current_value -= 1

    def get_current_value(self):
        return self.current_value

counter = DigitalCounter(initial_value=5, min_value=0, max_value=10)

print(counter.get_current_value())  # 5
counter.step_up()
print(counter.get_current_value())  # 6
counter.step_down()
print(counter.get_current_value())  # 5

counter.set_max_value(15)
counter.set_min_value(2)
counter.set_initial_value(3)
print(counter.get_current_value())  # 3

try:
    for _ in range(13):
        counter.step_up()
except ValueError as e:
    print(e)

try:
    for _ in range(5):
        counter.step_down()
except ValueError as e:
    print(e)
