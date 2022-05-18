file = r"C:\Users\huber\PycharmProjects\To-do list\tasks.txt"

data = open(file)
# task_add = open(file, "a")
# tasks_edit = open(file, "w")
task_list = data.readlines()
current_id = len(task_list)

while True:

    data = open(file)
    # task_add = open(file, "a")
    # tasks_edit = open(file, "w")
    task_list = data.readlines()
    current_id = len(task_list)

    data.flush()
    data.seek(0)
    print("To-do list:\n")
    print(*task_list)
    # for some reason it adds spaces to lines
    inp = input("Options:\n" +
                "a - add new task\n" +
                "don - mark task as done\\in progress\n"
                "del - delete a task\n"
                "det - access details\n")
    match inp:
        case "a":
            data = open(file)
            task_list = data.readlines()
            current_id = len(task_list) + 1
            task_text = input("Write what the task is\n")
            task_add = open(file, "a")
            task_add.write(f"{current_id}\t{str(task_text)}\tIN PROGRESS\n")
            print("Done!")
            task_add.seek(0)
            data.seek(0)
            pass
        case "don":
            while True:
                try:
                    index = input("Write the id of the task you want to mark as done.")
                    a_task = task_list[int(index) - 1].split("\t")
                    if a_task[2] == "IN PROGRESS":
                        a_task[2] = "DONE"
                    else:
                        a_task[2] = "IN PROGRESS"
                    tasks_edit.write(str(task_list))
                except TypeError as err:
                    print(r"{err}")
                except IndexError as err:
                    print(r"{err}")
        case "del":
            while True:
                try:
                    index = input("Write the id of the task you want to remove.")
                    del task_list[int(index) - 1]
                    tasks_edit.write(str(task_list))
                except TypeError as err:
                    print(r"{err}")
                except IndexError as err:
                    print(r"{err}")
#      case "det":
#           pass
# while True:
#     try:
#         index = input("Write the id of the task you want to know more about.")
#         int(index)
#     except TypeError as err:
#         print(r"{err}")
