from person import Person


class Student(Person):
    student_list = []
    def __init__(self, first_name, last_name, age, instructor, current_stack):
        # execute the parent class (Person) constructor and initialize those attributes
        super().__init__(first_name, last_name, age)
        self.instructor = instructor
        self.current_stack = current_stack
        Student.student_list.append(self)
    #Overwriting
    def print_info(self):
        super().print_info()    #Polymorphism
        print("Instructor:", self.instructor)
        print("Current stack:", self.current_stack)

    @classmethod
    def print_all_students(cls):
        for student in cls.student_list:
            student.print_info()

print("******** MENU OF OPTIONS **********")
print("1) Add a new student to the list")
print("2) Show all the list of students")
print("0) Exit the program")
option = input("")

while option != "0":
    if option == "1":
        first_name = input("Please type your first name: ")
        last_name = input("Please type your last name: ")
        age = input("Please type your age: ")
        instructor = input("PLease type your instructor's name: ")
        stack = input("Please type your current stack: ")
        
        new_student = Student(first_name, last_name, age, instructor, stack)
    elif option == "2":
        Student.print_all_students()
    
    print("******** MENU OF OPTIONS **********")
    print("1) Add a new student to the list")
    print("2) Show all the list of students")
    print("0) Exit the program")
    option = input("")  
