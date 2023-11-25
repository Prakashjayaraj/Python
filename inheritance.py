class Details :
    def emp_detals(self):
        print("enter the emp details")
    def emp_id(self):
        print("employee id is ")
class location(Details):
    def project(self):
            print("your location iis ")

class project(location,Details):
    def project(self):
        print("your project name is ")


pro = project()
pro.emp_id()
pro.emp_detals()
pro.project()

