class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        average = self.calculate_average()
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")

class GradingSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student '{name}' added.")

    def record_grade(self, student_name, grade):
        for student in self.students:
            if student.name == student_name:
                student.add_grade(grade)
                print(f"Grade {grade} recorded for {student_name}.")
                return
        print(f"Student '{student_name}' not found.")

    def show_results(self):
        if not self.students:
            print("No students to show.")
        else:
            print("\nStudent Results:")
            for student in self.students:
                student.display_info()
                print("-" * 20)

# Main code
if __name__ == "__main__":
    system = GradingSystem()

    while True:
        print("\nStudent Grading System Menu:")
        print("1. Add Student")
        print("2. Record Grade")
        print("3. Show Results")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter the student's name: ")
            system.add_student(name)
        elif choice == "2":
            name = input("Enter the student's name: ")
            try:
                grade = float(input("Enter the grade (0-100): "))
                system.record_grade(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")
        elif choice == "3":
            system.show_results()
        elif choice == "4":
            print("Exiting the Student Grading System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")
