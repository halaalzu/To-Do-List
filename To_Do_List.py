def to_do_list():
    tasks = []

    while True:
        print("\nMenu:")
        print ("1. Add Task")
        print ("2. View Tasks")
        print ("3. Remove Task")
        print ("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            task = input("Enter the task: ").strip()
            tasks.append(task)
        elif choice == "2":
            if not tasks:
                print("No tasks in the list.")
            else:
                print("Tasks:")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("Tasks:")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
                task = input("Enter the number of the task to remove: ").strip()
                del(tasks[int(task) - 1])
        elif choice == "4":
            break
        else :
            print("Invalid choice. Please choose a valid option.")

to_do_list()
