from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search, add_course, search_course_by_id_and_user, enroll_user_in_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advanced Search")
    print("6. Add Course")
    print("7. Search Course by ID and User")
    print("8. Enroll User in Course")
    print("9. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            user_id=int(input("Enter the user id: "))
            name=input("Enter the name: ")
            users=advanced_search(user_id=user_id, name=name)
            if users:
                for user in users:
                    print(user)
            else:
                print("No user found.")
        elif choice == '6':
            name = input("Enter course name: ")
            unit = int(input("Enter course unit: "))
            add_course(name, unit)
        elif choice == '7':
            course_id = int(input("Enter course ID: "))
            user_name = input("Enter user name: ")
            courses = search_course_by_id_and_user(course_id, user_name)
            if courses:
                for course in courses:
                    print(f"Course ID: {course[0]}, Name: {course[1]}, Unit: {course[2]}, Student: {course[3]}")
            else:
                print("No course found for the given criteria.")
        elif choice == '8':
            user_id = int(input("Enter user ID: "))
            course_id = int(input("Enter course ID: "))
            enroll_user_in_course(user_id, course_id)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
