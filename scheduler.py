import math
# highest priority is 0, increasing is lower priority
class Task:
    priority_counter = 0
    def __init__(self, period, computation_time):
        self.T = period
        self.C = computation_time
        self.P = Task.priority_counter
        Task.priority_counter += 1

def sort_pri(task):
    return task.P

def response_time(tasks):
    tasks.sort(reverse=True, key=sort_pri)

    # list contains only one element
    if (tasks[0].P == 0):
        return tasks[0].C

    candidate = tasks[0].C
    while True:
        # computation time:
        sum = tasks[0].C
        
        # interference time:
        for task in reversed(tasks[1:]):
            sum += math.ceil(candidate/task.T)*task.C
        if candidate == sum:
            return candidate
        candidate = sum

def is_scheduble(tasks):
    tasks.sort(reverse=True, key=sort_pri)
    return tasks[0].T >= response_time(tasks)
