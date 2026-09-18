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

elif Módulos == "Movimientos Financieros":
    st.write("**Resolución Ejercicio 1**")
    st.markdown("**Esta Plantilla Nos Ayuda A Registrar Nuestras Finanzas**")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    Movimiento = st.text_input("Concepto")

    st.markdown("**Datos del movimiento**")

    Ingreso = st.number_input("Ingreso", min_value=0.0, value=0.0)
    Gasto = st.number_input("Gasto", min_value=0.0, value=0.0)

    if st.button("Registrar movimiento"):
        nuevo_movimiento = {
            "Concepto": Movimiento,
            "Ingreso": Ingreso,
            "Gasto": Gasto
        }

        st.session_state.movimientos.append(nuevo_movimiento)

        st.success("Movimiento registrado correctamente")

    st.markdown("### Lista de movimientos registrados")

    for movimiento in st.session_state.movimientos:
        st.write(movimiento)

    total_ingresos = sum(
        movimiento["Ingreso"]
        for movimiento in st.session_state.movimientos
    )

    total_gastos = sum(
        movimiento["Gasto"]
        for movimiento in st.session_state.movimientos
    )

    saldo_final = total_ingresos - total_gastos

    st.markdown("### Resumen financiero")

    st.write("**Total de ingresos:**", total_ingresos)
    st.write("**Total de gastos:**", total_gastos)
    st.write("**Saldo final:**", saldo_final)

    if saldo_final > 0:
        st.success(f"Saldo a favor: {saldo_final}")
    elif saldo_final < 0:
        st.error(f"Saldo en contra: {saldo_final}")
    else:
        st.info("No tiene saldo a favor ni en contra")
  
elif Módulos == "Ejercicio 2":
    st.write("**Andrea a como el kg**")
