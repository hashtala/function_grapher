#programs will work for only summed terms yet I will add subtract later.
#trigs to be expanded 
#polynomial with leading coefficients to be added

import numpy as np
import matplotlib.pyplot as pl





def factorial(n):
    
    if n== 1 or n == 0:
        return 1
    return n*factorial(n-1)



def get_ith_term_exp(i):
    denominator = factorial(i)
    return 1/denominator

def fexp(x, terms = 11):
    exp = 0
    x = x / 10
    poly_terms = []
    for index in range(0, terms):
        n = get_ith_term_exp(index)
        poly_terms.append(n)
        
    for i in range(0, terms):
        exp += np.power(x, i)*get_ith_term_exp(i)


    return np.power(exp, 10)



def get_ith_term_sine(i):
    nominator = np.power(-1, i)
    denominator = factorial(2*i + 1)
    return nominator/denominator



def normalize_data(x):
    return x % (2*np.pi)




def fsin(x, terms = 10):
    x = normalize_data(x)
    polynomial_array = []
    for gela in range(0, terms):
        term = get_ith_term_sine(gela)
        polynomial_array.append(term)
    
    sine_x = 0;
    
    for i in range(0, terms):
        sine_x += np.power(x, 2*i + 1)*polynomial_array[i] 
    
    return sine_x


def pypplot(function):
    
    dom = make_domain()
    
    data_stripped_sum = make_var_for_sum(function)
    matrix_plotted_sum = sum_them(data_stripped_sum)
    pl.plot(dom, matrix_plotted_sum)
    pl.show()
    return 0
    
    

def make_var_for_sum(function):
    summed_terms = sum_list(function)
    stripped(summed_terms)
    polynom = poly(summed_terms)
    single_positive = single_values(summed_terms)
    trigs = trig(summed_terms)
    exponents = exps(summed_terms)
    
    main_dict = {"trigs": trigs, 'poly': polynom, 'exps': exponents,
                 'single': single_positive}
    
    return main_dict
    




def sum_them(data_dict):
    
    #recieves a dictionary containing all the data information
    
    domain_x = make_domain()
    pols = make_range_pol(domain_x, data_dict['poly'])
    trigos = make_range_trig(domain_x, data_dict['trigs'])
    singl = make_range_single(data_dict['single'])
    exponent = make_range_exp(domain_x, data_dict['exps'])
    final_matrix = pols + singl + trigos+ exponent
    
    return final_matrix

def make_range_single(single):
    lst = []
    for count in range(0,domain_size):
        lst.append(single)
    #end of for loop
    single_np = np.array(lst)
    return single_np
    

def make_range_pol(domain, polys):
    range_list = []
    list_of_ranges = []
    for term in polys:
        for x_val in domain:
            a = x_val**int(term[1])
            range_list.append(a)
        #end of for loop
        range_np = np.array(range_list)
        range_list = []
        list_of_ranges.append(range_np)
        
    summed_pol = np.zeros(domain_size)
    for term in list_of_ranges:
        summed_pol = summed_pol + term
    
    return summed_pol
    

def make_domain():
    domain_lst = []
    for gela in range(0,domain_size):
        domain_lst.append(0.1*gela)
    #end of the loop
    domain = np.array(domain_lst)
    return domain
    

def single_values(lst):
    inted_list = []
    for term in lst:
        try:
            inted_list.append(int(term))
        except:
            continue
    #end of for loop
    sum = 0
    for term in inted_list:
        sum += term  
        
    return sum
    
    


def sum_list(func):
    print('Applying Linearity')
    summations = func.split('+')
    return summations

def product_list(finc):
    summs = sum_list(finc)
    products = []
    for sum in summs:
        for char in sum:
            if char == '*':
                products.append(sum)
                break
            #end
            
        #end
    #end
    
    multipliers = []
    
    if not products:
        return 0;
    else:
        for term in products:
            multipliers.append(term.split('*'))
    #end of the for loop
    
    return tuple(multipliers)
                
    
    
def stripped(lst):
    std_bool = True;
    for term in lst:
        if type(term) == type('str'):
            continue
        else:
            std_bool = False
    if(std_bool):
        for term in range(0,len(lst)):
            lst[term] = lst[term].strip()
    else:
        print('CANNOT DO STRIP OPERATION ON INT OR FLOAT')
        return None
    return None

def poly(lst):         #it should get summed term list for further transformation
    if not lst:
        return None
    
    exponent_lst = [];
    for term in lst:
        for character in term:
            if character == '^':
                exponent_lst.append(term)
            elif character == 'e':
                continue
            else:
                continue
    for term in exponent_lst:
        for char in term:
            if char == 'e':
                exponent_lst.remove(term)
            #end of inner for loop
    #end of outer for loop
    exponent_tuple = []
    for term in exponent_lst:
        exponent_tuple.append(term.split('^'))
    #end of for loop
    exponent_tuple = tuple(exponent_tuple)
    return(exponent_tuple)
        
    
def trig(summed):
    trig_terms = []
    for term in summed:
        try:
            temp = term.split('(')
            if 'sin' in temp:
                trig_terms.append(term)
        except:
            pass
    return tuple(trig_terms)

def exps(summed):
    exponent_array = []
    for term in summed:
        for char in term:
            if char == 'e':
                exponent_array.append(term)
    return tuple(exponent_array)
     

def make_range_trig(domain, trigs):
    if not trigs:
        return np.zeros(domain_size)
    
    range_list = []
    list_of_ranges = []
    for actuaL_trig in trigs:
        for x_vals in domain:
            a = fsin(x_vals)
            range_list.append(a)
        #end of for loop
        trig_np = np.array(range_list)
        range_list = []
        list_of_ranges.append(trig_np)
    summed_trigs = np.zeros(domain_size)
    for term in list_of_ranges:
       summed_trigs = summed_trigs + term
       pass
    #end of the loop
    return summed_trigs
    
def make_range_exp(domain, exponents):
    
    if not exponents:
        return np.zeros(domain_size)
    
    lst_range = []
    list_of_ranges = []
    for expo in exponents:
        for x in domain:
            a = fexp(x)
            lst_range.append(a)
        #end of first for loop
        np_array = np.array(lst_range)
        lst_range = []
        list_of_ranges.append(np_array)
    #end of the loop
    summed_array = np.zeros(domain_size)
    
    for array in list_of_ranges:
        summed_array = summed_array + array
    
    return summed_array
    

domain_size = 200
pl.show()
while(1):
    function = input('please give your fuction \n')
    domain = input('please give how many steps you want to visualise \n')
    domain_size = 10*int(domain)
    pypplot(function)
    
















