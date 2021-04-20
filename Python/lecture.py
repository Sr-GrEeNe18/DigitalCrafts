


# class Person: 
#     def __init__(self, name, email, phone):
#         self.name =  name
#         self.email = email
#         self.phone = phone
#         # print(f"{name} It's a great day!")

#     def greeting(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))


# Sonny = person('sonny@hotmail', '254.675.0090')
# Jordan = other_person('jordan@aol', '703.678.0000')

# Sonny.greeting
# Jordan.greeting

# a = 'string'
# a = int(5)

# class CrazyString(str)
#     def __init__(self, word)
#         self.word = word

#     def reverse(self):
#         revString = ''

#         for char in self.words:
#             revString = char + revString

#         return revString

# kanye = CrazyString('west')


# print(kanye.capitalize())

# print(kanye.reverse())



# q = student("q", "hall")

# brandon = student("brandon", "stinson")
# mike = student("mike", "williams")
# cook = student("cook", "mike")

# rio.greeting("tim")
# q.greeting("gladys")
# brandon.greeting("roony")
# mike.greeting("matt")
# cook.greeting("chris")

# Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', 
# and phone of '483-485-4948', store it in the variable sonny.

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', 
# and phone of '495-586-3456', store it in the variable 'jordan'.

# Have sonny greet jordan using the greet method.

# Have jordan greet sonny using the greet method.

# Write a print statement to print the contact info (email and phone) of Sonny.

# Write another print statement to print the contact info of Jordan.

# 
class student:
    def __init__(self, firstName, campus):
        self.firstName = firstName
        self.campus = campus

    def print(self):
        print(f"{self.firstName} is located in {self.campus}")

class Campus:
    def __init__(self):
            self.student = []

    def addStudent(self, firstName, campus):
        student = Student(firstName, campus)
        self.students.append(student)

    def showCurrentStudents(self):
        for studentObj in self.students:
            print(f"{studentObj.firstName}, {studentObj.campus}")

campus = Campus()


student1 = Student('Carol', "Atlanta")
student2 = Student('Giselle', "Las Vegas")
student3 = Student('Brandon', "Dallas")


