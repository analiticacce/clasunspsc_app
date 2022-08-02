import streamlit as st
from clasunspsc.clasunspsc import recomendador_api
import pandas as pd
st.title("Clasificador UNSPSC")
st.header("GAEC - Colombia Compra Eficiente")
name = st.text_input("Ingrese productos", "")
if(st.button('Submit')):
    dicc = recomendador_api(name,10)
    dicc={'Código Producto':dicc['Código Producto'],'Nombre Producto':dicc['Nombre Producto'],'Nombre Clase':dicc['Nombre Clase']}
    result=pd.DataFrame(dicc)
    st.table(result)
    
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
     label="Descargue CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
