import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Visualizador de CSV")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Leer el archivo especificando la codificación y delimitador
        df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")  # Codificación común para evitar errores
        
        # Mostrar el DataFrame
        st.write("Vista previa del archivo CSV:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Hubo un error al leer el archivo: {e}")
else:
    st.write("Sube un archivo CSV para empezar.")
