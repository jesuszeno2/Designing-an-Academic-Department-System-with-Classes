"""
Jesus Zeno SIE Extra Credit C
We will be implementing the classes for the UML diagram for the academic department. This will demonstrate
the use of inheritance, association, and aggregation.
"""

# Person class will be the parent class of Student and Professor classes.
class Person:
    def __init__(self, name="", address="", phone="", email="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._name = str(name)
        self._address = str(address)
        self._phone = int(phone)
        self._email = str(email)
        self._course_list = None
        self._courses_names_list = None
        courses_list = []
        courses_names_list = []
        self._courses_list = courses_list
        self._courses_names_list = courses_names_list

    # Method to print the info for a person
    def Print_Person_Info(self):
        print("Name: {}".format(self._name))
        print("Address: {}".format(self._address))
        print("Phone number: {}".format(self._phone))
        print("Email: {}".format(self._email))


    # Method to list out all the courses for a person
    def ListCourses(self):
        i = 0
        # Use a for loop to iterate through all the courses for the person. In each iteration,
        # call the DisplayCourseInfo method.
        for i in range(len(self._courses_list)):
            # Try except block to tell us if there is an error displaying courses.
            try:
                self._courses_list[i].DisplayCourseInfo()
            except:
                print("Error displaying courses for person.")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the course to the list of courses for a specific person. Note that we are adding
    # the course objects to one list so we can call on their methods later as well as the course names
    # to another list so they are easily displayed.
    def Add_Course(self, course):
        self._courses_list.append(course)
        self._courses_names_list.append(course._name)
        print("\n{} has been added to {}'s course list".format(course._name, self._name))
        print("{}'s full course list includes:\n{}".format(self._name, self._courses_names_list))

    # Method to remove a course if a person wants to drop it.
    def Drop_Course(self, course):
        self._courses_list.remove(course)
        self._courses_names_list.remove(course._name)
        print("\n{} has been removed from {}'s course list".format(course._name, self._name))
        print("{}'s full course list includes:\n{}".format(self._name, self._courses_names_list))

# Child class of Person
class Professor(Person):
    def __init__(self, salary="", employee_id="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._salary = salary
        self._employee_id = employee_id

    # Method to print the info for a professor
    def Print_Professor_Info(self):
        super().Print_Person_Info()
        print("Salary: ${}".format(self._salary))
        print("Employee ID: {}".format(self._employee_id))
        print()

    # Add a course to the list of courses a professor teaches
    def Add_Professor_Course(self):
        super().Add_Course()

    # Remove a course to the list of courses a professor teaches
    def Drop_Professor_Course(self):
        super().Drop_Course()

    # Display the list of courses a professor teaches
    def List_Professor_Course(self):
        super().ListCourses()


class Student(Person):
    def __init__(self, student_id="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._student_id = student_id

    # Method to print the student info
    def Print_Student_Info(self):
        super().Print_Person_Info()
        print("Student ID: {}".format(self._student_id))
        print()

    # Add a course to the list of courses a student teaches
    def Add_Sudent_Course(self):
        super().Add_Course()

    # Remove a course to the list of courses a student teaches
    def Drop_Student_Course(self):
        super().Drop_Course()

    # List of courses a student teaches
    def List_Student_Courses(self):
        super().ListCourses()

# A class for each course offered at the university
class Course:
    def __init__(self, name="", course_number="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._name = name
        self._course_number = course_number
        self._professor_list = None
        self._professor_names_list = None
        professor_list = []
        professor_names_list = []
        self._professor_list = professor_list
        self._professor_names_list = professor_names_list
        self._student_list = None
        self._student_names_list = None
        student_list = []
        student_names_list = []
        self._student_list = student_list
        self._student_names_list = student_names_list

    # Show the info for the course
    def DisplayCourseInfo(self):
        print("Course name: {}".format(self._name))
        print("Course number: {}".format(self._course_number))
        print()

    # Method to list out all the professors for a course
    def ListProfessorsInCourse(self):
        i = 0
        # Use a for loop to iterate through all the courses for the professor. In each iteration,
        # call the Print_Professor_Info method.
        print("\nList info for professors teaching {}:".format(self._name))
        for i in range(len(self._professor_list)):
            # Try except block to give error for displaying professors teaching a course.
            try:
                self._professor_list[i].Print_Professor_Info()
            except:
                print("Error displaying professors teaching course.")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the course to the list of courses for a specific professor. Note that we are adding
    # the course objects to one list so we can call on their methods later as well as the course names
    # to another list so they are easily displayed.
    def Add_Professor_To_Course(self, professor):
        self._professor_list.append(professor)
        self._professor_names_list.append(professor._name)
        print("\nProfessor {} is a teaching a {} course".format(professor._name, self._name))
        print("{}'s list of professors includes:\n{}".format(self._name, self._professor_names_list))

    # Method to remove a professor from teaching a course.
    def Drop_Professor_From_Course(self, professor):
        self._professor_list.remove(professor)
        self._professor_names_list.remove(professor._name)
        print("\nProfess {} is not teaching a {} course".format(professor._name, self._name))
        print("{}'s list of professors includes:\n{}".format(self._name, self._professor_names_list))

    # Method to list out all the students for a course
    def ListStudentsInCourse(self):
        i = 0
        # Use a for loop to iterate through all the courses for the student. In each iteration,
        # call the PrintStudentInfo method.
        print("\nList info for students taking {}:".format(self._name))
        for i in range(len(self._student_list)):
            # Try except block tell us if there is an error showing the students in a course.
            try:
                self._student_list[i].Print_Student_Info()
            except:
                print("Error displaying students enrolled in a course.")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the student to the list students for a specific class. Note that we are adding
    # the course objects to one list so we can call on their methods later as well as the course names
    # to another list so they are easily displayed.
    def Add_Student_To_Course(self, student):
        self._student_list.append(student)
        self._student_names_list.append(student._name)
        print("\n{} has been added to {}'s course list".format(student._name, self._name))
        print("{}'s student list includes:\n{}".format(self._name, self._student_names_list))

    # Method to remove a course if a student wants to drop it.
    def Drop_Student_From_Course(self, student):
        self._student_list.remove(student)
        self._student_names_list.remove(student._name)
        print("\n{} has been removed from {}'s course list".format(student._name, self._name))
        print("{}'s student list includes:\n{}".format(self._name, self._student_names_list))

# Class to distinguish between undergraduate and graduate level courses.
class Program:
    def __init__(self, name="", under_or_grad="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._name = name
        self._under_or_grad = under_or_grad
        self._courses_list = None
        self._courses_names_list = None
        courses_list = []
        courses_names_list = []
        self._courses_list = courses_list
        self._courses_names_list = courses_names_list

    # Display the info for a given program
    def DisplayProgramInfo(self):
        print("\nProgram name: {}".format(self._name))
        print("Undergrad/Graduate level: {}".format(self._under_or_grad))
        print()

    # Method to list out all the courses for a program
    def ListCoursesInProgram(self):
        i = 0
        # Use a for loop to iterate through all the courses for the program. In each iteration,
        # call the DisplayCourseInfo method.
        print("\nList info for courses in {} program:".format(self._name))
        for i in range(len(self._courses_list)):
            # Try except block tell us if there is an error showing the courses in a program.
            try:
                self._courses_list[i].DisplayCourseInfo()
            except:
                print("Error displaying courses in a program.")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the course to the list of courses for a specific program. Note that we are adding
    # the course objects to one list so we can call on their methods later as well as the course names
    # to another list so they are easily displayed.
    def Add_Course_To_Program(self, course):
        self._courses_list.append(course)
        self._courses_names_list.append(course._name)
        print("\n{} has been added to the {} program".format(course._name, self._name))
        print("{}'s full course list includes:\n{}".format(self._name, self._courses_names_list))

    # Method to remove a course from a program.
    def Drop_Course_To_Program(self, course):
        self._courses_list.remove(course)
        self._courses_names_list.remove(course._name)
        print("\n{} has been removed from {}'s course list".format(course._name, self._name))
        print("{}'s full course list includes:\n{}".format(self._name, self._courses_names_list))

# This will be the CourseCatalog class for a given year. We can add or remove programs to then display
# the list of programs for a given year.
class CourseCatalog:
    def __init__(self, year="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._year = int(year)
        self._programs_list = None
        self._programs_names_list = None
        programs_list = []
        programs_names_list = []
        self._programs_list = programs_list
        self._programs_names_list = programs_names_list

    # Show the info for the course catalog
    def DisplayCourseCatalogInfo(self):
        print("\nThis course catalog is for year {}".format(self._year))

    # Method to list out all the programs for a catalog year
    def ListProgramsInCatalog(self):
        i = 0
        # Use a for loop to iterate through all the programs for the catalog. In each iteration,
        # call the DisplayProgramInfo method.
        print("\nList info for programs in {} catalog:".format(self._year))
        for i in range(len(self._programs_list)):
            # Try except block tell us if there is an error showing the courses in a program.
            try:
                self._programs_list[i].DisplayProgramInfo()
            except:
                print("Error displaying programs in catalog.")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the program to the list of programs for a specific catalog. Note that we are adding
    # the course objects to one list so we can call on their methods later as well as the course names
    # to another list so they are easily displayed.
    def Add_Program_To_Catalog(self, program):
        self._programs_list.append(program)
        self._programs_names_list.append(program._name)
        print("\nProgram {} has been added to the catalog for the year {}".format(
            program._name, self._year))
        print("{}'s catalog has the following programs:\n{}".format(self._year, self._programs_names_list))

    # Method to remove a program from the catalog.
    def Drop_Program_From_Catalog(self, program):
        self._programs_list.append(program)
        self._programs_names_list.remove(program._name)
        print("\nProgram {} has been removed from the catalog for the year {}".format(
            program._name, self._year))
        print("{}'s catalog has the following programs:\n{}".format(self._year, self._programs_names_list))