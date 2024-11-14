# ECOR 1042 Lab 5 - Individual submission for sort_m_avg_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Weitzel"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101301965"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"

#==========================================#
# Place your sort_m_avg_insertion function after this line
def sort_m_avg_insertion(students: list, sort: str) -> list:
    ''' Joshua Weitzel
    Sorts and returns a given list of dictionaries using the insertion sort algorithm. Function will pull
    the values stored in the dictionaries at 'M_AVG', and either sort them in ascending or descending order
    based on the inputed letter for the 'sort' parameter: 'A' for ascending, 'D' for descending.
    '''
    original = students #Stores original list for missing key case  
    for i in range(1, len(students)): #Iterate through list
        if 'M_AVG' in students[i]:
            full_key = students[i] #Full_key will be sorted back into list
            key = students[i]['M_AVG'] #Key stores sorting value
            j = i - 1
            while j >= 0 and key < students[j]['M_AVG']: #Iterate backwards and shift sorted entries
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = full_key #Insert sorted key into proper location
        else: #If key is not present
            print('“M_AVG” key is not present')
            return original
    if sort == 'A': #Ascending sort
        return students
    elif sort == 'D': #Descending sort
        students.reverse()
        return students
    else:
        return 'no valid sort order'
#list =  [{"M_AVG":7.2,"Model":"GP"}, {"M_AVG":9.1,"Model":"MS"}]
#print(sort_m_avg_insertion(list, 'D'))

# Do NOT include a main script in your submission
