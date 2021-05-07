<!-- render math formulas on export-->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous"><script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script><script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload='renderMathInElement(document.body, {delimiters: [{ left: "$$", right: "$$", display: true },{ left: "$", right: "$", display: false },{ left: "\\[", right: "\\]", display: true }]});'></script>


# Scheduler Response Time Analysis

Simple generic script that calculates if tasks are scheduleble and their worst possible execution time. Idea is to calculate the worst case time response and comparing that to the deadline. If the time is greater than the deadline then the task is not scheduable.

This test is exact. That means if the test passes, the system will be scheduable. If the test fails, the system will not be schedulable.

## Usage
```python
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

```
Create a list of tasks. Tasks are automatically assigned a priority. The first `Task` instance will have higher priority that second and so on.

Response time is a sum of computation time of the task $C_i$ and interference by higher priority tasks $I_i$. That is the time current task needs to wait for higher priority tasks to complete.$D_i$ is the deadline for the task.

$$R_i \leq D_i$$
$$R_i = C_i + I_i$$

Higher priority tasks will execute a number of times during $R$

Number of Releases$=\bigg \lceil {\frac{R_i}{T_j}} \bigg \rceil$

Total interference$=\bigg \lceil {\frac{R_i}{T_j}} \bigg \rceil C_j$


## Response time equation
$$w_{i}^{n+1} = C_i + \sum_{j \in hp(i)} \bigg \lceil {\frac{R_i}{T_j}} \bigg \rceil C_j$$
Solved by forming a recurrence relationship

$$w_i^{n+1} = C_i  \sum_{j \in hp(i)} \bigg \lceil {\frac{w_i^n}{T_j}} \bigg \rceil C_j$$

Solution is found when $w_i = w_i^{n+1}$

## Source
[video](https://www.youtube.com/watch?v=qaVRW5XN_ew)