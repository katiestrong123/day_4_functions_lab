tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
### MVP
# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks

# def uncompleted_tasks(list):
#     for task in list:
#         if task["completed"] == False:
#             print(task)

# uncompleted_tasks(tasks)

# 2. Print a list of completed tasks

# def completed_tasks(list):
#     for task in list:
#         if task["completed"]:
#             print(task)

# completed_tasks(tasks)

# 3. Print a list of all task descriptions

# def find_description(list):
#     descriptions = []
#     for task in list:
#         descriptions.append(task["description"])
#     return descriptions

# print(find_description(tasks))

# 4. Print a list of tasks where time_taken is at least a given time

# def minumum_time(time, list):
#     tasks_that_meet_time_target = []
#     for task in list:
#         if task["time_taken"] >= 30:
#             tasks_that_meet_time_target.append(task)
#     return tasks_that_meet_time_target


# print(minumum_time(30, tasks))

# 5. Print any task with a given description

# def input_description(input, list):
#     for task in list:
#         if task["description"] == input:
#             print(task)

# input_description("Wash Dishes", tasks)

# 6. Given a description update that task to mark it as complete.

# def update_completed_task(input, list):
#     for task in list:
#         if task["description"] == input:
#             task["completed"] = True
#     return list

# print(update_completed_task("Wash Dishes", tasks))

# 7. Add a task to the list

# def add_new_task(new_task, list):
#     list.append(new_task)

# new_task = { 
#     "description": "Make Bed", "completed": False, "time_taken": 5 }

# add_new_task(new_task, tasks)
# print(tasks)

# 8. Use a while loop to display the following menu and allow the user to enter an option.

def user_menu():
    user_input = True
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    while user_input != "Q": 
        user_input = input("Choose an option: ")
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        print("You selected " + user_input)
    
user_menu()

# 9. Call the appropriate function depending on the users choice.
#  7  week_1/day_4/functions_lab_2/start_code/task_list.py 
# @@ -0,0 +1,7 @@
# tasks = [
#     { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
#     { "description": "Clean Windows", "completed": False, "time_taken": 15 },
#     { "description": "Make Dinner", "completed": True, "time_taken": 30 },
#     { "description": "Feed Cat", "completed": False, "time_taken": 5 },
#     { "description": "Walk Dog", "completed": True, "time_taken": 60 },