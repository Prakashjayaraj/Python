#exception handling
class Eception:
    def div(self):
        try:
           number_1 = float(input("enter the number 1:- "))
           number_2 = float(input("enter the value for number 2:-"))
           result  = number_1 / number_2
           print(result)

        except ZeroDivisionError:
            print(f"you cannot divide by zero{number_2}")
        except Exception:
            print("error occured")
        finally:
            print("i will always excecute ")
    print("end")
obj = Eception()
obj.div()