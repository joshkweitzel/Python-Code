# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Joshua Weitzel, Andrés Roy-Serrano, Camryn Ryan, Abhinan Sajeendran"

# Update "" with your team (e.g. T102)
__team__ = "T-015"

#==========================================#
# Place your sort_cache_bubble function after this line
def sort_cache_bubble(lst: list[dict], AorD: str) -> list[dict]:
    ''' Andrés Roy-Serrano
    Returns a sorting list of dictionaries in an ascending or decending order
    depending on the user input, all using bubble sort.
    Preconditions: None
    >>> sort_cache_bubble( [ {"CACH": 10, "Model": "GP"}, {"CACH": 19, "Model": "MS"} ], "D")
    [ ["CACH": 19, "Model": "MS"}, {"CACH":10, "Model": "GP"} ]
    >>> sort_cache_bubble( [ {"Model": "GP"}, {"Model": "MS"} ], "D")
    "CACH" is not present.
     [ {"Model": "GP"}, {"Model": "MS"} ]
     '''
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if "CACH" in lst[j] and "CACH" in lst[j+1]:
                swap=True
                if AorD =="A":
                    while swap:
                        swap=False
                        for i in range(len(lst)-1):
                            if lst[i]["CACH"] > lst[i+1]["CACH"]:
                                machine = lst[i]
                                lst[i] = lst[i+1]
                                lst[i+1] = machine
                                swap = True

                elif AorD == "D":
                    swap = True
                    while swap:
                        swap = False
                        for i in range(len(lst) - 1):
                            if lst[i]["CACH"] < lst[i + 1]["CACH"]:
                                machine = lst[i]
                                lst[i] = lst[i+1]
                                lst[i+1] = machine
                                swap = True
            else:
                print("key is not present")
    return lst

#==========================================#
# Place your sort_prp_selection function after this line
def sort_prp_selection(prp_list: list[dict], A_or_D: str) -> list[dict]:
    """ Abhinan Sajeendran
    Retun a sorted list of dictionary (using selection sort) and depending on the the user input, it will return a sorted list of dictionary in ascedning order (if user inputs A) or decending order (if user inputs D). The function will return the same list of dictionary (not sorted) if PRP is not a key in the dictionary and will print (“PRP” key is not present)

    Precondition: None

    Examples:
    >>>sort_prp_selection([{"PRP":10, "Model":"GP"}, {"PRP": 19, "Model": "MS"}], "D")
    [{"PRP": 19, "Model": "MS"}, {"PRP": 10, "Model": "GP"}]

    >>>sort_prp_selection([{"Model":"GP"}, {"Model":"GP"}, "D"]
    "PRP" key is not present
    [{"Model":"GP"}, {"Model":"MS"}]
    """

    # ascending order
    if A_or_D == 'A':
        for i in range(len(prp_list)):
            if prp_list[i].get("PRP") == None:
                print("“PRP” key is not present")
                return prp_list
            min_index = i
            for j in range(i + 1, len(prp_list)):
                if prp_list[min_index]["PRP"] > prp_list[j]["PRP"]:
                    min_index = j
            prp_list[i], prp_list[min_index] = prp_list[min_index], prp_list[i]

    # decending order
    elif A_or_D == 'D':
        for i in range(len(prp_list)):
            if prp_list[i].get("PRP") == None:
                print("“PRP” key is not present")
                return prp_list
            min_index = i
            for j in range(i + 1, len(prp_list)):
                if prp_list[min_index]["PRP"] < prp_list[j]["PRP"]:
                    min_index = j
            prp_list[i], prp_list[min_index] = prp_list[min_index], prp_list[i]
    return prp_list

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
            print('M_AVG key is not present')
            return original
    if sort == 'A': #Ascending sort
        return students
    elif sort == 'D': #Descending sort
        students.reverse()
        return students
    else:
        return 'no valid sort order'

#==========================================#
# Place your sort_myct_bubble function after this line
def sort_myct_bubble(dictionaries: list[dict], A_or_D: str) -> list[dict]:
    """ Camryn Ryan
    Return a sorted list if "MYCT" is a key in the dictionary. The string determines if the list will be sorted in ascenidng or descending order. If there is no "MYCT" key, the funcion prints a message that tells user the key is not in the dictionary, and also returns the original list.
    
    >>>sort_myct_bubble([{"MYCT": 29, "Model":"GP"}, {"MYCT": 110, "Model": "MS"}], "A")
    [{"MYCT": 29, "Model":"GP}, {"MYCT": 110, "Model": "MS"}]
    >>>sort_myct_bubble([{"Model":"MS"}, {"Model":"GP"}], "A")
    
    """
    
    if len(dictionaries) == 0:
        print("invalid")
        return dictionaries 
    
    if not "MYCT" in dictionaries[0].keys():
        print ("MYCT key is not present") 
        return dictionaries 
   
    swap = True
    while swap:
        swap = False 
        for i in range(len(dictionaries) -1):
            if A_or_D == "A":
                if dictionaries[i]["MYCT"] > dictionaries[i + 1]["MYCT"]:
                    aux = dictionaries[i]
                    dictionaries[i] = dictionaries[i + 1]
                    dictionaries[i + 1] = aux 
                    swap = True  
            elif A_or_D == "D":
                if dictionaries[i]["MYCT"] < dictionaries[i + 1]["MYCT"]:
                    aux = dictionaries[i]
                    dictionaries[i] = dictionaries[i + 1]
                    dictionaries[i + 1] = aux 
                    swap = True  
            
    return dictionaries 

#==========================================#
# Place your sort function after this line
def sort(dict_list: list, order: str, function_call: str) -> list:
    '''
    Return sorted list of dictionaries in either descending or ascending order, given 'A' or 'D'.
    The function will call upon previous functions in order to use different sorting algorithms.
    '''
    if function_call == 'CACH':
        return sort_cache_bubble(dict_list, order)
    elif function_call == 'PRP':
        return sort_prp_selection(dict_list, order)
    elif function_call == 'M_AVG':
        return sort_m_avg_insertion(dict_list, order)
    elif function_call == 'MYCT':
        return sort_myct_bubble(dict_list, order)
    else:
        print('Cannot be sorted by' + function_call)
        return dict_list
# Do NOT include a main script in your submission
