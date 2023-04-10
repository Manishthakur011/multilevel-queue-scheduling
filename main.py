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
         def run(self):
        while not self.q1.empty() or not self.q2.empty() or not self.q3.empty():
            if not self.q1.empty():
                self.run_queue_with_round_robin(self.q1, self.q1_time_quantum)
            if not self.q2.empty():
                self.run_queue_with_priority_scheduling(self.q2)
            if not self.q3.empty():
                self.run_queue_with_first_come_first_serve(self.q3)
            self.time_elapsed += self.time_quantum

    def run_queue_with_round_robin(self, queue, time_quantum):
        print(f"Running queue 1 (Round Robin) for {time_quantum} seconds:")
        self.run_queue(queue, time_quantum)

    def run_queue_with_priority_scheduling(self, queue):
        print("Running queue 2 (Priority Scheduling) for 10 seconds:")
        self.run_queue(queue, self.time_quantum)

    def run_queue_with_first_come_first_serve(self, queue):
        print("Running queue 3 (FCFS) for 10 seconds:")
        self.run_queue(queue, self.time_quantum)

    def run_queue(self, queue, time_quantum):
        time_remaining = time_quantum
        while not queue.empty() and time_remaining > 0:
            process = queue.get()
            if process.remaining_time <= time_remaining:
                self.execute_process(process, process.remaining_time)
                time_remaining -= process.remaining_time
            else:
                self.execute_process(process, time_remaining)
                process.remaining_time -= time_remaining
                queue.put(process)
                time_remaining = 0

    def execute_process(self, process, time_executed):
        print(f"Process {process.pid} is executing for {time_executed} seconds. Remaining time: {process.remaining_time - time_executed}")
        process.remaining_time -= time_executed
        if process.remaining_time <= 0:
            print(f"Process {process.pid} completed.")

if __name__ == '__main__':
    scheduler = MultiLevelQueueScheduler()
    scheduler.prompt_process_data()
    scheduler.run()




