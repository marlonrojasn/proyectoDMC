import streamlit as st
import numpy as np
st.title ("TRABAJO PRÁCTICO MÓDULO I")
st.sidebar.title("Módulos")
Módulos = st.sidebar.selectbox ("Desplegar",["Home","Movimientos Financieros","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
if Módulos == "Home":
  st.write ("Trabajo Módulo I") 
  st.image("prog.png",width =300)
  st.write ("Marlon Jerson Rojas Novoa")
  st.write ("Módulo I")
  st.write("Ingeniero con interés en tecnología, análisis y gestión de datos, orientado al aprendizaje continuo y la innovación")
  st.write ("Año: 2026")
  st.write ("Descripción del proyecto")
  st.write ("Tecnologías usadas")

elif Módulos =="Movimientos Financieros":
  st.write ("Resolución Ejercicio1")
  st.markdown("Vamos Resolver El Ejercicio1")
  st.text_input("Ingrese Movimiento")
  Tipo = select.box("Tipo de Movimiento",[Ingreso,Gasto])
  valor = st.number_input("Ingrese el valor", min_value=0.0, value=0.0)    

    if tipo == "Ingreso":
        ingreso = valor
        gasto = 0
    else:
        ingreso = 0
        gasto = valor

    saldo = ingreso - gasto

    st.write("Movimiento:", movimiento)
    st.write("Tipo:", tipo)
    st.write("Valor:", valor)
    st.write("Saldo:", saldo)
  

elif Módulos =="Ejercicio 2":
  st.write("Resolución Ejercicio 2")
elif Módulos =="Ejercicio 3":
  st.write("Resolución Ejercicio 3")
else:
  st.write("Resolución Ejercicio 4")
 
st.write("Desarrollo web - Python")
