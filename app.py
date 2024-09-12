from crud import add_task, get_tasks, update_task, change_priority, delete_task


def menu():
    print("""
    1. Add task
    2. Show all tasks
    3. Update task
    4. Change task priority
    5. Delete task
    6. Exit
    """)
    choice = input("Enter your choice:  ")

    if choice == '1':
        task_name = input("Enter task name:  ")
        priority = input("Enter priority:  ")
        if add_task(task_name, priority):
            print("Successfully added task.")
        menu()

    elif choice == '2':
        for task in get_tasks():
            print(task)
        menu()

    elif choice == '3':
        task_id = int(input("Enter task id:  "))
        attr = input("""
        Select the attribute you want to change:
        1. Task name
        2. Task status
        """)
        if attr == '1':
            new_value = input("Enter new task name:  ")
            if update_task(task_id, task_name=new_value):
                print("Successfully updated task.")
        elif attr == '2':
            new_value = bool(input("Enter new status:  "))
            if update_task(task_id, status=new_value):
                print("Successfully updated task.")
        menu()

    elif choice == '4':
        task_id = int(input("Enter task id:  "))
        priority = int(input("Enter new priority you want to change:  "))
        if change_priority(task_id, priority):
            print("Successfully changed priority:\n")
            for task in get_tasks():
                print(task)
        menu()

    elif choice == '5':
        task_id = int(input("Enter task id you want to delete:  "))
        if delete_task(task_id):
            print("Successfully deleted task.")
        menu()

    elif choice == '6':
        return None

    else:
        print("Invalid input. Try again.")
        menu()


if __name__ == '__main__':
    menu()
