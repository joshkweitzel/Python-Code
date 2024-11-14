# ECOR 1042 Lab 3 - Template


# Update 
__author__ = "Joshua Weitzel"
__student_number__ = "101301965"
__team__ = "T15"

#==========================================#
# Place your machine_vendor_list function after this line
def machine_vendor_list(file_name: str, vendor: str) -> list[dict]:
    """
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
#Do not include a main scripth'