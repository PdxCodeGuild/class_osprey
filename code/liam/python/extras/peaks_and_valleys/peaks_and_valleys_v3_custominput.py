import re
#v3 - implement and count water runoff with custom input

def peaks(data_read):
    # Returns the indices of peaks. A peak has a lower number on both the left and the right.
    peak_count = list(enumerate(data_read))
    peak_indices = []
    for search in range(1, len(peak_count) - 1):
        if data_read[search] > data_read[search-1] and data_read[search] > data_read[search+1]:
            peak_indices.append(peak_count[search][0])         
    return peak_indices

def valleys(data_read):
    # Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
    valley_count = list(enumerate(data_read))
    valley_indices = []
    for search in range(1, len(valley_count) - 1):
        if data_read[search] < data_read[search-1] and data_read[search] < data_read[search+1]:
            valley_indices.append(valley_count[search][0])     
    return valley_indices

def peaks_and_valleys(data_read):
    #print indices in order
    pv_count = list(enumerate(data_read))
    pv = []
    for search in range(1, len(pv_count) - 1):
        if data_read[search] > data_read[search-1] and data_read[search] > data_read[search+1]:
            pv.append(pv_count[search][0])
        if data_read[search] < data_read[search-1] and data_read[search] < data_read[search+1]:
            pv.append(pv_count[search][0])
    return pv

def make_chart(data_read):
    chart_count = 0 
    for num in data_read:
        if num > chart_count:
            chart_count = num
    #finds highest number in the data list, allowing for potential user creation of data
    printout = ''''''
    #creates depiction of data in vertical readout
    while True:
        for value in data_read:
    
            if value >= chart_count:
                printout += 'X '
            elif value < chart_count:
                printout += '  '
        printout += '\n'
        chart_count -= 1
        if chart_count == 0:
            break
    return printout

def water_calc(chart):

    if 'X   X' in chart:
        water_print = chart.replace('X   X', 'X O X')
        if 'X       X' in water_print:
            water_print = water_print.replace('X       X', 'X O O O X')
            if 'X           X' in water_print:
                water_print = water_print.replace('X           X', 'X O O O O O X')

    water_count = water_print.count('O')
    print(f'Water will collect at {water_count} identifiable locations.')
    return water_print


def create_data():
    data_list = []
    size = int(input('Enter list size: '))
    for _ in range(size):
        num = int(input('Enter value: '))
        data_list.append(num)
    return data_list

data = list(create_data())

print(f'For input of {data} - ')

print(f'Peaks are at {peaks(data)}')

print(f'Valleys are at {valleys(data)}')

print(f'Peaks and Valleys, in order, are located at {peaks_and_valleys(data)}')

print(make_chart(data))

print(water_calc(make_chart(data)))