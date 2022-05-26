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
                "del - delete a task\n")
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
                    data = open(file)
                    task_list = data.readlines()
                    tasks_edit = open(file, "w")
                    index = input("Write the id of the task you want to mark as done.\n")
                    a_task = task_list[int(index) - 1].split("\t")
                    if a_task[2] == "DONE\n":
                        a_task[2] = "IN PROGRESS\n"
                    else:
                        a_task[2] = "DONE\n"
                    task_list[int(index) - 1] = "\t".join(a_task)
                    tasks_edit.write("".join(task_list))
                    tasks_edit.seek(0)
                    data.seek(0)
                except TypeError as err:
                    print(f"{err}")
                except IndexError as err:
                    print(f"{err}")
                finally:
                    break
            pass
        case "del":
            while True:
                try:
                    data = open(file)
                    task_list = data.readlines()
                    tasks_edit = open(file, "w")
                    index = input("Write the id of the task you want to remove.\n")
                    del task_list[int(index) - 1]
                    for i in range(int(index) - 1, len(task_list)):
                        print(f"loop iteration: {i}")
                        task_i_move = task_list[i].split("\t")
                        task_i_move[0] = str(i+1)
                        task_list[i] = "\t".join(task_i_move)
                    tasks_edit.write("".join(task_list))
                    data.seek(0)
                    tasks_edit.seek(0)
                except TypeError as err:
                    print(f"{err}")
                except IndexError as err:
                    print(f"{err}")
                finally:
                    break
            pass
#      case "det":
#           pass
# while True:
#     try:
#         index = input("Write the id of the task you want to know more about.")
#         int(index)
#     except TypeError as err:
#         print(r"{err}")
