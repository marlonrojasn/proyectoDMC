import streamlit as st
import numpy as np
st.title ("TRABAJO PRÁCTICO MÓDULO I")
st.sidebar.title("Módulos")
Módulos = st.sidebar.selectbox ("Desplegar",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
if Módulos == "Home":
  st.write ("Trabajo Módulo I") 
  st.image("prog.png",width =300)
  st.write ("Marlon Jerson Rojas Novoa")
  st.write ("Módulo I")
  st.write("Ingeniero con interés en tecnología, análisis y gestión de datos, orientado al aprendizaje continuo y la innovación")
  st.write ("Año: 2026")
  st.write ("Descripción del proyecto")
  st.write ("Tecnologías usadas")

elif Módulos =="Ejercicio 1":
  st.write ("Resolución Ejercicio1")
  cantidad =st.slider("Selecciones un valor del rango", min_value = 1, maxvalue = 100, value=20)
  arreglo =np.arrange(cantidad)

  st.write(arreglo)

elif Módulos =="Ejercicio 2":
  st.write("Resolución Ejercicio 2")
elif Módulos =="Ejercicio 3":
  st.write("Resolución Ejercicio 3")
else:
  st.write("Resolución Ejercicio 4")
 
st.write("Desarrollo web - Python")
