import streamlit as st
import pandas as pd
import chardet

# Título de la aplicación
st.title("Visualizador de CSV")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv", "txt"])

if uploaded_file is not None:
    try:
        # Detectar la codificación del archivo
        raw_data = uploaded_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

        # Validar si el archivo tiene contenido
        if not raw_data.strip():
            st.error("El archivo está vacío.")
        else:
            # Reiniciar el puntero después de leer los bytes
            uploaded_file.seek(0)

            # Intentar con diferentes delimitadores
            delimiters = [',', ';', '\t', '|']
            for delimiter in delimiters:
                try:
                    # Intentar leer el archivo con el delimitador actual
                    df = pd.read_csv(uploaded_file, encoding=encoding, delimiter=delimiter)
                    
                    # Validar si se detectaron columnas
                    if df.columns.size > 0:
                        st.write("Vista previa del archivo CSV:")
                        st.dataframe(df)
                        st.write(f"Codificación detectada: {encoding}")
                        st.write(f"Delimitador utilizado: '{delimiter}'")
                        break
                except pd.errors.ParserError:
                    uploaded_file.seek(0)  # Reiniciar el puntero para el próximo intento
            else:
                st.error("No se pudieron detectar columnas válidas en el archivo. Verifica el formato.")
    
    except pd.errors.EmptyDataError:
        st.error("El archivo está vacío o no tiene datos válidos.")
    except Exception as e:
        st.error(f"Hubo un error al leer el archivo: {e}")
else:
    st.write("Sube un archivo CSV para empezar.")
