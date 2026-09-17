import streamlit as st
import numpy as np
st.title ("TRABAJO PRÁCTICO MÓDULO I")
Módulos = st.sidebar.selectbox ("Desplegar",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
if Módulos == "Home":
  st.write ("Trabajo Módulo I") 
  st.write ("Marlon Rojas Novoa")
  st.image("Python.png")
elif Módulos =="Ejercicio 1"
  st.write ("Resolución Ejercicio1")

  cantidad =st.slider("Selecciones un valor del rango", min_value = 1, maxvalue = 100, value=20)
  arreglo =np.arrange(cantidad)

  st.write(arreglo)

elif Módulos =="Ejercicio 2"
elif Módulos =="Ejercicio 3"
 
st.write("Desarrollo web - Python")
