""" Understanding Why We Need Multi Processing """

## Threads Advantage:
## One of the main advantages of threads is that the memory space is shared,
## and therefore you can use the information stored in the class OhmLaw in any thread,
## even the main thread. This allows you to monitor the progress, update a plot
## or even alter the execution of a method while it is running

## However, Threads are not suitable for running computationally expensive tasks.

from multiprocessing import Process, cpu_count
from threading import Thread, current_thread
from time import time

import numpy as np


## A Simple Example
def calculate_random(number_points):
    thread_name = current_thread().getName()
    print("Invoked {} By Thread {}".format(__name__, thread_name))
    for value in range(10, number_points):
        numbers = np.random.random(value)
        fft = np.fft.fft(numbers)
    return fft


points = (15000,)
start = time()
data = calculate_random(15000)
end = time()
print("Total Time For Single Execution : {:2.2f} seconds".format(end - start))


## Reapeat Multiple Times
# start = time()
# data = calculate_random(15000)
# data = calculate_random(15000)
# data = calculate_random(15000)
# end = time()
# print("Total Time For Multiple Execution : {:2.2f} seconds".format(end - start))


## Now Repeat Using Threads
thread1 = Thread(target=calculate_random, args=points)
thread2 = Thread(target=calculate_random, args=points)
thread3 = Thread(target=calculate_random, args=points)

## Start The Threads
start = time()
thread1.start()
thread2.start()
thread3.start()

## Join The Threads To Pause Execution Of Next Steps
thread1.join()
thread2.join()
thread3.join()
end = time()


print(
    "Total Time For Multiple Execution (Threaded) : {:2.2f} seconds".format(end - start)
)


## Introducing Multi Processing
# process1 = Process(target=calculate_random, args=points)
# process2 = Process(target=calculate_random, args=points)
# process3 = Process(target=calculate_random, args=points)

# start = time()
# process1.start()
# process2.start()
# process3.start()

# process1.join()
# process2.join()
# process3.join()
# end = time()

# print(points
#     "Total Time For Multiple Execution (Processing) : {:2.2f} seconds".format(
#         end - start
#     )
# )


## Important Point About Processes
## The number of processes that you can spawn is not limited, but normally you
## shouldn't see an increase in performance once you have as many processes as
## cores on your computer.

cores = 1 if cpu_count() <= 2 else cpu_count() - 1
print("Number Of Cores Avaialable : {:d}".format(cores))

## Lets Explore A Fundamental Mistake

# start = time()
# for _ in range(cores):
#     process = Process(target=calculate_random, args=points)
#     process.start()
#     process.join()

# end = time()
# print(
#     "Total Time For Multiple Execution (Processing) : {:2.2f} seconds".format(
#         end - start
#     )
# )

## Lets Correct Our Fundamental Mistake
processes = list()
start = time()
for _ in range(cores):
    process = Process(target=calculate_random, args=points)
    processes.append(process)
    process.start()

for process in processes:
    process.join()

end = time()
print(
    "Total Time For Multiple Execution (Processing) : {:2.2f} seconds".format(
        end - start
    )
)


## Lets Explore One More Time
processes = list()
process_count = 10
print(f"Creating {process_count:d} Processes")
start = time()
for _ in range(process_count):
    process = Process(target=calculate_random, args=points)
    processes.append(process)
    process.start()

for process in processes:
    process.join()

end = time()
print(
    "Total Time For Multiple Execution (Processing) : {:2.2f} seconds".format(
        end - start
    )
)


## Threads and Jupyter
## Threads/Process are compatible with Jupyter.
## If you run either a Thread or a Process in one cell, you will be able to continue
## using your notebook without any problems.
