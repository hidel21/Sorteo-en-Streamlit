import streamlit as st
import pandas as pd
from utils.rifa_digital import RifaDigital
import os
import time
import random

st.set_page_config(page_title="Rifa Bera", page_icon="🏱", layout="centered")

# Estilos personalizados armonizados
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #0f1117;
        }
        h1, h2, h3 {
            color: #f0dd17;
        }
        .section-title {
            color: #3ebfe7;
            font-weight: 600;
            font-size: 18px;
            margin-top: 30px;
        }
        .slogan {
            text-align: center;
            color: #f0dd17;
            font-size: 20px;
            margin-top: -10px;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .stButton > button {
            background-color: #f0dd17;
            color: #0f1117;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
        }
        .stButton > button:hover {
            background-color: #3ebfe7;
            color: #0f1117;
        }
    </style>
""", unsafe_allow_html=True)

if 'set_actual' not in st.session_state:
    st.session_state.set_actual = 1

def mostrar_animacion_sorteo(df_filtrado, localidad):
    candidatos = df_filtrado['Nombre'].dropna().tolist()
    if not candidatos:
        return

    random.shuffle(candidatos)
    texto_ganador = st.empty()
    for _ in range(25):
        seleccionado = random.choice(candidatos)
        texto_ganador.markdown(f"""
            <div style="text-align: center;
                        font-size: 28px;
                        color: #00BFFF;
                        font-weight: bold;
                        background-color: #111111;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px #00BFFF;">
                🗓️ Seleccionando...<br><span style='color:#ffaa00;'>{seleccionado}</span>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)
    texto_ganador.empty()

def mostrar_logo():
    imagen = st.file_uploader("📸 Sube el banner del evento (PNG, JPG)", type=["png", "jpg", "jpeg"])
    col = st.container()
    with col:
        if imagen:
            st.image(imagen, use_column_width=True)
        else:
            ruta_logo = "assets/logo_bera.png"
            if os.path.exists(ruta_logo):
                st.image(ruta_logo, use_column_width=True)
        st.markdown("""
            <div style="
                text-align: center;
                font-size: 20px;
                color: #f0dd17;
                font-weight: bold;
                margin-top: -10px;
                letter-spacing: 2px;">
                🇻🇪 VENEZUELA TERRITORIO BERA
            </div>
        """, unsafe_allow_html=True)

def cargar_excel_desde_interfaz():
    uploaded_file = st.file_uploader("📁 Sube el archivo Excel con los empleados", type=["xlsx"], key="uploaded_file")
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            columnas_requeridas = {"Nombre", "Localidad"}
            if not columnas_requeridas.issubset(set(df.columns)):
                st.error("❌ El archivo debe contener las columnas: 'Nombre' y 'Localidad'")
                return None
            return df
        except Exception as e:
            st.error(f"❌ Error al leer el archivo: {e}")
            return None
    return None

mostrar_logo()
st.markdown("<h1 style='text-align: center;'>🏱 Rifa Digital de la Organización</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div style="
        text-align: center;
        background-color: #1c1e26;
        padding: 15px;
        border-radius: 12px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 0px 10px #ffaa00;
        font-size: 22px;
        font-weight: bold;
        color: #ffaa00;
    ">
        🎯 SET ACTUAL: {st.session_state.set_actual}
    </div>
""", unsafe_allow_html=True)

df = cargar_excel_desde_interfaz()

if df is not None:
    if 'rifa' not in st.session_state:
        st.session_state.rifa = RifaDigital(df, set_actual=st.session_state.set_actual)

    rifa = st.session_state.rifa

    st.markdown("<div class='section-title'>🎯 Configuración del sorteo</div>", unsafe_allow_html=True)

    localidades_disponibles = ["🏑 Todas las localidades"] + sorted(df['Localidad'].dropna().unique())
    localidad_seleccionada = st.selectbox("Selecciona la localidad para el sorteo", options=localidades_disponibles)

    premio = st.text_input("🏆 Premio (opcional)")

    if st.button("🎲 Realizar sorteo"):
        if localidad_seleccionada == "🏑 Todas las localidades":
            df_filtrado = df
        else:
            df_filtrado = df[df['Localidad'].str.upper() == localidad_seleccionada.upper()]

        mostrar_animacion_sorteo(df_filtrado, localidad_seleccionada)

        if localidad_seleccionada == "🏑 Todas las localidades":
            ganador = rifa.sortear_global(premio)
        else:
            ganador = rifa.sortear_por_nombre_localidad(localidad_seleccionada, premio)

        if ganador is not None:
            st.markdown(f"""
                <div style="
                    text-align: center;
                    background-color: #003366;
                    padding: 30px;
                    border-radius: 15px;
                    margin-top: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0px 0px 20px #00BFFF;
                    font-size: 26px;
                    font-weight: bold;
                    color: #FFCC00;">
                    🎉 <u>GANADOR</u><br><br>
                    🧝 {ganador['Nombre']}<br>
                    📍 Localidad: {ganador['Localidad']}<br>
                    🏆 Premio: {premio or 'Sin premio'}
                </div>
            """, unsafe_allow_html=True)

            archivo_auto = rifa.exportar_resultados_en_memoria()
            if archivo_auto:
                with open(f"resultados_rifa_set_{rifa.set_actual}.xlsx", "wb") as f:
                    f.write(archivo_auto.getbuffer())
        else:
            st.warning("⚠️ No hay participantes disponibles para esta localidad.")

    if st.button("➡️ Siguiente set"):
        st.session_state.set_actual += 1
        st.success(f"✅ Ahora estás en el SET {st.session_state.set_actual}")

    if st.button("🔄 Resetear rifas"):
        rifa.resetear()
        st.session_state.set_actual = 1
        st.info("Rifa reseteada correctamente.")

    archivo_excel = rifa.exportar_resultados_en_memoria()
    if archivo_excel:
        st.download_button(
            label="📥 Descargar resultados de ganadores",
            data=archivo_excel,
            file_name=f"resultados_rifa_set_{rifa.set_actual}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("⚠️ Aún no hay ganadores para exportar.")