from driver import get_tasks,print_schedule

def prio():
    tasks = get_tasks()
    prio_task = sorted(tasks, key=lambda Task: Task.prio)   #sorts the tasks based on priority

    print_schedule(prio_task)       #calls the function from driver.py to print the tasks


if __name__ == '__main__':
    prio()