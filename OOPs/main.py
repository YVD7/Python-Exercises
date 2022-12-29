class Student:

    # class variable
    school_name = 'ABC school'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Yash",27)

# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify variables
s1.name = 'Jessa'
s1.age = 14
print('Stuent',s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ_School'
print('School_name:',Student.school_name)