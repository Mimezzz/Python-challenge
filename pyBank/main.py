import csv
total_month=0
total=0
last_figure=867884
total_change=0
max_increase=0
max_decrease=0

with open('resources/budget_data.csv', 'r') as csvfile:
    csvread=csv.reader(csvfile,delimiter=',')

    csvheader=next(csvread)
    for row in csvread:
        total_month+=1
        total=total+float(row[1])
        new_change=float(row[1])-last_figure
        last_figure = float(row[1])
        total_change+=new_change
        if new_change>max_increase:
            max_increase=new_change
            max_increase_time=row[0]
        elif new_change<max_decrease:
            max_decrease=new_change
            max_decrease_time=row[0]



    avg_change=round(total_change/(total_month-1),2)
    print('Financial Analysis\n---------------')
    print(f'Total Month: {total_month}')
    print(f'Total: {total}')
    print(f'Average Change: {avg_change}')
    print(f'Greatest Increase in Profits: {max_increase_time} {max_increase}')
    print(f'Greatest Decrease in Profits: {max_decrease_time} {max_decrease}')

with open('analysis/analysis.txt','w',newline='') as newtxt:
    lines=[
        'Financial Analysis\n---------------',
        f'Total Month: {total_month}\n',
        f'Total: {total}\n',
        f'Average Change: {avg_change}\n',
        f'Greatest Increase in Profits: {max_increase_time} {max_increase}\n',
        f'Greatest Decrease in Profits: {max_decrease_time} {max_decrease}\n']

    newtxt.writelines(lines)