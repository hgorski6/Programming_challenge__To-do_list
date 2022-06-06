import os

# Setting up the path for the file
script_dir = os.path.dirname(__file__)
rel_path = r"tasks.dat"
file = os.path.join(script_dir, rel_path)

while True:

    # the file is structured in a form of a table: new line denotes new row and tabulator separates columns.
    data = open(file)
    task_list = data.readlines()

    data.flush()
    data.seek(0)

    # The initial interface
    print("\nTo-do list:\n")
    print(*task_list)
    # for some reason it adds spaces to lines
    inp = input("Options:\n" +
                "a - add new task\n" +
                "don - mark task as done\\in progress\n"
                "del - delete a task\n")

    # Handling of the interface
    match inp:
        # Here we ask for and append to the file user's input, without the tabulator, as it is use to separate "columns" in the file.
        case "a":
            data = open(file)
            task_list = data.readlines()
            current_id = len(task_list) + 1
            task_add = open(file, "a")
            while True:
                task_text = input("Write what the task is\n")
                if "\t" in str(task_text):
                    print("Error: you can\'t put tabulator in your task name")
                    pass
                else:
                    break
            task_add.write(f"{current_id}\t{str(task_text)}\tIN PROGRESS\n")
            task_add.seek(0)
            data.seek(0)
            pass
        case "don":
            # Here we modify the line with desired task and the third column, containing the information about the progress of the task.
            # We do so by unpacking the file, using .readLines() method, modifying the value, repacking it using .join() method and writing it into the file.
            while True:
                try:
                    index = input("Write the id of the task you want to mark as done\\in progress.\n")
                    data = open(file)
                    task_list = data.readlines()
                    a_task = task_list[int(index) - 1].split("\t")
                    tasks_edit = open(file, "w")
                    if a_task[2] == "IN PROGRESS\n":
                        a_task[2] = "DONE\n"
                    else:
                        a_task[2] = "DONE\n"
                    task_list[int(index) - 1] = "\t".join(a_task)
                    tasks_edit.write("".join(task_list))
                    tasks_edit.seek(0)
                    data.seek(0)
                except IndexError:
                    print("Error: the index is out of range")
                finally:
                    break
            pass
        case "del":
            # Here we delete the line chosen by the user.
            # However we also have to lower the index of each task below it by one. We do it similarly as when we mark a task as "done".
            while True:
                try:
                    index = input("Write the id of the task you want to remove.\n")
                    data = open(file)
                    task_list = data.readlines()
                    del task_list[int(index) - 1]
                    tasks_edit = open(file, "w")
                    for i in range(int(index) - 1, len(task_list)):
                        task_i_move = task_list[i].split("\t")
                        task_i_move[0] = str(i + 1)
                        task_list[i] = "\t".join(task_i_move)
                    tasks_edit.write("".join(task_list))
                    data.seek(0)
                    tasks_edit.seek(0)
                except IndexError:
                    print("Error: the index is out of range")
                    data.seek(0)
                finally:
                    break
