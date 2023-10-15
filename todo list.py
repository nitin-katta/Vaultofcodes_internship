def display_list(todo_list):
    if len(todo_list) == 0:
        print("No tasks are present for now")
    else:
        for i in range(len(todo_list)):
            print("Displaying  Tasks")
            print(i+1,todo_list[i]\t)

def add_task(todo_list, task):
    todo_list.append(task)
    print(task,"The task has been added to the list successfully")
    

def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
        print(task, "The task has been deleted from the list ")
    else:
        print("There is no such task")
              

todo_list = [] 

while True:
    print("1. To display tasks")
    print("2. To add a task")
    print("3. To remove a task")
    print("4. Exit ")
    user_input = int(input("Enter your choice"))
    if user_input == 1:
        display_list(todo_list)
    elif user_input == 2:
         task = input("Enter your task")
         add_task(todo_list, task)
    elif user_input == 3:
         task = input("Enter your task to delete")
         remove_task(todo_list, task)
    elif user_input == 4:
        exit()
    else:
        print("Enter your choice correctly")

    
    

