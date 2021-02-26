import numpy as np
import PySimpleGUI as sg
import math
import lineal
from kolmogorov import kolmogorovSmirnov
from cuadrados_medios import mean_squares
import generadorMultiplicativo
import chiSquared as cs
import lecuyer

# Can validate if a string or list of strings is an int


def validateInt(string=None, stringList=None):
    listValidate = []
    if stringList is not None:
        for i in range(len(stringList)):
            try:
                int(stringList[i])
                listValidate.append(True)
            except ValueError:
                listValidate.append(False)

        if any(i == False for i in listValidate):
            return False
        else:
            return True

    elif string is not None:
        try:
            int(string)
            return True
        except ValueError:
            return False
    else:
        return False


def mainGUI():

    layout = [[sg.Text("¿Cual metodo desea utilizar?")],
              [sg.Button("Medios Cuadrados"), sg.Button("C. Lineal"), sg.Button("C. Mixto"), sg.Button("Multiplicativo"),
               sg.Button("C. Combinado"), sg.Button("Prueba de Chi-cuadrada"), sg.Button("Prueba de Kolmogorov-Smirnov"), sg.Exit("Salida")]]

    window = sg.Window("Simulador de numeros random", layout)
    while True:
        button, values = window.read()
        if button in (sg.WIN_CLOSED, 'Salida'):
            break

    # ----------------- MEDIOS CUADRADOS ----------------------------------------------------------------------------
        if button == 'Medios Cuadrados':
            layout = [[sg.Text("Escriba el número semilla de cuatro dígitos"), sg.InputText(size="5")],
                      [sg.Text("Escriba la cantidad de Rs a recibir:"),
                       sg.InputText(size="5")],
                      [sg.Button("Continuar")],
                      [sg.Button("Regresar")]]
            window2 = sg.Window("Medios Cuadrados", layout)

            while True:
                button, MCseed = window2.read()
                if button in (sg.WIN_CLOSED, 'Regresar'):
                    window2.close()
                    break

                # If all text is recognized a  number
                elif validateInt(stringList=MCseed):
                    # Then, if seed number is a valid one (four digits)
                    if int(MCseed[0]) >= 1000:
                        if(int(MCseed[1]) > 0):
                            windowResults = sg.Window("Resultados")
                            resultLayout = [[sg.Text("Los resultados son:")]]
                            result = mean_squares(MCseed[0], MCseed[1])
                            resultBox = []
                            for i in range(len(result)):
                                resultBox.append(
                                    "R{}: {}".format(i, result[i]))
                            resultLayout = resultLayout + [[sg.Listbox(values=resultBox, size=(40, 10))], [
                                sg.Button("Prueba de Bondad de Ajuste", key='test')]]
                            button, MCseed = windowResults.Layout(
                                resultLayout).Read()
                            if button == sg.WIN_CLOSED:
                                windowResults.close()
                            elif button == 'test':
                                which_test(result)
                        else:
                            sg.popup_error(
                                "El numero de Rs debe ser positivo")

                    else:
                        sg.popup_error(
                            "El numero escrito no tiene cuatro dígitos")

                else:
                    sg.popup_error(
                        "El valor escrito no fue reconocido como un numero")

    # ----------------- CONGRUENCIA LINEAL --------------------------------------------------------------------
        elif button == 'C. Lineal':

            layout = [[sg.Text("Escriba el número semilla"), sg.InputText(size="5")],
                      [sg.Text("Escriba el multiplicador:"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el incremento"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el modulo (numero mayor a 0)"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba la cantidad de Rs a obtener:"),
                       sg.InputText(size="8")],
                      [sg.Button("Continuar")],
                      [sg.Button("Regresar")]]

            linearWindow = sg.Window("Congruencia Lineal", layout)
            while True:
                button, MCseed = linearWindow.read()

                if button in (sg.WIN_CLOSED, 'Regresar'):
                    linearWindow.close()
                    break

                elif (validateInt(stringList=MCseed)):
                    modulo = MCseed[3]
                    iterations = MCseed[4]
                    if int(modulo) > 0 and int(iterations) > 0:
                        windowResults = sg.Window("Resultados")
                        resultLayout = [[sg.Text("Los resultados son:")]]
                        for i in MCseed:
                            MCseed[i] = int(MCseed[i])

                        result = lineal.linear_congruential(
                            MCseed[0], MCseed[1], MCseed[2], MCseed[3], MCseed[4])
                        resultBox = []
                        for i in range(len(result)):
                            resultBox.append("R{}: {}".format(i, result[i]))
                        resultLayout = resultLayout + [[sg.Listbox(values=resultBox, size=(40, 10))], [
                            sg.Button("Prueba de Bondad de ajuste", key='test')]]
                        button, MCseed = windowResults.Layout(
                            resultLayout).Read()
                        if button == sg.WIN_CLOSED:
                            windowResults.close()
                        elif button == 'test':
                            which_test(result)
                    else:
                        sg.popup_error(
                            "El modulo o el numero de Rs escrito no es un numero mayor a 0")
                else:
                    sg.popup_error(
                        "Alguno de los valores escritos no es adecuado")

    # ----------------- CONGRUENCIAL MIXTO ----------------------------------------------------------------------------
        elif button == 'C. Mixto':
            layout = [[sg.Text("Escriba el número semilla"), sg.InputText(size="5")],
                      [sg.Text("Escriba el multiplicador:"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el incremento"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el modulo (numero mayor a 0)"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba la cantidad de Rs a obtener:"),
                       sg.InputText(size="8")],
                      [sg.Button("Continuar")],
                      [sg.Button("Regresar")]]
            mixWindow = sg.Window("Congruencial Mixto", layout)
            while True:
                button, MCseed = mixWindow.read()

                if button in (sg.WIN_CLOSED, 'Regresar'):
                    mixWindow.close()
                    break

                elif (validateInt(stringList=MCseed)):
                    for i in MCseed:
                        MCseed[i] = int(MCseed[i])

                    if lineal.hullDobell(MCseed[0], MCseed[1], MCseed[2], MCseed[3])[0]:
                        if int(MCseed[3]) > 0:
                            MCseed[4] = MCseed[3]
                            windowResults = sg.Window("Resultados")
                            resultLayout = [[sg.Text("Los resultados son:")]]
                            result = lineal.linear_congruential(
                                MCseed[0], MCseed[1], MCseed[2], MCseed[3], MCseed[4])
                            resultBox = []
                            for i in range(len(result)):
                                resultBox.append(
                                    "R{}: {}".format(i, result[i]))
                            resultLayout = resultLayout + [[sg.Listbox(values=resultBox, size=(40, 10))], [
                                sg.Button("Prueba de Bondad de Ajuste", key='test')]]
                            button, MCseed = windowResults.Layout(
                                resultLayout).Read()
                            if button == sg.WIN_CLOSED:
                                windowResults.close()
                            elif button == 'test':
                                which_test(result)
                        else:
                            sg.popup_error(
                                "El modulo debe ser positivo")

                    else:
                        if lineal.hullDobell(MCseed[0], MCseed[1], MCseed[2], MCseed[3])[1][0] == False:
                            sg.popup_error(
                                "El comun divisor mas grande para c y m no es 1")
                        if lineal.hullDobell(MCseed[0], MCseed[1], MCseed[2], MCseed[3])[1][1] == False:
                            sg.popup_error(
                                "a-1 no es divisible entre q")
                        if lineal.hullDobell(MCseed[0], MCseed[1], MCseed[2], MCseed[3])[1][2] == False:
                            sg.popup_error(
                                "a-1 no es divisible entre 4")
                else:
                    sg.popup_error(
                        "Alguno de los valores escritos no es adecuado")

    # ----------------- GENERADOR MULTIPLICATIVO ----------------------------------------------------------------------------
        elif button == 'Multiplicativo':
            layout = [[sg.Text("Escriba el número semilla X0:"), sg.InputText(size="5")],
                      [sg.Text("Escriba el multiplicador a:"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el modulo (debe ser mayor a 0, a y X0):"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba la cantidad de Rs a obtener:"),
                       sg.InputText(size="8")],
                      [sg.Button("Continuar")],
                      [sg.Button("Regresar")]]
            multWindow = sg.Window("Generador Multiplicativo", layout)
            while True:
                button, MCseed = multWindow.read()

                if button in (sg.WIN_CLOSED, 'Regresar'):
                    multWindow.close()
                    break

                elif (validateInt(stringList=MCseed)):
                    for i in MCseed:
                        MCseed[i] = int(MCseed[i])
                    if int(MCseed[2]) > 0 and (int(MCseed[2]) > int(MCseed[1])) and (int(MCseed[2]) > int(MCseed[0])):
                        windowResults = sg.Window("Resultados")
                        resultLayout = [[sg.Text("Los resultados son:")]]
                        result = generadorMultiplicativo.multiplicativo(
                            MCseed[0], MCseed[1], MCseed[2], MCseed[3])
                        resultBox = []
                        for i in range(len(result)):
                            resultBox.append("R{}: {}".format(i, result[i]))
                        resultLayout = resultLayout + [[sg.Listbox(values=resultBox, size=(40, 10))], [
                            sg.Button("Prueba de Bondad de Ajuste", key='test')]]
                        button, MCseed = windowResults.Layout(
                            resultLayout).Read()
                        if button == 'test':
                            which_test(result)
                        elif button == sg.WIN_CLOSED:
                            windowResults.close()
                    else:
                        sg.popup_error(
                            "Los valores ingresados no cumplen con la relacion m>0, m>a, m>X0")
                else:
                    sg.popup_error(
                        "Alguno de los valores escritos no es adecuado")

    # ----------------- LINEAL COMBINADO ----------------------------------------------------------------------------
        elif button == 'C. Combinado':
            layout = [[sg.Text("Escriba el número semilla X1:"), sg.InputText(size="5")],
                      [sg.Text("Escriba el multiplicador a1:"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el modulo m1 (debe ser mayor a 0):"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el número semilla X2:"),
                       sg.InputText(size="5")],
                      [sg.Text("Escriba el multiplicador a2:"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba el modulo m2 (debe ser mayor a 0):"),
                       sg.InputText(size="8")],
                      [sg.Text("Escriba la cantidad de Rs a obtener:"),
                       sg.InputText(size="8")],
                      [sg.Button("Continuar")],
                      [sg.Button("Regresar")]]
            combWindow = sg.Window("Generador Combinado", layout)
            while True:
                button, MCseed = combWindow.read()

                if button in (sg.WIN_CLOSED, 'Regresar'):
                    combWindow.close()
                    break

                elif (validateInt(stringList=MCseed)):
                    windowResults = sg.Window("Resultados")
                    resultLayout = [[sg.Text("Los resultados son:")]]
                    for i in range(len(MCseed)):
                        MCseed[i] = int(MCseed[i])
                    
                    #variables to reduce cognitive complexity
                    a_l = [MCseed[1], MCseed[4]]
                    m_l = [MCseed[2], MCseed[5]]
                    seed_l = [MCseed[0], MCseed[3]]
                    iterat = MCseed[6]
                    result = lecuyer.ecuyer(seed_l, a_l, m_l, iterat)
                    resultBox = []
                    for i in range(len(result)):
                        resultBox.append("R{}: {}".format(i, result[i]))
                    resultLayout = resultLayout + [[sg.Listbox(values=resultBox, size=(40, 10))], [
                        sg.Button("Prueba de Bondad de Ajuste", key='test')]]
                    button, MCseed = windowResults.Layout(
                        resultLayout).Read()
                    if button == 'test':
                        which_test(result)
                    elif button == sg.WIN_CLOSED:
                        windowResults.close()
                else:
                    sg.popup_error(
                        "Alguno de los valores escritos no es adecuado")

    # ----------------- CHI - CUADRADA --------------------------------------------------------------------------------------
        elif button == 'Prueba de Chi-cuadrada':
            chi_square_test()

        elif button == 'Prueba de Kolmogorov-Smirnov':
            kolmogorov_test()

    window.close()


def which_test(r_list):
    chi_crit, chi_header = cs.get_chi_table("chi_critical.txt")
    layout = [[sg.Text("Cual test deseas aplicar?")],
              [sg.Text("Nivel de Significancia"),
               sg.Combo(chi_header, key="signif")],
              [sg.Button("Kolmogorov"), sg.Button("Chi-Squared")]]
    choose_window = sg.Window("Eleccion de test", layout)
    while True:
        button, vals = choose_window.read()

        if button == sg.WIN_CLOSED:
            choose_window.close()
            break
        elif button == "Kolmogorov":
            signif = vals['signif']
            kolmogorov_test(r_list, signif)
        elif button == "Chi-Squared":
            signif = vals['signif']
            chi_square_test(r_list, signif)


def chi_square_test(r_list=None, signif=None):
    chi_crit, header = cs.get_chi_table("chi_critical.txt")
    if r_list == None and signif == None:
        tab1_layout = [[sg.Text('Nombre del archivo')],
                       [sg.Input(), sg.FileBrowse(key='filename')]]

        tab2_layout = [[sg.Text("Asegurese de ingresar los datos separados de un \\n (enter)")],
                       [sg.Multiline(size=(30, 5), key='input_data')]]

        layout = [[sg.TabGroup([[sg.Tab('Lectura de archivo', tab1_layout), sg.Tab('Insercion manual de datos', tab2_layout)]])],
                  [sg.Text("Significancia"), sg.InputCombo(
                      header, size=(15, 3), key='signif')],
                  [sg.OK(), sg.Cancel()]]

        chi_window = sg.Window("Prueba de Chi-cuadrada", layout)
        while True:
            event, vals = chi_window.read()
            signif = vals['signif']
            if event in (sg.WIN_CLOSED, 'Cancel'):
                chi_window.close()
                break
            elif event == 'OK' and vals['filename'] != '':
                r_list = cs.get_list(vals['filename'])

            elif event == 'OK' and vals['input_data'] != '':
                r_list = vals['input_data'].split("\n")
                del r_list[-1]  # last element is always \n
                r_list = [float(i) for i in r_list]
            else:
                sg.popup_error(
                    "Alguno de los valores escritos no es adecuado, solo puede usar una forma de verificacion a la vez.")

            observed = cs.get_classes(r_list)
            expected = cs.get_expected(observed, r_list)
            observed = list(observed.values())
            chi_square(observed, expected, signif)

    else:  # list provided, we come from some other function
        observed = cs.get_classes(r_list)
        expected = cs.get_expected(observed, r_list)
        observed = list(observed.values())
        chi_square(observed, expected, signif)


def kolmogorov_test(r_list=None, signif=None):
    if r_list == None:
        tab1_layout = [[sg.Text('Nombre del archivo')],
                       [sg.Input(), sg.FileBrowse(key='filename')]]

        tab2_layout = [[sg.Text("Asegurese de ingresar los datos separados de un \\n (enter)")],
                       [sg.Multiline(size=(30, 5), key='input_data')]]

        layout = [[sg.TabGroup([[sg.Tab('Lectura de archivo', tab1_layout), sg.Tab('Insercion manual de datos', tab2_layout)]])],
                  [sg.Text("Significancia"), sg.Input(
                      size=(15, 3), key='signif')],
                  [sg.OK(), sg.Cancel("Cancelar")]]

        kol_window = sg.Window("Prueba de Kolmogorov-Smirnov", layout)
        while True:
            event, vals = kol_window.read()
            signif = vals['signif']
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                kol_window.close()
                break
            elif event == 'OK' and vals['filename'] != '':
                r_list = cs.get_list(vals['filename'])

            elif event == 'OK' and vals['input_data'] != '':
                r_list = vals['input_data'].split("\n")
                del r_list[-1]  # last element is always \n for some reason
                r_list = [float(i) for i in r_list]
            else:
                sg.popup_error(
                    "Alguno de los valores escritos no es adecuado, solo puede usar una forma de verificacion a la vez.")
            kolm_test(r_list, float(signif))
    else:
        kolm_test(r_list, float(signif))


def chi_square(observed, expected, signif):
    res, p_val = cs.check_hypothesis(observed, expected, signif)
    if res:
        sg.popup(
            f"Los numeros cumplen una distribucion uniforme: el p-valor es mayor a la significancia {p_val} > {signif}")
    else:
        sg.popup(
            f"Los numeros NO cumplen una distribucion uniforme: el p-valor es menor a la significancia {p_val} <= {signif}")


def kolm_test(r_list, signif):
    d, dalpha, res = kolmogorovSmirnov(r_list, signif)
    if res:
        sg.popup(
            f"Los numeros cumplen una distribucion uniforme: {d} <= {dalpha}")
    else:
        sg.popup(
            f"Los numeros NO cumplen una distribucion uniforme: {d} > {dalpha}")


mainGUI()
