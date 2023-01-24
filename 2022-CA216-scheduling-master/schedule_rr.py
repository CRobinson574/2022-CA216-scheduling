from driver import get_tasks, print_schedule

def rr():
    tasks = get_tasks()     #gets tasks from file using function in driver.py
    timeq = 10               #time quantum is 10ms


    burst_t = [0] * len(tasks)  #this is the remaining burst time
    wait_t = [0] * len(tasks)   #how long each task has to wait


    for i in range(0, len(tasks)):      #setting the burst time so we can calculate when each task finishes
        burst_t[i] = int(tasks[i].time)

    current_t = 0       #current time used to calculate the total wait time for each task


    while(1):
        done = True

        for i in range(len(tasks)):

            if burst_t[i] > 0:
                done = False

                if burst_t[i] > timeq:
                    current_t += timeq
                    burst_t[i] -= timeq

                else:
                    current_t += burst_t[i]
                    wait_t[i] = current_t - burst_t[i]

                    burst_t[i] = 0

        if done == True:
            break


    for i in range(len(tasks)):     #repeat this from line 12 for printing purposes
        burst_t[i] = tasks[i].time


    total_turn = 0
    for i in range(len(tasks)):     #more information needed to print the rr tasks so cannot use the print_schedule in driver file
        turnaround_t = int(burst_t[i]) + int(wait_t[i])
        total_turn += turnaround_t
        print("Proccess: " + tasks[i].name + " arrived at time: 0 and ran for: " + str(burst_t[i]) + "MS. It had a turnaround time of: " + str(turnaround_t))
        print()


    avg_turn = total_turn // len(tasks)
    print("The average turnaround time rounded down to the nearest integer is: ", avg_turn)

    total_wait = 0
    for i in range(len(tasks)):
        total_wait += wait_t[i]

    avg_wait = total_wait // len(tasks)
    print("The average wait time is: ", avg_wait)


if __name__ == '__main__':
    rr()