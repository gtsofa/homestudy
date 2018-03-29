# file oop.y

class Person():
    def __init__(self, name, job=None, pay=0):
         """Initialize the Person with a name, a job type and its pay."""
        self.name = name 
        self.job = job
        self.pay = pay

    def firstName(self):
        """Return Person name."""
        return self.name.split()[0]

    def lastName(self):
        """"Return last name of the Person"""
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus = .10):
        """Return Person's payment raise"""
        Person.giveRaise(self, percent + bonus)
        
    def __repr__(self):
        """Return a representation of a manager instance."""
        return "<Manager: {} {}>".format(self.name, self.pay)

#if __name__ == '__main__':
    
    # self test code

chris = Manager('Chris Jones', 5000)
chris.giveRaise(.20)
print(chris)
