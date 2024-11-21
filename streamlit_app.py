import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Visualizador de Archivos CSV/XLSX")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo CSV o XLSX", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Verificar el tipo de archivo y leerlo apropiadamente
        if uploaded_file.name.endswith(".csv"):
            # Leer archivo CSV
            df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
            st.write("Vista previa del archivo CSV:")
        elif uploaded_file.name.endswith(".xlsx"):
            # Leer archivo XLSX
            df = pd.read_excel(uploaded_file, engine="openpyxl")
            st.write("Vista previa del archivo XLSX:")
        
        # Mostrar el DataFrame
        st.dataframe(df)

    except Exception as e:
        st.error(f"Hubo un error al leer el archivo: {e}")
else:
    st.write("Sube un archivo CSV o XLSX para empezar.")
