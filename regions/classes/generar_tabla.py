import pandas as pd
import gekko as gk

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

objec = LinearProgramming(4)
table = objec.generarTabla()
print(table)
    

