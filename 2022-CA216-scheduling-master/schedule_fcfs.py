from driver import get_tasks, print_schedule


def fcfs():

    tasks = get_tasks()
    print_schedule(tasks)

if __name__ == "__main__":
    fcfs()