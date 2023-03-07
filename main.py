# multilevel queue scheduling #

from queue import Queue

class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def __str__(self):
        return f'PID: {self.pid}, Priority: {self.priority}, Burst Time: {self.burst_time}'

class MultiLevelQueueScheduler:
    def __init__(self):
        self.q1 = Queue()   # Highest priority queue
        self.q2 = Queue()   # Medium priority queue
        self.q3 = Queue()   # Lowest priority queue
        self.time_quantum = 10
        self.q1_time_quantum = 4
        self.time_elapsed = 0

    def prompt_process_data(self):
        num_processes = int(input("Enter the number of processes: "))
        for i in range(num_processes):
            pid = i + 1
            priority = int(input(f"Enter the priority for process {pid}: "))
            burst_time = int(input(f"Enter the burst time for process {pid}: "))
            process = Process(pid, priority, burst_time)
            self.add_process_to_queue(process)

    def add_process_to_queue(self, process):
        if process.priority >= 1 and process.priority <= 3:
            self.q3.put(process)
        elif process.priority >= 4 and process.priority <= 6:
            self.q2.put(process)
        elif process.priority >= 7 and process.priority <= 9:
            self.q1.put(process)
