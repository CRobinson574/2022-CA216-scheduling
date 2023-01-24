from driver import get_tasks, print_schedule


def sjf():
    tasks = get_tasks()
    
    sjf_list = sorted(tasks, key=lambda Task: Task.time)    #sorts the tasks based on time, ascending
    

    print_schedule(sjf_list)



if __name__ == '__main__':
    sjf()