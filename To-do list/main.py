import pyodbc

# help(pyodbc)

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/huber/PycharmProjects/To-do list/tasks.accdb;')
cursor = conn.cursor()
cursor.execute('select Tasks from List')

while True:
    print("To-do list:\n")

    for row in cursor.fetchall():
        print(row + "\n")

    inp = input("Options:\n" +
                "a - add new task\n" +
                "d - mark task as done\\in progress\n"
                "r - delete a task\n")

    match inp:
        case "a":
            task_detail = input("Write the what the task is")
        case "d":
            while True:
                try:
                    index = input("Which task do you want to mark as done?")
                    int(index)
                except TypeError as err:
                    print(r"{err}")
        case "r":
            pass
