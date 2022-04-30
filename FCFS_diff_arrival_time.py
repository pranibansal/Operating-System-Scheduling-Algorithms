import csv

class FCFS_DIFF_ARRIVAL_TIME:
    def callingcsv(self):
        data = open("FCFS_diff_arrival_time.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        FCFS_DIFF_ARRIVAL_TIME.calculatecompletiontime(self, rows)

    def calculatecompletiontime(self, csv_data):
        csv_data.sort(key = lambda x : x[1])
        start_time = 0
        start_time_list = []
        end_time = []
        for i in range(len(csv_data)):
            start_time_list.append(start_time)
            start_time = start_time + int(csv_data[i][2])
            e_time = start_time
            end_time.append(e_time)
            csv_data[i].append(e_time)
        
        FCFS_DIFF_ARRIVAL_TIME.print_data(self, csv_data)

    def print_data(self, csv_data):
        print("Process_ID  Arrival_Time  Burst_Time  Completion_Time")
        for i in range(len(csv_data)):
            for j in range(len(csv_data[i])):
                print(csv_data[i][j], end="	        ")
            print()
        print("\n\nProcess in order of execution along with completion time - ")
        for i in range(len(csv_data)):
            
            print(csv_data[i][0] + "(" + str(csv_data[i][3]) + " sec"+  ")", sep = "\n")

if __name__ == "__main__":
    fcfs_diff_arrival_time = FCFS_DIFF_ARRIVAL_TIME()
    fcfs_diff_arrival_time.callingcsv()