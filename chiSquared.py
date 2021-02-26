import math
import numpy as np
from scipy import stats

# funciones

# get a list from a filename
def get_list(filename):  # receives the filename
    data = []
    with open(filename, "r") as f_ptr:
        line = f_ptr.readline()
        while line:
            data.append(float(line))
            line = f_ptr.readline()
        f_ptr.close()

    return data

# get classes from a list into a dictionary
def get_classes(l, min_classes=5):  # range list is a tuple and l is the list with the data
    maxi = max(l)
    mini = min(l)

    k = math.floor(1 + 3.22 * math.log(len(l), 10))
    range_classes = (maxi-mini) / float(k)
    l = sorted(l)
    classes = {}
    mini_loc = 0
    maxi_loc = range_classes
    keys_to_del = []
    j = 1
    sum_to_move = 1

    while j < k+1:
        for i in l:
            if i > mini_loc and i <= maxi_loc:
                if (mini_loc, maxi_loc) not in classes:
                    classes[(mini_loc, maxi_loc)] = 1
                else:
                    classes[(mini_loc, maxi_loc)] += 1
        mini_loc = maxi_loc
        maxi_loc += range_classes
        j += 1
    return classes

#obtaining expected data from classes
#p not multiplied by the class range as assuming uniform dist over [0,1) so 1/(b-a)==1
def get_expected(classes, data_l):
    e_i = 0.0
    expected = []

    for class_range in classes.keys():
        e_i = (class_range[1]-class_range[0])*len(data_l)
        expected.append(e_i)

    return expected

# lee los primeros 10 chi criticos con las 9 mas comunes significancias (.995, .99, .975, .95, .9, .1, .05, .025, .01)
# de acuerdo con la pagina: https://people.smp.uq.edu.au/YoniNazarathy/stat_models_B_course_spring_07/distributions/chisqtab.pdf


def get_chi_table(filename):
    chi_critical_table = np.zeros((10, 9))
    with open(filename, "r") as f_ptr:
        # header con las signif
        line = f_ptr.readline()
        chi_header = line.split("\t")

        # primera linea con datos
        line = f_ptr.readline()
        i, j = 0, 0
        while line:
            j = 0
            numbers = line.split("\t")
            while j < chi_critical_table.shape[1]:
                chi_critical_table[i][j] = numbers[j]
                j += 1
            line = f_ptr.readline()
            i += 1
        f_ptr.close()
    return chi_critical_table, chi_header

#Final step: checking if the hypothesis is true or not
def check_hypothesis(observed, expected, signif):
    chi2_stat, p_val = stats.chisquare(observed, expected)
    if p_val < float(signif):
        return False, p_val #reject null hypothesis
    else:
        return True, p_val #fail to reject null hypothesis


# # #### Ejemplo #######
# #obteniendo datos (paso opcional, se puede meter una lista cualquiera en las funciones que siguen)
# l = get_list("data.txt")
# # #Obteniendo las clases de chi cuadrada
# c = get_classes(l)
# #datos esperados (con base en las clases)
# expected = get_expected(c, l)
# #no es necesario
# # #obtener la tabla teorica de valores de chi donde chi_crit es la tabla, y header son los valores de significancias
# # chi_crit, header = get_chi_table("chi_critical.txt")
# observed = list(c.values())
# print("obs", observed)
# print("exp", expected) 
# chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
# signif = 0.05
# res = check_hypothesis(p_value, signif)
# if res:
#     print(f"Uniforme: {p_value} > {signif}")
# else:
#     print(f"NO uniforme {p_value} <= {signif}")
