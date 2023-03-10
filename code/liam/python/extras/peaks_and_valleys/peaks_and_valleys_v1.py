#Peaks and Valleys - return index values of conditions

def peaks(data_read):
    # Returns the indices of peaks. A peak has a lower number on both the left and the right.
    peak_count = list(enumerate(data_read))
    peak_indices = []
    for search in range(1, len(peak_count) - 1):
        if data_read[search] > data_read[search-1] and data_read[search] > data_read[search+1]:
            peak_indices.append(peak_count[search][0])   
    print(f'Peaks are located at {peak_indices}')       
    return peak_indices

def valleys(data_read):
    # Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
    valley_count = list(enumerate(data_read))
    valley_indices = []
    for search in range(1, len(valley_count) - 1):
        if data_read[search] < data_read[search-1] and data_read[search] < data_read[search+1]:
            valley_indices.append(valley_count[search][0])
    print(f'Valleys are located at {valley_indices}')      
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
    print(f'Peaks and Valleys, in order, are located at {pv}')
    return pv

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

graph_data = dict(enumerate(data))
print(graph_data)

peaks(data)

valleys(data)

peaks_and_valleys(data)