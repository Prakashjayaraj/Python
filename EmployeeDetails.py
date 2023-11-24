class Employee:
    Developers = ["arun", "bala", "gopi"]
    Testers = ["ganesh", "naveen", "ram"]
    Marketers = ["balaganesh", "prakash"]
    Project = ["capital one"]
    ProjectMembers = [Project, Developers, Testers, Marketers]

    @classmethod
    def display_members(cls):
        print("""
        Choose what you want to get:--

        1. Developers
        2. Testers
        3. Marketers
        4. Project
        5. Project Members

        """)
        choice = input("Choose what you want to display: ")

        if choice == '1':
            print(cls.Developers)
        elif choice == '2':
            print(cls.Testers)
        elif choice == '3':
            print(cls.Marketers)
        elif choice == '4':
            print(cls.Project)
        elif choice == '5':
            print(cls.ProjectMembers)
        else:
            print("Invalid choice!")

Employee.display_members()
