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
import datetime 
from datetime import date


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
activity_type = []
for line in lines:
    columns = line.split(',')
    activity_type.append(columns[0]) #what the activity is named with no repeates
items_occurance = Counter(activity_type).values()
items_type = Counter(activity_type).keys()


#compiling all distance and time data
total_distance = []
time_count = dict.fromkeys(items_type, datetime.timedelta())
distance_count = dict.fromkeys(items_type, 0)
for line in lines:
    text = line.split(',')
    distance_count[text[0]]+= round(float(text[4]))
    
    (h ,m, s) = text[6].split(':')
    d = datetime.timedelta(hours = int(h), minutes =int(m), seconds= int(s))
    d = date.strftime(h, m, s)
    time_count[text[0]] += d
    

print(time_count)


#converting datetime object bask to strings for list, strf 

# print(distance_count)
# print(time_count)

total_distance = []
total_distance = list(distance_count.values())

#compiling data to be in pretty print terminal display
x = PrettyTable()
x.add_column('Activity Type', list(items_type))
x.add_column('Activity Occurance', list(items_occurance))
x.add_column('Total Distance', total_distance)
# print(x)