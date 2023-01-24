import sys

class Task:
    def __init__(self, name, prio, time):
        self.name = name
        self.prio = prio
        self.time = time

def get_tasks():
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        tasks = []
        for line in lines:
            t = line.split(",")
            tasks.append(Task(t[0], t[1].strip(), t[2].strip()))

    return tasks


def print_schedule(tasks):
    i = 0
    time = 0
    total_turn = 0
    while i < len(tasks):
        turnaround = time + int(tasks[i].time)
        total_turn += turnaround
        print("Process: " + tasks[i].name + " arrived at time: 0"  + " and ran for: " + tasks[i].time + "MS. It had a turnaround time of: " + str(turnaround))
        print()
        time = time + int(tasks[i].time)
        i += 1

    avg_turn = total_turn // len(tasks)

    print("The average turaround time rounded down to the nearest integer for all tasks is:", avg_turn)

    
    total_wait = 0
    for i in range(len(tasks)):
        total_wait += int(tasks[i].time)

    avg_wait = total_wait // len(tasks)
    print("The average wait time for each task rounded down to the nearest integer is: ", avg_wait)