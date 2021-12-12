#Object Oriented Programming with Python

#example 1
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f'{self.name} barked!'
    def wag(self):
        print(f'{self.name} *wags tail*')
    def change_age(self, age):
        self.age = age
        return self.age

dog1 = Dog('Richard', 12)
dog2 = Dog('Cipher', 6)
dog1.wag()
print(dog1.bark())
dog2.wag()
print(f'{dog2.name} is now {dog2.change_age(7)} years old!')
'''

#example 2
'''
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Programme():
    def __init__(self, name, max_students):
        self.name = name
        self.max = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max and student.grade > 75:
            self.students.append(student)
            print(f'{student.name} was accepted!')
            return True
        print(f'{student.name} was rejected.')
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.grade
        return value / len(self.students)

s1 = Student('Monika', 16, 90)
s2 = Student('Reginald', 17, 97)
s3 = Student('Milo', 15, 40)
c1 = Programme('Engineering', 4)
c1.add_student(s1)
c1.add_student(s3)
c1.add_student(s2)
print(c1.get_avg_grade())
'''


#Inheritance
'''
class Wizard():
    def __init__(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def spell(self):
        print('\nNo attack yet.')

class RookieWizard(Wizard):
    def info(self):
        self.power = 1 * self.level
        self.health = round(self.level * 1.2 * 10)
        print(f'Rookie Wizard has entered the arena with {self.health}HP and {self.power}AP!')

    def spell(self):
        print('\nRookie Wizard used \'Stick\'!')

class BetterWizard(Wizard):
    def __init__(self, level, type, magic):
        super().__init__(level)
        self.type = type
        self.magic = magic

    def info(self):
        self.power = 2 * self.level
        self.health = round(self.level * 2 * 10)
        print(f'Better Wizard of type {self.type} has entered the arena with {self.health}HP and {self.power}AP!')

    def spell(self):
        print(f'\nBetter Wizard({self.type}) used \'{self.magic}\'!')
rw = RookieWizard(9)
print(f'Rookie Wizard is level {rw.get_level()}')
rw.info()
bw1 = BetterWizard(5, 'Ice', 'Frost')
print(f'Better Wizard is level {bw1.get_level()}')
bw1.info()
bw2 = BetterWizard(7, 'Flame', 'Fireball')
print(f'Better Wizard is level {bw2.get_level()}')
bw2.info()
rw.spell()
bw1.spell()
bw2.spell()
wiz = Wizard(100)
wiz.spell()
'''


#Class Attribute AND Class Methods
'''
class People():
    total = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        People.total += 1 # OR People.add_person()

    @classmethod
    def add_person(cls):
        cls.total += 1

    @classmethod
    def to_the_moon(cls):
        cls.GRAVITY = -1.62
        return cls.GRAVITY

    @classmethod
    def back_on_earth(cls):
        cls.GRAVITY = -9.8
        return cls.GRAVITY

p1 = People('Jimmy')
p2 = People('Vaneric')
p3 = People('Louis')
print(People.total)
print(f'Gravity on the Moon: {People.to_the_moon()}')
print(f'Gravity on Earth: {People.back_on_earth()}')
'''


#Static Methods
'''
class Static:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def prind(x):
        print(x)

print(Static.add5(2))
Static.prind('goo goo')
'''