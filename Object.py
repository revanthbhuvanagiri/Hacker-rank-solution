class computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_comp(self):
        print("my computer name is ", self.name, "and the age of the computer", self.age)


revanth = computer('HP', 30)

revanth.my_comp()