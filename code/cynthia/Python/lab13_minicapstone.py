#Lab13 Minicapstone

#Main Goal: quantify data for an activity and display it in the terminal (think yearly recap data, just the highlights)
#isolating by activity type, date, distace, time
#colorize and theme the terminal display in the sellected table

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Theme
from collections import Counter
import datetime

with open('code/cynthia/Python/Garmin_activity_data.csv', 'r') as garmin_data:
    text = garmin_data.read().split('\n')
    lines = text[1:]
    keys = text[0].split(',')


#compiling activity types and occurances
activity_type = []
for line in lines:
    columns = line.split(',')
    activity_type.append(columns[0]) 
items_occurance = list(Counter(activity_type).values()) #how many times the activity happened
items_type = list(Counter(activity_type).keys()) #what the activity is named with no repeates


#compiling all distance 
total_distance = []
distance_count = dict.fromkeys(items_type, 0)
for line in lines:
    text = line.split(',')
    distance_count[text[0]]+= round(float(text[4]))
total_distance = list(distance_count.values())


#average distance
average_distance = [a/b for a, b in zip(total_distance, items_occurance)]
rounded_average_distance = [round(num, 1) for num in average_distance]


#compiling activity durations
time_count = dict.fromkeys(items_type, datetime.timedelta())
for line in lines:
    text = line.split(',')
    (h ,m, s) = text[6].split(':')
    d = datetime.timedelta(hours = int(h), minutes =int(m), seconds= int(s))
    time_count[text[0]] += d

durations = dict.fromkeys(items_type, '')
for key in time_count:
    duration = str(time_count[key])
    (h ,m, s) = duration[-8:].split(':')
    days_in_hours = time_count[key].days * 24
    hours = days_in_hours + int(h)
    durations[key] = ':'.join((str(hours),m,s))

just_durations_list = list(durations.values())


#PrettyTable Theme 
class Themes:
    MyTheme = Theme(
        default_color= '\033[35m',
        vertical_color="\033[36m",
        horizontal_color="\033[36m",
        junction_color="\033[33m",
        junction_char = '*',
    )

#compiling data to be in pretty table terminal display
x = PrettyTable()
x = ColorTable(theme=Themes.MyTheme)

x.add_column('Activity Type', items_type)
x.add_column('Activity Occurance', items_occurance)
x.add_column('Total Distance', total_distance)
x.add_column('Total Duration', just_durations_list )
x.add_column('Average Distance', rounded_average_distance)

#additional styalization of the Table
x.header_style = 'upper'
x.sortby = 'Activity Occurance'
x.reversesort = True 
x.align = 'l'
print(x)
