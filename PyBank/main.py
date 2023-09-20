import os
import csv

# Lists to store data
months_included = []
profit_losses = []
profit_loss_changes = []

#initialize variables
number_of_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #next(csvreader, None)
    # Read the header row first
    csv_header = next(csvfile)

    # Loop through looking for the budget data for total months
    for row in csvreader:
         number_of_months += 1
         #store current month value of profit/loss
         current_month_profit_loss = int(row[1])
       
         #append each profit loss to calculate total profit losses
         total_profit_loss += current_month_profit_loss         

         if number_of_months == 1:
            #Make current month profit loss is same as previous month profit loss for the first month
            previous_month_profit_loss = current_month_profit_loss            
         else:
            #append each month in months_included to count number of months
            months_included.append(row[0])
            # change in profit loss for the next month 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            #append each profit loss change to profit loss changes    
            profit_loss_changes.append(profit_loss_change)
            #store current month profit loss to the previous current month profit loss for the next profit/loss value
            previous_month_profit_loss = current_month_profit_loss
        
    
    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)    
    average_profit_loss = round(sum_profit_loss/(number_of_months - 1), 2)

    # greatest and least changes in "Profit/Losses" over the entire period
    greatest_pl_change = max(profit_loss_changes)
    least_pl_change = min(profit_loss_changes)
   
    #Get the index for greatest and least month from the profit loss changes list
    greatest_month_idx =  profit_loss_changes.index(greatest_pl_change)
    least_month_idx = profit_loss_changes.index(least_pl_change)

    # greatest and least month changes in "Profit/Losses" over the entire period
    greatest_month =  months_included[greatest_month_idx]
    least_month = months_included[least_month_idx]   
     
    # Print the output to the console
    print(" ******** Financial Analysis *************** ")
    print("---------------------------------------------")
    print(f"Total months : {number_of_months}")
    print(f"Total:  ${total_profit_loss}")
    print(f"Average Change: ${average_profit_loss}") 
    print(f"Greatest Increase in Profits:{greatest_month} (${greatest_pl_change})") 
    print(f"Greatest Decrease in Losses:{least_month} (${least_pl_change})")
    print("----------------------------------------------")     

# write the output into the file
# Set path for the output file
csvpath = os.path.join("analysis", "output.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, 'w', newline='') as output_file:
   # Write the output into the output file
   output_file.write("Financial Analysis\n")
   output_file.write(f"Total Months:  {number_of_months}\n")   
   output_file.write(f"Total:  ${total_profit_loss}\n")
   output_file.write(f"Average Change: ${average_profit_loss}\n")
   output_file.write(f"Greatest Increase in Profits:{greatest_month} (${greatest_pl_change})\n")
   output_file.write(f"Greatest Decrease in Losses:{least_month} (${least_pl_change})\n")