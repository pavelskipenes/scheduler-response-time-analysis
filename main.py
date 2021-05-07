from scheduler import *

tasks = []
tasks.append(Task(7,3))
tasks.append(Task(12,3))
tasks.append(Task(20,5))

print("total response time: " + str(response_time(tasks)))
if is_scheduble(tasks):
    print("tasks are scheduble")
else:
    print("tasks are not scheduble")
