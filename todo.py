
# define to do list
todo_list = ['sfsfsf', 'test', 'sfasf']
done = []
def menu():
    answer = input("Select c to create or a to get list:")

    if answer == "c":
        task = input("Enter task name:")
        create(task)
    elif answer == "a":
        print(todo_list)
    elif answer == "d":
        order = input("Select order number of task or name of task:")
        delete_task(order)
    else: print("Invalid answer")


def create(task):
    todo_list.append(task)
    for i in todo_list:
        print(i)

def delete_task(order):
    if order.isdigit():
        index = int(order)
        if 0 <= index < len(todo_list):
            task = todo_list.pop(index)
            print("Deleted")
            menu()
    elif order in todo_list:
            todo_list.remove(order)
            print(f"Deleted task: {order}")

while True:
    menu()
