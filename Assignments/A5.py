"""
-------------------------
# Student Name: Quynh Dao
# Student ID: 130440130
# Student email: daox0130@mylaurier.ca
#-------------------------
"""
from pqueue import pQueue3


class Process:

    def __init__(self, PID, time, arrival):
        assert (len(str(PID)) == 10 and isinstance(PID, int)), 'Invalid PID' 
        assert (time > 0 and isinstance(time, int)), 'Invalid time'
        assert (arrival > 0 and isinstance(arrival, int)), 'Invalid arrival'
        
        self.PID = PID
        self.time = time
        self.arrival = arrival
        
    def __str__(self):
        return '[' + str(self.arrival) + ']' + '(' + str(self.PID) + ',' + str(self.time) + ')'
    
    def key(self):
        return self.PID
    
    def __eq__(self, other):
        return self.PID == other.PID and self.time == other.time and self.arrival == other.arrival
    
    def __ne__(self, other):
        return not self == other
    
    def __gt__(self, other):
        if self.arrival > other.arrival:
            return True
        elif self.arrival < other.arrival:
            return False
        elif self.time > other.time:
            return True
        elif self.time < other.time:
            return False
        elif self.PID > other.PID:
            return True
        return False
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __lt__(self, other):
        if self.arrival < other.arrival:
            return True
        elif self.arrival > other.arrival:
            return False
        elif self.time < other.time:
            return True
        elif self.time > other.time:
            return False
        elif self.PID < other.PID:
            return True
        return False
    
    def __le__(self, other):
        return self < other or self == other


def read_processes(filename):
    processes = []
    fv = open(filename, 'r')
    for line in fv:
        int1 = line.find(']')
        int2 = line.find('(')
        int3 = line.find(',')
        int4 = line.find(')')

        time = int(line[1:int1])
        PID = int(line[int2 + 1:int3])
        arrival = int(line[int3 + 1:int4])

        process = Process(PID, arrival, time)
        processes.append(process)
    fv.close()
        
    return processes


def schedule(filename, scheduler_type):
    processes = read_processes(filename)
    
    if scheduler_type == 'FIFO':
        schedule = schedule_FIFO(processes)
    elif scheduler_type == 'SJF':
        schedule = schedule_SJF(processes)
    else:
        print('Error: Wrong scheduler_type')
    return 


def schedule_FIFO(processes):
    timer = 0
    
    q = pQueue3(len(processes), 'L')
    
    for process in processes:
        q.insert(process)
        
    process_num_1 = q.peek()
    x = process_num_1.arrival
    
    while not q.is_empty():
        process = q.peek()
        if timer == 0:
            print('[Timer:{}]: Starting FIFO Scheduler'.format(timer))
            timer += 1
        elif timer == x:
            print('Fetching Process: ' + str(process))
            for i in range(process.time):
                print('[Timer:{}]: {}'.format(timer + i, process.PID))
            x += process.time
            timer += process.time
            q.remove()
        else:
            print('[Timer:{}]: idle'.format(timer))
            timer += 1

    return


def schedule_SJF(processes):
    # your code here
    return
