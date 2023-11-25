class Company:

    def __init__(self, username, id):
        self.id = id
        self.name = username

    def login(self):
        print("enter your login details ")

    def register(self):
        print("please register your id ")


class project(Company):
    def __init__(self, username, id, projectname):
        super().__init__(username, id)
        self.projectname = projectname

    def pro(self):
        print("your project is ")