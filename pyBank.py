import csv

# Path to the CSV file
csv_path = "PyBank/Resources/budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
monthly_charges = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csv_path, "r") as file:
    csv_reader = csv.reader(file, delimiter=",")

    # Skip the header row
    header = next(csv_reader)

    # Loop through each row in the CSV file
    for row in csv_reader:

        # Extract the date and profit/ losses for the current row
        date = row[0]
        profit = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount of profit/ losses
        net_total += profit

        # Calculate the change in profit/ losses compared to the previous month
        change = profit - previous_profit
        if previous_profit != 0:
            monthly_charges.append(change)

        # Update tthe previous profit variable for the next iteration
        previous_profit = profit

        # Find the greatest increase and decrease in profits
        if change > greatest_increase[1]:
            greatest_increase = [date, change]
        elif change < greatest_decrease[1]:
            greatest_decrease = [date, change]

# Calculate the average change in profit/ losses
average_change = sum(monthly_charges) / len(monthly_charges)

# Print the analysis results
print("Financial Analysis")
print("-------------------------");
print(f"Total Months: {total_months}")
print(f"Total : ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]}) (${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]}) (${greatest_decrease[1]})")

out = open("output.txt", "w")


out.write("Financial Analysis\n")
out.write("-------------------------\n");
out.write(f"Total Months: {total_months}\n")
out.write(f"Total : ${net_total}\n")
out.write(f"Average Change: ${average_change:.2f}\n")
out.write(f"Greatest Increase in Profits: {greatest_increase[0]}) (${greatest_increase[1]})\n")
out.write(f"Greatest Decrease in Profits: {greatest_decrease[0]}) (${greatest_decrease[1]})\n")

out.close()