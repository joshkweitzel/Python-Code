# ECOR 1042 Lab 6 - Individual submission for curve_fit function
# Remember to include docstring and type annotations for your functions
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Andrés Roy-Serrano"
# Update "" with your student number (e.g., 100100100)
__student_number__ = "101299606"
# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-015"
#==========================================#
# Place your curve_fit function after this line
import matplotlib.pyplot as plt
from numpy import polyfit, polyval, sign, linspace

def curve_fit(data: list[dict], attr: str, deg: int) -> str:
    """Return a string representation of the equation of best fit for
       M_AVG compared to an attribute selected by a user. 
       The equation has a degree selected by a user.
         
       Precondition: len(arr_1st) > deg and 1 <= deg <= 5

       >>> curve_fit([{'ERP": 23, 'M_AVG': 1262.0},
              {'ERP': 29, 'M_AVG' : 2756.0},
              {'ERP': 22, 'M_AVG': 1500.0},
              {'ERP': 124, 'M_AVG': 5000.0}], 'ERP', 3)
       'у =- 0.7039500323325283x^3 + 121.66373096410422X^2\
       - 4643.567794271977×^1 + 52268.90563163403'
       
       >>> curve_fit([{'CACH': 54, 'M_AVG': 20000.0},
              {'CACH': 64, 'M_AVG': 20000.0},
              {'CACH': 180, 'M_AVG': 24000.0},
              {'CACH': 21, 'M_AVG': 24000.0},
              {'CACH': 68, 'M_AVG': 40000.0}], 'CACH', 3)
       'у =- 0. 25832157496707103x^3 + 67.56890509490773x^2\
       - 4122.324924122533x^1 + 83323.93278635312'

       >>> curve_fit([{'CACH': 54, 'M_AVG': 20000.0},
              {'CACH': 64, 'M_AVG': 20000.0},
              {'CACH': 180, 'M_AVG': 24000.0},
              {'CACH': 21, 'M_AVG': 24000.0},
              {'CACH': 68, 'M_AVG': 40000.0}], 'CACH', 10)
       'у =- 0.06745370999524318x^4 + 21.501725854191825×^3
       - 2082.918191486624×^2 + 76516.55926316246×^1 - 850289.8402428939'
    """
    
    # gets a dictionary of dictionaries for each attribute value
    values={}
    for i in range(len(data)):
        if data[i][attr] not in values:
            values[data[i][attr]]={"mem_tot": data[i]["M_AVG"], "freq": 1}
        else:
            values[data[i][attr]["mem_tot"]] = values[data[i]
                                                     [attr]]["mem_tot"] + data[i]["M_AVG"]
            values[data[i][attr]]["freq"] = values[data[i][attr]]["freq"] +1
    
    # gets two lists for x and y
    x = []
    y = []
    for key in values:
        x.append(key)
        y.append(values[key]["mem_tot"] / values[key]["freq"])
    
    # interploates if need be
    if deg >= len(x):
        deg = len(x) - 1
        
    # get coef_list
    coef_list = list(polyfit(x,y,deg))
    
    # Equation Maker
    final_eq = ''
    reverse_coef_list = coef_list[::-1]
    
    for n in range(deg, -1, -1):
        if n == deg and sign(reverse_coef_list[n]) == sign(1):
            coef_eq = f'{reverse_coef_list[n]}x^{n}'
            final_eq += coef_eq
        else:
            if n ==0:
                if sign(reverse_coef_list[n]) == sign(-1):
                    coef_eq = f'{-reverse_coef_list[n]}'
                    final_eq += ' - ' + coef_eq
                else:
                    coef_eq = f'{reverse_coef_list[n]}'
                    final_eq += ' + ' + coef_eq    
            else:
                if sign(reverse_coef_list[n]) == sign (-1):
                    coef_eq = f'{-reverse_coef_list[n]}x^{n}'
                    final_eq += ' - ' + coef_eq
                else:
                    coef_eq = f'{reverse_coef_list[n]}x^{n}'
                    final_eq += ' + ' + coef_eq
    final_eq = "y = " + final_eq
    
    return final_eq