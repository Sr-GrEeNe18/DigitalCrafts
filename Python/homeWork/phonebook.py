
import pickle 

# def pickle.dump():


# with open('phonebook.pickle', 'rb') as fh:
#     phonebook = pickle.load(fh)
# print(phonebook)
#   





with open('phonebook.pickle', 'rb') as fh:
    Electronic_Phonebook = pickle.load(fh)

users_input = input('''
Electonic_Phonebook
===========================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? ''')

# Electronic_Phonebook = {
#     'Igor': '857-485-2935',
#     'Jazz': '334-584-2345',
#     'John': '803-793-0866',
# }

def lookup(name):
    print(f'\nlook up entry for {name}: {Electronic_Phonebook[name]}')

# set a entry

def set_entry():
    firstname = input(f"\n name of person?")
    number = (f"Their number is....")
    Electronic_Phonebook[firstname] = number


# deleting

def delete(name):
    del Electronic_Phonebook[name]
# list

def list():
    print('listed entries in phonebook: ')
    for x in Electronic_Phonebook:
        print(f'{x}: {Electronic_Phonebook[x]} ')

while users_input != '5':
    users_input = input('What do you want to do next? ')
    
    if users_input == '1':
        name = input('what name are you looking for')
        lookup(name)
    elif users_input == '2':
        set_entry()
    elif users_input == '3':
        name = input('Who would you like to delete? ')
        delete(name)
    elif users_input == '4':
        list()
    elif users_input == '5':
        print('Bye')
        break





