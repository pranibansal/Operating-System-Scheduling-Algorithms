import csv

class FCFS:
    def callingcsv(self):
        data = open("FCFS_same_arrival_time.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        FCFS.calculatecompletiontime(self, rows)

    def calculatecompletiontime(self, csv_data):
        print(csv_data)
        start_time = []
        end_time = []
        s_time = 0
        for i in range(len(csv_data)):
            start_time.append(s_time)
            s_time = int(csv_data[i][2]) + s_time
            e_time = s_time
            end_time.append(e_time)
            csv_data[i].append(e_time)
        t_time = FCFS.calculateTurnaroundtime(self, csv_data)
        FCFS.printData(self,csv_data, t_time)

    def calculateTurnaroundtime(self, csv_data):
        turnaround_time = 0
        for i in range(len(csv_data)):
            t_time = int(csv_data[i][3]) - int(csv_data[i][1])

            csv_data[i].append(t_time) 

    def printData(self, csv_data, t_time):
        print("Process_ID  Arrival_Time  Burst_Time  Completion_Time  Turnaround_Time")
        for i in range(len(csv_data)):
            for j in range(len(csv_data[i])):
                print(csv_data[i][j], end="	        ")
            print()
        print("\n\nProcess in order of execution along with completion time - ")
        for i in range(len(csv_data)):
            
            print(csv_data[i][0] + "(" + str(csv_data[i][3]) + " sec"+  ")", sep = "\n")


    
if __name__ == "__main__":
    fcfs = FCFS()
    fcfs.callingcsv()


