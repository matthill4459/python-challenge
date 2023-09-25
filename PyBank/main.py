import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")


#Variables that need to be defined
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0


# This will read the csv file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    # this will Iterate through the rows in the CSV file
    for row in csvreader:
        # Extract data from the current row of the csvfile
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months and net total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        # Calculate profit/loss changes and store them in a list
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)

            # Find the greatest increase and decrease in profits
            if profit_loss_change > greatest_increase_amount:
                greatest_increase_amount = profit_loss_change
                greatest_increase_date = date
            elif profit_loss_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_change
                greatest_decrease_date = date

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average of profit/loss changes
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Write the results to a text file
with open('financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print("Results have been written to 'financial_analysis.txt'")
