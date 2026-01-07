class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age


    def show_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)
        print("age:", self.age)


s1 = Student("Meghla", 20, 17)

s1.show_info()
