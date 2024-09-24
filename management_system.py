from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class User:
    def __init__(self):
        self._username = None

    @property
    def username(self): 
        return self._username

    @username.setter
    def username(self, new_name):
        self._username = new_name

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print("{} added to the meeting.".format(employee.username))
        self.attendees.append(employee.username)

    def __len__(self):
        return len(self.attendees)

class Employee(AbstractEmployee, User):
    def __init__(self, username):
        super().__init__()
        User.__init__(self)
        self.username = username

    def say_id(self):
        print("My id is {}".format(self.id))

    def say_username(self):
        print("My username is {}".format(self.username))

def main():
    employees = {}  # Dictionary to store employees by username
    meetings = []   # List to store meetings

    while True:
        print("\n--- Employee Management System ---")
        print("1. Create Employee")
        print("2. Add Employee to Meeting")
        print("3. List Attendees in a Meeting")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            username = input("Enter employee username: ")
            employees[username] = Employee(username)
            print("Employee '{}' created with id {}.".format(username, employees[username].id))
        elif choice == "2":
            username = input("Enter employee username: ")
            if username in employees:
                meeting = Meeting()
                meeting + employees[username]
                meetings.append(meeting)
            else:
                print("Employee '{}' not found.".format(username))
        elif choice == "3":
            if meetings:
                print("\nAttendees in Meetings:")
                for i, meeting in enumerate(meetings, start=1):
                    print(f"Meeting {i}: {', '.join(meeting.attendees)}")
            else:
                print("No meetings yet.")
        elif choice == "4":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
