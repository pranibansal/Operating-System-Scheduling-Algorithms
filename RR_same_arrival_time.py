import csv

class RoundRobin:
    def callingcsv(self):
        data = open("RR_same_arrival_time.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        time_quantum = 4
        RoundRobin.calculatecompletiontime(self, rows, time_quantum)

    def calculatecompletiontime(self, csv_data, time_quantum):
        start_time_list = []
        end_time_list = []
        executed_process = []
        ready_queue = []
        s_time = 0
        while 1:
            temp = []
            for i in range(len(csv_data)):
                if int(csv_data[i][1]) <= s_time and int(csv_data[i][3]) == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if csv_data[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    The above if loop checks that the next process is not a part of ready_queue
                    '''
                    if present == 0:
                        temp.extend([csv_data[i][0], csv_data[i][1], csv_data[i][2], csv_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    The above if loop adds a process to the read_queue only if it is not already present in it
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                    '''
            if len(ready_queue) == 0:
                break
            if len(ready_queue) != 0:
                if int(ready_queue[0][2]) > time_quantum:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time_list.append(s_time)
                    s_time = s_time + time_quantum
                    e_time = s_time
                    end_time_list.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(csv_data)):
                        if csv_data[j][0] == ready_queue[0][0]:
                            break
                    csv_data[j][2] = int(csv_data[j][2]) - time_quantum
                    ready_queue.pop(0)
                elif int(ready_queue[0][2]) <= time_quantum:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time_list.append(s_time)
                    s_time = s_time + int(ready_queue[0][2])
                    e_time = s_time
                    end_time_list.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(csv_data)):
                        if csv_data[j][0] == ready_queue[0][0]:
                            break
                    csv_data[j][2] = 0
                    csv_data[j][3] = 1
                    csv_data[j].append(e_time)
                    ready_queue.pop(0)
        #t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        #w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.print_data(self, csv_data)

    def print_data(self, csv_data):
        print("Process_ID  Arrival_Time  Rem_Burst_Time  Completion_Status  Init_Burst_Time  Completion_Time")
        for i in range(len(csv_data)):
            for j in range(len(csv_data[i])):
                print(csv_data[i][j], end="	        ")
            print()
        print("\n\nProcess in order of execution along with completion time - ")
        for i in range(len(csv_data)):
            print(csv_data[i][0] + "(" + str(csv_data[i][5]) +  " sec" + ")" , sep = "\n")

if __name__ == "__main__":
    fcfs_diff_arrival_time = RoundRobin()
    fcfs_diff_arrival_time.callingcsv()