# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Camryn Ryan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101263706"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt 
import numpy as np

def histogram(dict_: list[dict], attribute: str):
    """ Create a histogram given a list of dictionaries and a string. Assume that the string provided is a key in all of the dictionaries in the list of dictionaries. 
    """
    dict_1 = {}

    for i in dict_:
        if i[attribute] not in dict_1.keys():
            dict_1[i[attribute]] = 1
        else: 
            dict_1[i[attribute]] += 1
            
    x = list(dict_1.keys())
    y = []
    for val in x:
        y += [dict_1[val]]

    plt.figure()
    plt.title("Lab 6: Histogram")
    plt.xlabel('Attribute')
    plt.ylabel('Instances')
    plt.bar(x, y)
    plt.xticks(rotation = 90)
    plt.show()

    '''
    if Instances(x[0], (int, float)):
        return max(x)
    else:
        return -1
    '''

# Do NOT include a main script in your submission
