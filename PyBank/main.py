
total_months = 0
total_pl = 0.00
chgProfits = 0
profit = 0

moChanges = []
date = []


import csv
file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    

    Date = csv_header.index('Date')
    PL = csv_header.index('Profit/Losses')

    for row in csvreader:
        #Count months
        total_months = total_months + 1
        
        #Calc total PL
        total_pl = total_pl + int(row[PL])

        #Calc Monthly Change, store in list, reset for next row
        moNum = float(row[1])
        change = moNum - profit
        moChanges.append(change)
        chgProfits = chgProfits + change
        profit = moNum

        #Add dates to new date list
        date.append(row[0])

        #Greatest incr and decr
        grIncr = max(moChanges)
        incrDate = date[moChanges.index(grIncr)]
        grDecr = min(moChanges)
        decrDate = date[moChanges.index(grDecr)]

    #Remove change for first row of changes as there is no data before   
    final_moChanges = moChanges[1:86]
    avg_final = sum(final_moChanges) / len(final_moChanges)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${int(total_pl)}")
    print(f"Average Change: ${str(round(avg_final,2))}")
    print(f"Greatest Increase in Profits: {incrDate} (${int(grIncr)})")
    print(f"Greatest Decrease in Losses: {decrDate} (${int(grDecr)})")
    print("----------------------------")

out_file = "./Analysis/output.txt"
with open(out_file, 'w') as outputFile:
    outputFile.write("Financial Analysis")
    outputFile.write("----------------------------")
    outputFile.write(f"Total Months: {total_months}")
    outputFile.write(f"Total: ${int(total_pl)}")
    outputFile.write(f"Average Change: ${str(round(avg_final,2))}")
    outputFile.write(f"Greatest Increase in Profits: {incrDate} (${int(grIncr)})")
    outputFile.write(f"Greatest Decrease in Losses: {decrDate} (${int(grDecr)})")
    outputFile.write("----------------------------")