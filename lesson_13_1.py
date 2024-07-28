class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}"

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def __str__(self):
        return f"ID: {self.student_id}, Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}"

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Об'єкт не є студентом")

    def remove_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)
            return student
        else:
            return None

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return '\n'.join(str(student) for student in self.students)

student1 = Student("Іван", "Петренко", 20, "001")
student2 = Student("Ольга", "Коваль", 22, "002")
student3 = Student("Андрій", "Шевченко", 21, "003")

group = Group()

group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

print(group)

found_student = group.find_student("Коваль")
print("\nЗнайдено студента:\n", found_student)

removed_student = group.remove_student("Коваль")
print("\nВидалено студента:\n", removed_student)

print("\nСписок студентів після видалення:\n", group)
