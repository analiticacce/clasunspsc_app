import streamlit as st
from clasunspsc.clasunspsc import recomendador_api
import pandas as pd
st.title("Clasificador UNSPSC")
st.header("This is a header")
name = st.text_input("Ingrese productos", "Type Here ...")
if(st.button('Submit')):
    result = recomendador_api(name,4)
    result=pd.DataFrame(result)
    st.table(result)