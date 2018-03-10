import os
import csv

Budget_data_csv = os.path.join("data", "budget_data_1.csv")

# create lists to store data
datescolumn = []
revenuescolumn = []
monthly_revenue_change = []

with open(Budget_data_csv, newline="") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    
    for row in budgetreader:
    
        # add dates
        datescolumn.append(row[0])
        dates = datescolumn[1:]

        # add revenues
        revenuescolumn.append(row[1])
        revenues = revenuescolumn[1:]

# convert revenues to integers
revenues = list(map(int, revenues))

Total_Months = len(dates)
Total_Revenue = sum(revenues)

# create list of monthly revenue changes
for i in range(1, int(Total_Months)): 

    monthly_revenue_change.append(revenues[i] - revenues[i-1])

    # print(monthly_revenue_change)

Av_Rev_Change = int(sum(monthly_revenue_change) / len(monthly_revenue_change))

# find greatest increases and decreases in revenue
lrg_incr_rev = max(monthly_revenue_change) 
lrg_decr_rev = min(monthly_revenue_change)

# find dates at which greatest increases and decreases in revenue occur
maxdate = dates[monthly_revenue_change.index(max(monthly_revenue_change)) + 1] 
mindate = dates[monthly_revenue_change.index(min(monthly_revenue_change)) + 1] 

print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(Total_Months)) 
print("Total Revenue: $" + str(Total_Revenue))
print("Average Revenue Change: $" + str(Av_Rev_Change))
print("Greatest Increase in Revenue: " + maxdate + " ($" + str(lrg_incr_rev) + ")")
print("Greatest Increase in Revenue: " + mindate + " ($" + str(lrg_decr_rev) + ")")

# create output lines
msg_total_months = "Total Months: " + str(Total_Months)
msg_total_revenue = "Total Revenue: $" + str(Total_Revenue)
msg_av_rev_change = "Average Revenue Change: $" + str(Av_Rev_Change)
msg_lrg_incr_rev = "Greatest Increase in Revenue: " + maxdate + " ($" + str(lrg_incr_rev) + ")"
msg_lrg_decr_rev = "Greatest Increase in Revenue: " + mindate + " ($" + str(lrg_decr_rev) + ")"


full_analysis = ["Financial Analysis", 
                "--------------------",
                msg_total_months,  
                msg_total_revenue,
                msg_av_rev_change,
                msg_lrg_incr_rev,
                msg_lrg_decr_rev
                ]             

# write output file
with open("output.txt", "w") as output:

    for i in full_analysis:

        output.write(str(i) + '\n')

output.close()
