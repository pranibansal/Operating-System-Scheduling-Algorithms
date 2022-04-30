import csv

class SJF_NP_DIFF_ARRIVAL_TIME:
    def callingcsv(self):
        data = open("SJF_np_diff_arrival_time.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        SJF_NP_DIFF_ARRIVAL_TIME.calculatecompletiontime(self, rows)

    def calculatecompletiontime(self, csv_data):
        csv_data.sort(key = lambda x : x[1])
        start_time = 0
        start_time_list = []
        end_time = []
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(csv_data)):
            for j in range(len(csv_data)):
                if int(csv_data[j][3]) == 0:
                    temp.extend([csv_data[j][0], csv_data[j][1], csv_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
                elif int(csv_data[j][2]) <= start_time and int(csv_data[j][3]) == 0:
                    temp.extend([csv_data[j][0], csv_data[j][1], csv_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
            

            if len(ready_queue) != 0:
                '''means there are multiple processes in the ready queue. Now sort the process acc to burst time. 
                if 2 process has same burst time then arrival time. Since NP mode then full execution of the process will take'''
                csv_data.sort(key = lambda x : x[2])
                start_time_list.append(start_time)
                start_time = start_time + int(ready_queue[0][2])
                e_time = start_time
                end_time.append(e_time)
                for k in range(len(csv_data)):
                    if csv_data[k][0] == ready_queue[0][0]:
                        break
                csv_data[i][3] = 1
                csv_data[i].append(e_time)

            elif len(ready_queue) == 0:
                if start_time < int(normal_queue[0][1]):
                    start_time = int(normal_queue[0][1])
                start_time_list.append(start_time)
                start_time = start_time + int(normal_queue[0][2])
                e_time = start_time
                end_time.append(e_time)
                for k in range(len(csv_data)):
                    if csv_data[k][0] == normal_queue[0][0]:
                        break
                csv_data[i][3] = 1
                csv_data[i].append(e_time)

            
        SJF_NP_DIFF_ARRIVAL_TIME.print_data(self, csv_data)

    def print_data(self, csv_data):
        print("Process_ID  Arrival_Time  Burst_Time  Completion_Status  Completion_Time")
        for i in range(len(csv_data)):
            for j in range(len(csv_data[i])):
                print(csv_data[i][j], end="	        ")
            print()
        print("\n\nProcess in order of execution along with completion time - ")
        for i in range(len(csv_data)):
            print(csv_data[i][0] + "(" + str(csv_data[i][4]) + " sec" +  ")" , sep = "\n")

        

if __name__ == "__main__":
    SJF_np_diff_arrival_time = SJF_NP_DIFF_ARRIVAL_TIME()
    SJF_np_diff_arrival_time.callingcsv()