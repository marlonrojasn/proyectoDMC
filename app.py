import streamlit as st
st.title ("TRABAJO PRÁCTICO MÓDULO I")
Módulos = st.sidebar.selectbox ("Desplegar",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
if Módulos == "Home":
  st.write ("Trabajo Módulo I")
  st.write ("Marlon Rojas Novoa")
st.write("Elaborado por: Marlon Rojas")
