finished = 'y'
todoList = []

def add(todoItem):
    newTodo = input("enter new todo Item>>")
    todoList.append(todoItem)    

def display():

    for todoItem in enumerate(todoList):
        print(f'{todoItem}')

def upate(index, newupdatedValue):
    index = int(input('what item would you like to update'))
    newupdatedValue = input('what is your change?')
    print(f"(index)
    todoList[index] = newupdatedValue

def delete(index):
    index = int(input('what item would you like to delete?'))
    del todoList[index]

while finished == 'y':

    print('what would you like to do')
    userInput = input(f"""
1. List todos
2. Add a todo item
3. Delete a todo intem
4. Update a todo item
5. end the app
""")

    choice = int(userInput)

    if choice == 1:
        display()
    elif choice == 2:
        add()
    else:
        finished = 'n'




