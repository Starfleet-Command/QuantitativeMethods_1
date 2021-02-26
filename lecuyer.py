import numpy as np


def ecuyer(seed_l, a_l, m_l, iterat):
    s_table = np.zeros((len(a_l), iterat))
    sum_list = np.zeros((iterat-1,))

    #llenando las semillas
    for i in range(len(a_l)):
        s_table[i][0] = seed_l[i]

    for col in range(1, iterat):
        for row in range(len(a_l)):
            s_table[row][col] = (a_l[row] * s_table[row][col-1]) % m_l[row]
            sum_list[col-1] += ((-1)**row) * s_table[row][col]

    sum_list = sum_list % (m_l[0]-1)

    for i in range(len(sum_list)):
        if sum_list[i]>0:
            sum_list[i] = sum_list[i]/m_l[0]
        else:
            sum_list[i] = (m_l[0]-1)/m_l[0]
    return sum_list.tolist()


# # Ejemplo
# # multiplicadores
# a_l = [40014, 40692]
# # modulos
# m_l = [2147483563, 2147483399]
# # cuantas iteraciones haremos
# des = 150
# # semillas
# l_seeds = [79, 81]
# # num de generadores
# l = 2
# res = ecuyer(l_seeds, a_l, m_l, des)
# for i in res:
#     print (i)
# r = cs.get_range(res)
# c = cs.get_classes(r, res)
# c = cs.reduce_table(c)
# chi_crit, header = cs.get_chi_table("chi_critical.txt")
# final_res, obt, exp = cs.check_hypothesis(res, len(c)-1, 0.05, chi_crit, header)
# if final_res:
#     print(f"its a uniform distribution according to Chi {obt} <= {exp}")
# else:
#     print(f"No es {obt} > {exp}")
