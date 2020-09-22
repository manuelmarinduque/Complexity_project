import pandas as pd
from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

class LinearProgramming():
    
    def __init__(self, num_regiones):
        self.__num_regiones = num_regiones

    def construirTabla(self):
        info = [[50, 1000, 2, 5000000, 550, 0], 
                [25, 100, 4, 4000000, 350, 4], 
                [90, 3000, 1, 4000000, 2600, 0],
                [40, 500, 1, 1500000, 1000, 0],
                [35, 700, 1, 5000000, 300, 2],
                [22, 80, 3, 3500000, 250, 0],
                [30, 60, 2, 4500000, 300, 3]]
        tabla = pd.DataFrame(info, columns=('Población', 'Estaciones', 'Personal', 'Costos', 'Muertes', 'Cualificacion'))
        return tabla

    def __estacionesPorHabitantes(self, tabla):
        estaciones = tabla['Estaciones']
        poblacion = tabla['Población']
        resultado = estaciones.div(poblacion)
        tabla['est*hab'] = resultado
        return tabla

    def __muertesPorMillon(self, tabla):
        muertes = tabla['Muertes']
        poblacion = tabla['Población'].mul(100000)
        resultado = muertes.div(poblacion).mul(1000000)
        tabla["Muertes*millon"] = resultado
        return tabla

    def __beneficio(self, tabla):
        tabla2 = tabla.sort_values('est*hab', ascending = False) 
        indices = indices = [i for i in range(1,8)]
        tabla2['Beneficio'] = indices
        return tabla2.sort_index()

    def __ventiladores(self, tabla):
        tabla2 = tabla.sort_values('Muertes*millon', ascending = False) 
        indices1 = [2,2]
        indices2 = [1 for i in range(0, len(tabla2['Muertes'])-2)]
        indices = indices1+indices2
        tabla2['Ventiladores'] = indices
        return tabla2.sort_index()

    def generarTabla(self, tabla):
        tabla = self.__estacionesPorHabitantes(tabla)
        tabla = self.__muertesPorMillon(tabla)
        tabla = self.__beneficio(tabla)
        tabla = self.__ventiladores(tabla)
        return tabla

    def __generarTablaModelo(self, tabla):
        variables_regiones = [LpVariable(f'x{i}', lowBound=0, cat='Integer') for i in range (1, self.__num_regiones + 1)]
        beneficio = tabla['Beneficio'].values
        ventiladores = tabla['Ventiladores'].values
        personal = tabla['Personal'].values
        costos = tabla['Costos'].values
        cualificacion = tabla['Cualificacion'].values
        info = [variables_regiones, beneficio, ventiladores, personal, costos, cualificacion]
        tabla_modelo = pd.DataFrame(info, columns=[f'Region{i}' for i in range(1, self.__num_regiones + 1)])
        return tabla_modelo, variables_regiones
    
    def __variablesModelo(self, tabla):
        tabla_modelo, variables_regiones = tabla
        funcion_objetivo = 0
        ventiladores = 0
        personal = 0
        costo = 0
        cualificacion = 0
        for nombre_columna, contenido in tabla_modelo.items():
            funcion_objetivo += contenido[1]*contenido[0]
            ventiladores += contenido[2]*contenido[0]
            personal += contenido[3]*contenido[0]
            costo += contenido[4]*contenido[0]
            cualificacion += contenido[5]*contenido[0]
        return variables_regiones, funcion_objetivo, ventiladores, personal, costo, cualificacion
    
    def modelo(self, tabla, total_ventiladores, total_personal, total_costo, total_cualificacion):
        tabla_modelo = self.__generarTablaModelo(tabla)
        regiones, funcion_objetivo, ventiladores, personal, costo, cualificacion = self.__variablesModelo(tabla_modelo)
        model = LpProblem('Modelo_proyecto', LpMaximize)
        model += funcion_objetivo
        model += ventiladores <= total_ventiladores
        model += personal <= total_personal
        model += costo <= total_costo
        model += cualificacion >= total_cualificacion
        model.solve()
        valores_regiones = (value(regiones[0]), value(regiones[1]), value(regiones[2]), value(regiones[3]), value(regiones[4]), value(regiones[5]), value(regiones[6]))
        return valores_regiones, value(model.objective)
    
    def distribucionElementos(self, valores_regiones, tabla):
        distribucionVentiladores = [i*j for i,j in zip(valores_regiones, tabla['Ventiladores'].values)]
        distribucionProfesionales = [i*j for i,j in zip(valores_regiones, tabla['Personal'].values)]
        distribucionPresupuesto = [i*j for i,j in zip(valores_regiones, tabla['Costos'].values)]
        distribucionCualificacion = [i*j for i,j in zip(valores_regiones, tabla['Cualificacion'].values)]
        return distribucionVentiladores, distribucionProfesionales, distribucionPresupuesto, distribucionCualificacion

