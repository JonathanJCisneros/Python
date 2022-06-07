class Student:
    # Constructor - Constructing objects
    def __init__(self, first_name, last_name, insructor, current_stack):
        # Attributes - Accessible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = insructor
        self.current_stack = current_stack
    
    # Methods
    def print_student_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Instructor:", self.instructor)
        print("Current stack:", self.current_stack)

    def full_name(self):
        return self.first_name + " " + self.last_name

alexander = Student("Alexander", "Miller", "Alfredo", "Python/Flask")
alexander.print_student_info()
print(f"{alexander.first_name}'s instructor is {alexander.instructor}")

print("-----------------")

martha = Student("Martha", "Smith", "Amanda", "Web Fundamentals")
martha.print_student_info()
print(f"{martha.first_name}'s instructor is {martha.instructor}")

name = alexander.full_name()
print(name)
