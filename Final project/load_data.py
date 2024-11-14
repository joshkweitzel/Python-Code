# ECOR 1042 Lab 3 - Template


# Update "" to list all students contributing to the team work
__author__ = "Joshua Weitzel, Abinan Sajeendran, Andrés Roy-Serrano, Camryn Ryan"

# Update "" with your team (e.g. T102)
__team__ = "T015"

#==========================================#
# Place your machine_vendor_list function after this line
def machine_vendor_list(file_name: str, vendor: str) -> list[dict]:
    """ Joshua Weitzel
    Return list of dictionaries containing information about machines given the name of a vendor
    Example:
    >>>machine_vendor_list('machine.csv', 'amdahl')
    [{'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Model': 470v/7a...]
    """   
    machine_list = [] #Empty list where the dictionaries will be stored
    with open(file_name, 'r') as sheet:
        header = sheet.readline().strip().split(',') #Reads first line in csv, to be used later for key names in the dictionaries
        for line in sheet:
            #Break up values in line
            info = line.strip().split(',') #info references data in each column and cell on csv
            if info[0] == vendor:
                machine_dict = {header[1]:info[1], header[2]:int(info[2]), header[3]:int(info[3]), header[4]:int(info[4]),\
                                 header[5]:int(info[5]), header[6]:int(info[6]), header[7]:int(info[7])}
                machine_list.append(machine_dict)
        sheet.close()       
    return machine_list
#==========================================#
# Place your machine_model_list function after this line
def machine_model_list(filename: str, machine_model: str) -> list[dict]:
    """ Abhinan Sajeeendran
    Return a list(dictionary) of machines when a model is inputed. The code will create a dicitonary with the information in each row (see examples for what the code will return) except for the model information. 

    Preconditions: machine_model parameter must be in the column titled "Model" in the machine.csv file and to be inputed exactly how it is in the csv file.

    Examples:
    >>>machine_model_list('machine.csv', '32/60')
    [{'Vendor': 'adviser', 'MYCT': 125, 'MMIN':6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]

    >>>machine_model_list('machine.csv', '470v/7')
    [{'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}]

    >>>machine_model_list('machine.csv', 'Jul-65')
    [{'Vendor': 'basf', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70}]
    """

    infile = open(filename, "r")  # opens the file and reads the line

    model_list = []  # creating an empty list

    with infile as file:
        # reads each column name and converts to a list, spliting each by ', '
        column_list = file.readline().strip().split(',')

        for i in file:
            # splits each row and converts to a list of strings, spliting each by ', '
            row_model = i.strip().split(',')

            # if a model number is inputed as a parameter (will decide which row to create the list from), it will create a dictionary that includes the column title (except model) and its values (as integers and not as strings)
            if row_model[1] == machine_model:

                list_model = {column_list[0]: row_model[0], column_list[2]: int(row_model[2]), column_list[3]: int(row_model[3]),
                              column_list[4]: int(row_model[4]), column_list[5]: int(row_model[5]), column_list[6]: int(row_model[6]), column_list[-1]: int(row_model[-1])}  # creating the dictionary, column_list is a string, row_model is converted to an integer

                # adding the dictionary to the empty list
                model_list.append(list_model)

        return model_list  # returns the updated list
#==========================================#
# Place your machine_cache_list function after this line
def machine_cache_list(file_name: str, cach: int) -> list[dict]:
    """ Camryn Ryan
    Return a list (stored as a dictionary) of machines given the file \
    name and the minimum acceptable cache memory. If no machines meet the \
    requirement, function returns an empty list. The keys of the dictionary \
    are the labels for each element in the spreadsheet, excluding 'CACH"
    Examples:
    >>>machine_cache_list('machine.csv', 130)
    [ {'Vendor': "adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, \
    MMAX': 6000, 'PRP': 198, 'ERP': 199}, {'Vendor': 'burroughs', 'Model':\
    'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124},\
    {'Vendor': 'cdc', 'Model': 'cyber:170/750', 'MYCT': 25,'MMIN': 1310, \
    'MMAX': 2620, 'PRP': 274,'ERP' 102}, {'Vendor': 'cdc', 'Model'\
    'cyber:170/750', 'MYCT': 25,'MMIN': 1310, 'MMAX': 2620, 'PRP': 368,\
    'ERP' 102}]
    
    >>>machine_cache_list('machine.csv', 7000)
    []
    
    >>>machine_cache_list('machine,csv', 250)
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, \
    'MMAX': 6000, 'PRP': 198, 'ERP': 199}]    
    """
    cache_list = []
    with open(file_name, 'r') as file:
        key = file.readline().strip().split(',')
        for line in file:
            value = line.strip().split(',')
            if int(value[5]) >= cach:
                machine = {key[0]:value[0], key[1]:value[1], key[2]:int(value[2]), \
                key[3]:int(value[3]), key[4]:int(value[4]), key[6]:int(value[6]), \
                key[7]:int(value[7])}
                cache_list.append(machine)
        file.close()
    return cache_list
#==========================================#
# Place your machine_prp_list function after this line
def machine_prp_list (file_name: str, prp: int) -> list[dict]:
    """ Andrés Roy-Serrano
    Return a list (dictionary) of machines when a minimum acceptable prp is inputed. The code will go threw the file and create a list
        with all machines (and respective information) that have a prp that are bigger or equal to the minimum acceptable published
        relative preformance.

        Examples:
        >>> machine_prp_list ('machine.csv', 1145)
        [ { 'Vendor': 'sperry',  'Model': '1100/94',  'MYCT': 30,  'MMIN': 8000,  'MMAX': 64000,  'CACH': 128,  'ERP': 978} ]
        
        >>> machine_prp_list ('machine.csv', 2000)
        [ ]
        
    """
    prp_list = [ ]  # creating an empty list
    with open(file_name, 'r') as file:
        key = file.readline().strip().split(',') # reads each column name and converts to a list, spliting each by ', '
        for i in file:
            value = i.strip().split(',')  # splits each row and converts to a list of strings, spliting each by ', '
            if int(value[6]) >= prp:
                thisdict = {key[0]: value[0], key[1]: value[1], key[2]: int(value[2]), \
                                key[3]:int(value[3]), key[4]:int(value[4]), key[5]:int(value[5]), key[7]:int(value[7])}
                prp_list.append(thisdict)
        file.close()
    return prp_list
#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, filter: tuple) -> list:
    """
    Calls different functions which return various information from a given file
    Input: vendor, model, cach, prp or all
    """
    if filter[0].lower() == 'vendor':
        return machine_vendor_list(file_name, filter[1])
    elif filter[0].lower() == 'model':
        return machine_model_list(file_name, filter[1])
    elif filter[0].lower() == 'cach':
        return machine_cache_list(file_name, int(filter[1]))
    elif filter[0].lower() == 'prp':
        return machine_prp_list(file_name, int(filter[1]))
    elif filter[0].lower() == 'all': #Outputs every machine on list
        out = []
        with open(file_name, 'r') as file:
            header = file.readline().strip().split(',') #Assigns the key names
            for line in file:
                info = line.strip().split(',') #info references data in each column and cell on csv
                if info[0].lower() != header[0]:
                    machine_dict = {header[0]:info[0], header[1]:info[1], header[2]:int(info[2]), header[3]:int(info[3]), header[4]:int(info[4]),\
                                    header[5]:int(info[5]), header[6]:int(info[6]), header[7]:int(info[7])}
                    out.append(machine_dict)
        return out
    else:
        return []
#==========================================#
# Place your add_average_main_memory function after this line
def add_average_main_memory(machine_list: list) -> list:
    """ 
    Given a list of dictionaries generated by any of the previous functions, return a new list with an additional entry
    in each dictionary. This new entry contains the average memory for each machine which is found using the
    keys 'MMIN' and 'MMAX'
    Example:
    >>>loaded_list = load_data(('machine.csv'), ('vendor', 'amdahl'))
    >>>add_average_main_memory(loaded_list)
    [{'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0}...]
    """
    for i in range(len(machine_list)):
        avg_mem = (machine_list[i]['MMIN'] + machine_list[i]['MMAX']) / 2
        machine_list[i]['M_AVG'] = avg_mem
    return machine_list
# Do NOT include a main script in your submission
