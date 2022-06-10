# Multiple Inheritance : a child class can inherit the properties of multiple parent class.

#parent class 1 :  developer
class developer:
    def __init__(self,p,e):
        self.program = p
        self.experience=e
    def details(self):
        print(f"Program is {self.program} . total experience {self.experience} ")

#parent class 2 :  cricket
class cricket:
    def __init__(self,t,r):
        self.role=r
        self.team=t
    def printdetails(self):
        print(f"Role is {self.role} in team {self.team}.")

#Child class :  person
class person(developer,cricket):
    def __init__(self,n,p,e,t,r):
        developer.__init__(self,p,e)
        cricket.__init__(self,t,r)
        self.name=n
    def printperson(self):
        print(f"{self.name} is developer and a  cricketer.")


a = developer("C++",4)
b = cricket("Blue hunt","all-rounder")
c = person("Rakesh","Python",3,"Blue star","Bowler")

a.details()
b.printdetails()
c.printperson()
c.details()                #inheriting class developer
c.printdetails()           #inheriting class cricket