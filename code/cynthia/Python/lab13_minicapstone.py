#Lab13 Minicapstone

#Main Goal: quantify data for an activity and display it in the terminal (think yealry recap data, just the highlights)
    #isolating by activity type, date, distace, time
#Extra Goal: allow the user to input the date range or specific activity they want to filter by
#Stretch goal: colorize and theme the terminal display in the sellected table

#install pretty table -- done
#import csv
#parse csv into a listed dictionary
#display the data in the terminal with a table



# from prettytable import from_csv
from prettytable import PrettyTable
from collections import Counter


#inporting file, this also prints all data in the csv
# with open ("code/cynthia/Python/Garmin_activity_data.csv") as fp:
#     mytable = from_csv(fp)
# print(mytable)

#isolating data to print in the table, trying to import csv, select data then put it into pretty print
with open('code/cynthia/Python/Garmin_activity_data.csv', 'r') as garmin_data:
    text = garmin_data.read().split('\n')
    lines = text[1:]
    keys = text[0].split(',')

# isolating key information, creating headers for each key, might not use because pretty print can also intake a key later in the add_column statement
# key_data = keys[0], keys[1], keys[3], keys[4], keys[6]


#compiling activity types and occurances
activity_occurance = []
activity_type = []
total_distance = []

for line in lines:
    lines = line.split(',')
    activity_occurance.append(lines[0]) #how many times the activity happened
    activity_type.append(lines[0]) #what the activity is named with no repeates
items_occurance = Counter(activity_occurance).values()
items_type = Counter(activity_type).keys()
# print(activity_type)


activity_and_distance = []
for line in text[1:]:
    text = line.split(',')
    items_occurance.update({lines[0]:text[4]})
    
print(items_occurance)


#compiling all distance data
# for line in text[1:]:
#     text = line.split(',')
#     total_distance.append(text[4])
# print(list(map(float, total_distance)))
    


#compiling data to be in pretty print terminal display
x = PrettyTable()
x.add_column('activity type', list(items_type))
x.add_column('activity occurance', list(items_occurance))
# print(x)

