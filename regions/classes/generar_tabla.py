import pandas as pd
# import gekko as gk

class LinearProgramming():
    
    def __init__(self, num_regiones):
        self.num_regiones = num_regiones

    def generarTabla(self):
        info = [[50, 1000, 2, 5000, 550], 
                [25, 100, 4, 400, 350], 
                [90, 3000, 1, 4000, 2600],
                [40, 500, 1, 1500, 1000],
                [35, 700, 1, 5000, 300],
                [22, 80, 3, 3500, 250],
                [30, 60, 2, 4500, 300]]
        df = pd.DataFrame(info, columns=('Población', 'Estaciones', 'Personal', 'Costos', 'Muertes'))
        return df

    def estacionesPorHabitantes(self, tabla):
        estaciones = tabla['Estaciones']
        poblacion = tabla['Población']
        resultado = estaciones.div(poblacion)
        tabla['est*hab'] = resultado
        return tabla

    def muertesPorMillon(self, tabla):
        muertes = tabla['Muertes']
        poblacion = tabla['Población'].mul(100000)
        resultado = muertes.div(poblacion).mul(1000000)
        tabla["Muertes*millon"] = resultado
        return tabla

    def beneficio(self, tabla):
        tabla2 = tabla.sort_values('est*hab', ascending = False) 
        indices = indices = [i for i in range(1,8)]
        tabla2['Beneficio'] = indices
        return tabla2.sort_index()

    def ventiladores(self, tabla):
        tabla2 = tabla.sort_values('Muertes*millon', ascending = False) 
        indices1 = [2,2]
        indices2 = [1 for i in range(0, len(tabla2['Muertes'])-2)]
        indices = indices1+indices2
        tabla2['Ventiladores'] = indices
        return tabla2.sort_index()

        

objec = LinearProgramming(4)
table = objec.generarTabla()
result = objec.estacionesPorHabitantes(table)
result2 = objec.muertesPorMillon(result)
result3 = objec.beneficio(result2)
result4 = objec.ventiladores(result3)
print(result4)

    

