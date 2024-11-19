import streamlit as st
import pandas as pd
import chardet  # Necesario para detectar la codificación

# Título de la aplicación
st.title("Visualizador de CSV")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        # Detectar la codificación
        raw_data = uploaded_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
        # Leer el archivo con la codificación detectada
        df = pd.read_csv(uploaded_file, encoding=encoding)
        
        # Mostrar el DataFrame
        st.write("Vista previa del archivo CSV:")
        st.dataframe(df)
        
        st.write(f"Codificación detectada: {encoding}")
        
    except Exception as e:
        st.error(f"Hubo un error al leer el archivo: {e}")
else:
    st.write("Sube un archivo CSV para empezar.")
