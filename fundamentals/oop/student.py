class Student:
    bootcamp = "Coding Dojo"
    list_students = []
    # Constructor - Constructing objects
    def __init__(self, first_name, last_name, insructor, current_stack, mark):
        # Attributes - Accessible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = insructor
        self.current_stack = current_stack
        # import Grade class tomorrow
        self.grade = Grade(current_stack, mark, first_name)
        Student.list_students.append(self)
    
    # Methods
    def print_student_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Instructor:", self.instructor)
        print("Current stack:", self.current_stack)
        self.grade.print_info().extra_points(5).print_info()

    def full_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def print_all_students(cls):
        for student in cls.list_students:
            print(student.full_name(), student.current_stack)
    
    @classmethod
    def change_stack(cls, new_stack):
        for student in cls.list_students:
            student.current_stack = new_stack

    @staticmethod
    def add_two_numbers(num1, num2):
        return num1 + num2

alexander = Student("Alexander", "Miller", "Alfredo", "Python/Flask", 9.2)
alexander.print_student_info()
print(f"{alexander.first_name}'s instructor is {alexander.instructor}")

print("-----------------")

martha = Student("Martha", "Smith", "Amanda", "Web Fundamentals", 7)
martha.print_student_info()
print(f"{martha.first_name}'s instructor is {martha.instructor}")

name = alexander.full_name()
print(name)

print(alexander.bootcamp)
print(martha.bootcamp)

Student.bootcamp = "The Coding Dojo"

print(alexander.bootcamp)
print(martha.bootcamp)

Student.print_all_students()

Student.change_stack("MERN")
Student.print_all_students()

print(Student.add_two_numbers(20, 30))