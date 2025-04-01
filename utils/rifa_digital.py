import os
import io
import pandas as pd

class RifaDigital:
    def __init__(self, df, set_actual=1):
        self.original_data = df.copy()
        self.data = df.copy()
        self.set_actual = set_actual
        self.ganadores = []

        if "Ganador" not in self.data.columns:
            self.data["Ganador"] = False
        if "Premio" not in self.data.columns:
            self.data["Premio"] = None
        if "Set" not in self.data.columns:
            self.data["Set"] = None

    def filtrar_por_localidad(self, localidad):
        return self.data[
            (self.data['Localidad'].str.upper() == localidad.upper()) &
            (~self.data['Ganador']) &
            (self.data['Set'].isna() | (self.data['Set'] != self.set_actual))
        ]

    def sortear_por_nombre_localidad(self, localidad, premio=None):
        participantes = self.filtrar_por_localidad(localidad)
        if participantes.empty:
            return None

        ganador = participantes.sample(1).iloc[0]
        idx = self.data[self.data['Nombre'] == ganador['Nombre']].index[0]

        self.data.at[idx, 'Ganador'] = True
        self.data.at[idx, 'Premio'] = premio
        self.data.at[idx, 'Set'] = self.set_actual

        self.ganadores.append(self.data.loc[idx])

        return self.data.loc[idx]

    def sortear_global(self, premio=None):
        participantes = self.data[
            (~self.data['Ganador']) &
            (self.data['Set'].isna() | (self.data['Set'] != self.set_actual))
        ]
        if participantes.empty:
            return None

        ganador = participantes.sample(1).iloc[0]
        idx = self.data[self.data['Nombre'] == ganador['Nombre']].index[0]

        self.data.at[idx, 'Ganador'] = True
        self.data.at[idx, 'Premio'] = premio
        self.data.at[idx, 'Set'] = self.set_actual

        self.ganadores.append(self.data.loc[idx])

        return self.data.loc[idx]

    def resetear(self):
        self.data = self.original_data.copy()
        self.data['Ganador'] = False
        self.data['Premio'] = None
        self.data['Set'] = None
        self.ganadores = []
        self.set_actual = 1

    def siguiente_set(self):
        self.set_actual += 1

    def exportar_resultados_en_memoria(self):
        df_export = self.data[self.data['Ganador'] == True]
        if df_export.empty:
            return None
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_export.to_excel(writer, index=False, sheet_name="Ganadores")
        output.seek(0)
        return output
