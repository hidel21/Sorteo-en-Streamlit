Perfecto. Aquí tienes un `README.md` **profesional, claro y completo**, ideal para documentar tu proyecto de **Rifa Digital**. Incluye:

- ✅ Descripción del proyecto  
- 🛠️ Instrucciones de instalación y uso  
- 🎯 Detalles de funcionalidad  
- 🧑‍💻 Información del autor

---

## 📄 `README.md`

```markdown
# 🎁 Rifa Digital - Organización Bera

Aplicación interactiva desarrollada en **Python y Streamlit** para realizar rifas dinámicas, justas y transparentes en eventos corporativos de la Organización Bera.

Diseñada para usarse en eventos en vivo, esta herramienta permite cargar listas de empleados, realizar sorteos por localidad o generales, y exportar resultados en tiempo real.

---

## 🚀 Funcionalidades

- 🎯 **Sorteo por localidad** o **global** (todas las localidades).
- 🔄 Gestión de **sets múltiples** para múltiples rondas de rifas.
- 🎰 **Animación en vivo** antes de revelar el ganador, para mayor transparencia.
- 🧍‍♂️ Control de **ganadores únicos por set**.
- 📤 **Exportación automática** a Excel de los ganadores.
- 🧹 Botón para **resetear rifas** y comenzar desde cero.
- 🖼️ Carga opcional de **banner visual del evento**.

---

## 🧾 Requisitos del sistema

- Python 3.8 o superior
- Navegador web moderno

---

## 📦 Instalación

1. Clona el repositorio o copia los archivos del proyecto.

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

   **Contenido de `requirements.txt`:**

   ```txt
   streamlit
   pandas
   openpyxl
   ```

---

## ▶️ Cómo ejecutar la app

Desde el terminal:

```bash
streamlit run app2.py
```

La aplicación se abrirá automáticamente en tu navegador en [http://localhost:8501](http://localhost:8501)

---

## 📋 Estructura esperada del archivo Excel

El archivo debe tener al menos estas columnas:

| Nombre           | Localidad       |
|------------------|-----------------|
| Juan Pérez       | PLM             |
| María González   | Administrativo  |
| Pedro Sánchez    | PLV             |

---

## 📂 Estructura del proyecto

```
RifaDigital/
│
├── app2.py                   # App principal Streamlit
├── utils/
│   └── rifa_digital.py       # Lógica de sorteos
├── assets/
│   └── logo.png              # Banner por defecto si no se carga uno
├── resultados_rifa_set_X.xlsx  # Exportaciones automáticas por SET
├── requirements.txt
└── README.md
```

---

## 🎯 Instrucciones de uso

1. Sube tu archivo Excel con nombres y localidades.
2. (Opcional) Carga el banner del evento.
3. Selecciona una localidad o “🏁 Todas las localidades”.
4. Escribe el premio a entregar.
5. Haz clic en **"🎲 Realizar sorteo"**.
6. Mira la animación en vivo y se anunciará al ganador.
7. Descarga los resultados o pasa al siguiente set.

---

## 📌 Consideraciones

- Los ganadores se almacenan en memoria durante la sesión de Streamlit.
- Si cierras la app sin exportar, se perderán los resultados a menos que se guarden manualmente.
- Se genera un archivo Excel automáticamente después de cada sorteo.
- No se repiten ganadores dentro del mismo set.

---

## 👨‍💻 Autor

**Hidelberg Martínez**  
Desarrollador de sistemas y programador Odoo  
📍 Venezuela – Territorio Bera  
✉️ Contacto: (agrega tu email o red si deseas)  

---

**¡Hecha para brillar en eventos reales, con emoción y transparencia!**  
🇻🇪 *Venezuela Territorio Bera*
```# Sistema-de-sorteo
# Sorteo-en-Streamlit
