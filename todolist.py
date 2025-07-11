list_of_tasks = []

while True:
    user_input = input("Choose from the following (1-4):\n1. Add a task\n2. Remove a task\n3. View tasks\n4. Quit\n")

    if user_input == '1':
        user_task = input("Enter your task to add: ")
        list_of_tasks.append(user_task)
        print(f"Tasks added so far:\n{list_of_tasks}")

    elif user_input == '2':
        print(f"Tasks:\n{list_of_tasks}")
        rmv_task = input("Enter the task you want to remove: ")
        if rmv_task in list_of_tasks:
            list_of_tasks.remove(rmv_task)
            print(f"Task \"{rmv_task}\" has been removed. Updated list:\n{list_of_tasks}")
        else:
            print(f"Task \"{rmv_task}\" not found in the list.")

    elif user_input == '3':
        print(f"Current task list:\n{list_of_tasks}")

    elif user_input == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid input. Please enter a number from 1 to 4.")
