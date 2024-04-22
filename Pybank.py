import os
import csv

# Set the file path using os.path.join for better cross-platform compatibility
file_path = r"C:\Users\Thomas\Desktop\Finished Projects\Project 3 Finished\PyBank_Poll\PyBank\Resources\budget_data.csv"

# Read data from the CSV file
with open(file_path) as my_file:
    # Create a CSV reader object
    csv_reader = csv.reader(my_file)
    
    # Read the header
    header = next(csv_reader)
    
    # Store the data in a list
    data = list(csv_reader)
    
    # Calculate the total number of months
    count = len(data)

    # Extract columns from the data
    all_amount = [int(row[1]) for row in data]
    all_month = [row[0] for row in data]

    # Calculate the average rate of change
    average_rate_change = round((all_amount[-1] - all_amount[0]) / (count - 1))

    # Calculate the differences between consecutive months
    difference_rows_inc = [all_amount[i + 1] - all_amount[i] for i in range(len(all_amount) - 1)]
    
    # Find the month with the greatest increase and decrease
    max_difference_row = max(difference_rows_inc)
    min_difference_row = min(difference_rows_inc)

    inc_month = all_month[difference_rows_inc.index(max_difference_row) + 1]
    dec_month = all_month[difference_rows_inc.index(min_difference_row) + 1]

    # Display the financial analysis
    print("Financial Analysis")
    print("-" * 30)
    print(f'Total months: {count}')
    print(f'Total: ${sum(all_amount):,}')
    print(f"Average Change: ${average_rate_change:,}")
    print(f"Greatest Increase in Profits: {inc_month} ${max_difference_row:,}")
    print(f"Greatest Decrease in Profits: {dec_month} ${min_difference_row:,}")

# Write output to a text file
    with open('financial_analysis.txt', 'w') as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("-" * 30 + "\n")
        txt_file.write(f'Total months: {count}\n')
        txt_file.write(f'Total: ${sum(all_amount):,}\n')
        txt_file.write(f"Average Change: ${average_rate_change:,}\n")
        txt_file.write(f"Greatest Increase in Profits: {inc_month} ${max_difference_row:,}\n")
        txt_file.write(f"Greatest Decrease in Profits: {dec_month} ${min_difference_row:,}\n")

    print("Financial analysis has been exported to financial_analysis.txt file.")