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
  st.markdown("Esta Plantilla Nos Ayuda A Registrar Nuestras Finanzas")
  Movimiento = st.text_input("Ingrese Movimiento")
  Tipo = st.selectbox("Tipo de Movimiento",["Ingreso","Gasto"])
  Ingreso = st.number_input("Ingreso",value=0.0)
  Gasto= st.number_input("Gasto",value=0.0)    
  Saldo = Ingreso - Gasto
  st.write("Movimiento:", Movimiento)
  st.write("Tipo:", Tipo)
  st.write("Total Ingreso:", Ingreso)
  st.write("Total Gasto:", Gasto)
  st.write("Saldo:", Saldo)
  
  if Saldo > 0:
    st.write("A Favor:", Saldo)
  elif Saldo <0:
    st.write("En Contra:", Saldo)
  else:
    st.write("No cuenta con saldo")
  

elif Módulos =="Ejercicio 2":
  st.write("Resolución Ejercicio 2")
elif Módulos =="Ejercicio 3":
  st.write("Resolución Ejercicio 3")
else:
  st.write("Resolución Ejercicio 4")
 
st.write("Desarrollo web - Python")
