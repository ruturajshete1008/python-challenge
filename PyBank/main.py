import os
import csv

file_path = os.path.join('..', 'PyBank', 'budget_data.csv')
Output_file = open('/Users/ruturajshete/Desktop/python-challenge/PyBank/budget_data_results.txt', 'w')

with open(file_path, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    counter = 0
    Net_revenue = 0
    Month = []
    Revenue = []
    Revenge_Change = []

    for row in reader:
        Month.append(row[0])
        Revenue.append(int(row[1]))

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(Month))
    print("Total Revenue: $", sum(Revenue))

# The total number of months included in the dataset and
# The total net amount of "Profit/Losses" over the entire period

    Output_file.write("Financial Analysis\n")
    Output_file.write("-----------------------------------\n")
    dateLen = str(len(Month))
    Output_file.write("Total Months: " + dateLen)
    printRev = str(sum(Revenue))
    Output_file.write("\nTotal Revenue: $" + printRev)

# The average change in "Profit/Losses" between months over the entire period

    for i in range(1,len(Revenue)):
        Revenge_Change.append(Revenue[i] - Revenue[i-1])   
        Average_Change = round((sum(Revenge_Change)/len(Revenge_Change)), 2)

        Max_Change = max(Revenge_Change)

        Min_Change = min(Revenge_Change)

        Max_Change_Date = str(Month[Revenge_Change.index(max(Revenge_Change))])
        Min_Change_Date = str(Month[Revenge_Change.index(min(Revenge_Change))])


# The greatest increase in profits (date and amount) over the entire period and
# The greatest decrease in losses (date and amount) over the entire period

    print("Avereage Revenue Change: $", Average_Change)
    print("Greatest Increase in Profits:", Max_Change_Date,"($", Max_Change,")")
    print("Greatest Decrease in Profits:", Min_Change_Date,"($", Min_Change,")")

    Average_Revenue_Change = str(Average_Change)

    Output_file.write("\nAvereage Revenue Change: $" + Average_Revenue_Change)
    Output_file.write("\nGreatest Increase in Profits:" + str(Max_Change_Date) +" ($" + str(Max_Change) +")")
    Output_file.write("\nGreatest Decrease in Profits:" + str(Min_Change_Date) +" ($" + str(Min_Change) +")")
