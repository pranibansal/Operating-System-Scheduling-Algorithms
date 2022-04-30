import csv

class Priority:
    def csv_reader(self):
        data = open("Priority_same_arrival_time.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        Priority.calculatingcompletiontime(self, rows)

    def calculatingcompletiontime(self, csv_data):
        csv_data.sort(key = lambda x : x[3])
        process_start_time = 0
        process_start_time_list = []
        process_exit_time_list = []
        for i in range(len(csv_data)):
            process_start_time_list.append(process_start_time)
            process_start_time = process_start_time + int(csv_data[i][2])
            process_exit_time = process_start_time
            process_exit_time_list.append(process_exit_time)
            csv_data[i].append(process_exit_time)
        Priority.calculateturnaroundtime(self, csv_data)

    def calculateturnaroundtime(self, csv_data):
        final_turnaround_time = 0
        for i in range(len(csv_data)):
            turnaround_time = int(csv_data[i][4]) - int(csv_data[i][1])
            final_turnaround_time = final_turnaround_time + turnaround_time
            csv_data[i].append(turnaround_time)

        #average_turnaround_time = final_turnaround_time / len(csv_data)
        #return average_turnaround_time
        Priority.calculatewaitingtime(self, csv_data)
        

    def calculatewaitingtime(self, csv_data):
        final_waiting_time = 0
        for i in range(len(csv_data)):
            waiting_time = int(csv_data[i][5]) - int(csv_data[i][2])
            final_waiting_time = final_waiting_time + waiting_time
            csv_data[i].append(waiting_time)
        
        #average_waiting_time = final_waiting_time / len(csv_data)
        #return average_waiting_time
        Priority.print_data(self, csv_data)


    def print_data(self, csv_data):
        print("Process_ID  Arrival_Time  Burst_Time  Priority_Defined  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(csv_data)):
            for j in range(len(csv_data[i])):
                print(csv_data[i][j], end="	        ")
            print()
        print("\n\nProcess in order of execution along with completion time - ")
        for i in range(len(csv_data)):
            
            print(csv_data[i][0] + "(" + str(csv_data[i][4]) +  " sec" + ")" , sep = "\n")


if __name__ == "__main__":
    priority = Priority()
    priority.csv_reader()