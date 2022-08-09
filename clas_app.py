import streamlit as st
from clasunspsc.clasunspsc import recomendador_api
import pandas as pd

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')
st.title("Clasificador UNSPSC")
st.header("GAEC - Colombia Compra Eficiente")
name = st.text_input("Ingrese productos", "")
if(st.button('Submit')):
    dicc = recomendador_api(name,10)
    if list(dicc.keys())[0]=="Result"
         result=pd.DataFrame(dicc)
    else:
          dicc={'Código Producto':dicc['Código Producto'],'Nombre Producto':dicc['Nombre Producto'],'Nombre Clase':dicc['Nombre Clase']}
          result=pd.DataFrame(dicc)
    st.table(result)
    csv = convert_df(result)
    st.download_button(
     label="Descargue CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
