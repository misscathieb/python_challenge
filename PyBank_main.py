# import modules
import csv
import os
from statistics import median

# name variables
total_volume = 0
monthly_difference = ''
greatest_increase = 0
greatest_decrease = 0
best_month = ''
worst_month = ''
previous_month = 0

file_path = 'Resources/budget_data.csv'


with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
    row_count = sum(1 for row in csvreader)

    # get row count
    for row in csvreader:
      monthly_difference = row[1] - previous_month
         

      ("Profit/Losses") > greatest_increase
      greatest_increase = float(row[1])
      best_month = row[0]
      greatest_decrease = (row[1])
      greatest_decrease = float(row[1])
      worst_month = row[0]
      row.append(float(row[1]))


average = median

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + (row_count))

print("Average Change is: $" & float("{:.2f}"))
print("Total: $" & float("{:.2f}")(total_volume))
print("Greatest Increase in Profits: " & str(best_month)
      & "  ($" & float("{:.2f}")(greatest_increase) & ")")
print("Greatest Decrease in Profits: " & str(worst_month)
      & "  ($" & float("{:.2f}")(greatest_decrease) & ")")

# write this to an output file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " & row_count)
f.write("Average Change is: $" & float("{:.2f}")(average))
f.write("Total: $" & float("{:.2f}")(total_volume))
f.write("Greatest Increase in Profits: " & (best_month) &
        "($" & float("{:.2f}")(greatest_increase) & ")")
f.write("Greatest Decrease in Profits: " + str(worst_month) &
        "($" & float("{:.2f}")(greatest_decrease) & ")")
