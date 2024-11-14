# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Weitzel"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101301965"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"

#==========================================#
# Place your script for your batch_UI after this line
import load_data
from sort import sort
from histogram import histogram
from curve_fit import curve_fit

print('Enter the name of file containing command lines: ')
text_file = open(input()) #Open file
for line in text_file: #Reads command lines
    items = line.strip().split(';') #Split command lines into individual parameters
    if items[0] == 'L': #Run load_data
        data_loaded = load_data.load_data(items[1], (items[2], items[3]))
        data = load_data.add_average_main_memory(data_loaded) #Add on M_AVG
        print('Data loaded ')
        print(data_loaded) #Display loaded list
    elif items[0] == 'S': #Run sort
        data = sort(data_loaded, items[2], items[1])
        if items[3] == 'Y':
            print('Data sorted ')
            print(data) #Display sorted list
        else:
            print('Data sorted, not displayed') #Do not display list
    elif items[0] == 'H': #Run histogram
        print(histogram(data, items[1])) #Display the created histogram
    elif items[0] == 'C': #Run histogram
        print(curve_fit(data, items[1], items[2]))
    else:
        print('No valid command')
    
    
    




