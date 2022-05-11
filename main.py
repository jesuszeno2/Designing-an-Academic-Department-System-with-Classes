"""
Jesus Zeno
This is the main program to create the objects made in the Academic department program file. We will be
able to perform various functions that will lead up to printing out the course catalog showing the programs
in a given year.
"""

from Academic_Department import Person, Professor, Student, Course, Program, CourseCatalog

def main():

    # We make our first student object and print out their info.
    Peter_Parker = Student(name="Peter Parker", address="20 Ingram Street Queens, NY", phone="7185555555",
                           email="friendly.spider@midtownhigh.edu", student_id="194")
    Peter_Parker.Print_Student_Info()

    # We will make a second student object and print out their info.
    Mary_Jane_Watson = Student(name="Mary Jane Watson", address="410 Chelsea Street New York, NY",
                               phone="2125555555", email="spider.lover@midtownhigh.edu", student_id="25")
    Mary_Jane_Watson.Print_Student_Info()

    # We make our first professor and print out their info.
    Otto_Octavius = Professor(name="Dr. Otto Octavius", address="52 East Street Brooklyn, NY",
                               phone="7185555555", email="otto.octavius@midtownhigh.edu",
                                salary="90,000", employee_id="55")
    Otto_Octavius.Print_Professor_Info()

    # Make our first course and print out its info.
    Advanced_Robotics = Course(name="Advanced Robotics", course_number="ROB1967")
    Advanced_Robotics.DisplayCourseInfo()

    # Add students and professors to course
    Advanced_Robotics.Add_Student_To_Course(Peter_Parker)
    Advanced_Robotics.Add_Student_To_Course(Mary_Jane_Watson)
    Advanced_Robotics.Add_Professor_To_Course(Otto_Octavius)

    # Print the info for the students and professor(s) in the given course.
    Advanced_Robotics.ListStudentsInCourse()
    Advanced_Robotics.ListProfessorsInCourse()

    # Make our first program
    Bioinformatics = Program(name="Bioinformatics", under_or_grad="Graduate")
    Bioinformatics.DisplayProgramInfo()

    # Add the course to a program
    Bioinformatics.Add_Course_To_Program(Advanced_Robotics)

    # Make a 2022 course catalog
    Course_Catalog_2022 = CourseCatalog(year="2022")
    Course_Catalog_2022.DisplayCourseCatalogInfo()

    # Add the bioinformatics program to the course catalog
    Course_Catalog_2022.Add_Program_To_Catalog(Bioinformatics)

    # List all the programs in the catalog for a given year
    Course_Catalog_2022.ListProgramsInCatalog()


if __name__ == '__main__':
    main()
