from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def banks(self):
        print("Banking interest")

class Hdfc(Bank):

    print(__name__)
    bankk = None
    def banks(self):
        print("Rate of interest is 12%")

class Sbi(Bank):
    bankk = None
    def banks(self):
        print("Rate of interest is 14%")

na = Hdfc()
naa = Sbi()
na.banks()
naa.banks()


