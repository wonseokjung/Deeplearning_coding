class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("initialized SchoolMember: {}".format(self.name))

    def tell(self):
        "tell my detail"
        print('name:"{}" Age:"{}"').format(self.name, self.age)


class Teacher(SchoolMember):
    "Represent a teacher"

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initialized teacher:{})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)x
        print('Salary:"{d}"'.format(self.salary))


class Student(SchoolMember):
    "Represent a stduent"

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))


t = Teacher("Mrs.Shrividya", 40, 30000)
s = Student("WonseokJUng", 29, 100)

print()

members = [t, s]
for i in members:
    i.tell()
