class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
print(f'{sonny.name}\'s email is: {sonny.email}. Sony\'s phone number is:{sonny.phone}\n')
print(f'{jordan.name}\'s email is: {jordan.email}. Jordan\'s phone number is:{jordan.phone}')