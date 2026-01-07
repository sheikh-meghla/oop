class Teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    def show_info(self):
        print("Teacher name:", self.name)
        print("sub:", self.sub)

s1 = Teacher("Liza", "English")
s1.show_info()


