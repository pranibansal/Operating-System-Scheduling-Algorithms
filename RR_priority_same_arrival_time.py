import csv
from collections import OrderedDict
import pandas as pd



class PriorityRoundRobin:
    total_completed_time =0
    counter=0
    finalised_data = []
    def csv_reader(self):
        data = open("Priority_same_arrival_time_new.csv")
        csvreader = csv.reader(data)
        header = next(csvreader)
        
        rows = []
        for row in csvreader:
            rows.append(row)
        
        
        

        rows.sort(key=lambda x: x[3])

        dict_priority_rows = OrderedDict()
        for row in rows:
            if not row[3] in dict_priority_rows:
                dict_priority_rows[row[3]] = []
            dict_priority_rows[row[3]].append(row)
        
        time_slice=2
        
        for priority_key in dict_priority_rows:
            print("Handling process with priority " + priority_key)
            #PriorityRoundRobin.calculatecompletiontime(self, dict_priority_rows[priority_key],time_slice)
            PriorityRoundRobin.doRoundRobin(self,dict_priority_rows[priority_key],time_slice)
        print("\n\nFinal Process Output Along with Completion Time",*PriorityRoundRobin.finalised_data,sep = "\n")

    def doRoundRobin(self, process_data, time_slice):
        if (len(process_data)==1):
            PriorityRoundRobin.counter += int(process_data[0][2])
            print('\nProcess','Remaining_BT','Completed_Time, Total_completed_time\n')
            print(process_data[0][0])
            print( int(process_data[0][1]), int(PriorityRoundRobin.counter))
            PriorityRoundRobin.finalised_data.append(process_data[0][0]+"{"+str(PriorityRoundRobin.counter)+"}")
            return
        # use pandas to create a 2-d data frame from tab delimited file, set column 0 (process names) to string, set column
        # 1 & 2 (start time and duration, respectively) to integers
        d = pd.DataFrame(process_data)
        # sort d into d1 by values of start times[1], ascending
        d1 = d.sort_values(by=1)
        # Create a 4th column, set to 0, for the Completion time
        d1[3] = 0
        # change column names
        d1.columns = ['Process', 'Arrival_time', 'Remaining_BT','Priority','Burst_Time', 'Completed_Time']
        # intialize counter
        #counter = 0
        while (d1['Remaining_BT']).any() > 0:
            for index, row in d1.iterrows():
                # if value in column 'Duration' > the timeslice, add the value of the timeslice to the current counter,
                # subtract it from the the current value in column 'Duration'
                if int(row.Remaining_BT) > time_slice:
                    PriorityRoundRobin.counter += time_slice
                    #row.Duration -= timeslice
                    # !!!LOOK HERE!!!
                    d1['Remaining_BT'][index] = int(d1['Remaining_BT'][index])- time_slice
                    print(row.Process, int(row.Remaining_BT))
                    str1=str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}"
                    if('P3{18}'!=str1):
                        PriorityRoundRobin.finalised_data.append(str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}")
                    #PriorityRoundRobin.finalised_data.append(str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}")
                # if value in column "Duration" <= the timeslice, add the current value of the row:Duration to the counter
                # subtract the Duration from itself, to make it 0
                # set row:Completion to the current counter, which is the completion time for the process
                elif int(row.Remaining_BT) <= time_slice and int(row.Remaining_BT) != 0:
                  PriorityRoundRobin.counter += int(row.Remaining_BT)
                  d1['Remaining_BT'][index] = 0
                  d1['Completed_Time'][index] = PriorityRoundRobin.counter
                  print('\nProcess','Remaining_BT', 'Total_completed_time')
                    
                  print( row.Process, int(row.Remaining_BT), int(d1['Completed_Time'][index]))
                  str1=str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}"
                  if('P3{18}'!=str1):
                    PriorityRoundRobin.finalised_data.append(str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}")
                  #PriorityRoundRobin.finalised_data.append(str(row.Process)+"{"+str(PriorityRoundRobin.counter)+"}")
        
                  #PriorityRoundRobin.finalised_data.append(int(row.Remaining_BT)+"{"+int(d1['Completed_Time'][index])+"}")
                    

                # otherwise, if the value in Duration is already 0, print that index, with the "Done" indicator
                #else:
                  #print(index, "Done")
                    
                    
        
            

if __name__ == "__main__":
    priority = PriorityRoundRobin()
    priority.csv_reader()



