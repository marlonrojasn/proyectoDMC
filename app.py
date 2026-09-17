import streamlit as st
import numpy as np
st.title ("TRABAJO PRÁCTICO MÓDULO I")
st.sidebar.markdown(
    "<h2 style='text-align: center;'>Módulos</h2>",
    unsafe_allow_html=True)
st.sidebar.image("Python.png", width=150)
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
  st.write ("**Resolución Ejercicio1**")
  st.markdown("**Esta Plantilla Nos Ayuda A Registrar Nuestras Finanzas**")
  Movimiento = st.text_input("Concepto")
  st.markdown ("**Tipo de Movimiento**")
  Ingreso = st.number_input("Ingreso",value=0.0)
  Gasto= st.number_input("Gasto",value=0.0)    
  Saldo = Ingreso - Gasto
  st.write("Movimiento:", Movimiento)
  st.write("Total Ingreso:", Ingreso)
  st.write("Total Gasto:", Gasto)
  st.write("Saldo:", Saldo)
  
  if Saldo > 0:
    st.write("A Favor:", Saldo)
  elif Saldo <0:
    st.write("En Contra:", Saldo)
  else:
    st.write("No cuenta con saldo")
  

