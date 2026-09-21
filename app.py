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

    st.markdown(
        "**Esta Plantilla Nos Ayuda A Registrar Nuestras Finanzas**"
    )

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    Movimiento = st.text_input("Concepto")

    st.markdown("**Datos del movimiento**")

    Tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    Valor = st.number_input(
        "Valor",
        min_value=0.0,
        value=0.0
    )

    if st.button("Registrar movimiento"):

        nuevo_movimiento = {
            "Concepto": Movimiento,
            "Tipo": Tipo,
            "Valor": Valor
        }

        st.session_state.movimientos.append(nuevo_movimiento)

        st.success("Movimiento registrado correctamente")

    st.markdown("### Lista de movimientos registrados")

    for movimiento in st.session_state.movimientos:
        st.write(movimiento)

    total_ingresos = sum(
        movimiento["Valor"]
        for movimiento in st.session_state.movimientos
        if movimiento["Tipo"] == "Ingreso"
    )

    total_gastos = sum(
        movimiento["Valor"]
        for movimiento in st.session_state.movimientos
        if movimiento["Tipo"] == "Gasto"
    )

    saldo_final = total_ingresos - total_gastos

    st.markdown("### Resumen financiero")

    st.write("**Total de ingresos:**", total_ingresos)
    st.write("**Total de gastos:**", total_gastos)
    st.write("**Saldo final:**", saldo_final)

    if saldo_final > 0:
        st.success(f"Flujo de caja a favor: {saldo_final}")

    elif saldo_final < 0:
        st.error(f"Flujo de caja en contra: {saldo_final}")

    else:
        st.info("El flujo de caja está en equilibrio")






elif Módulos == "Ejercicio 2":

    import numpy as np
    import pandas as pd

    st.title("Registro de Productos")

    st.markdown(
        """
        Esta aplicación permite registrar productos mediante un formulario.
        Cada registro contiene el nombre, categoría, precio, cantidad y total.
        Al presionar el botón "Agregar producto", la información se almacena
        y se muestra en una tabla actualizada.
        """
    )

    # Crear los arrays en session_state
    if "nombres" not in st.session_state:
        st.session_state.nombres = np.array([])

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array([])

    if "precios" not in st.session_state:
        st.session_state.precios = np.array([])

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array([])

    if "totales" not in st.session_state:
        st.session_state.totales = np.array([])

    # Formulario
    st.markdown("### Ingreso de datos")

    nombre = st.text_input("Nombre del producto")

    categoria = st.selectbox(
        "Categoría",
        ["Bebidas", "Alimentos", "Limpieza", "Tecnología"]
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.10
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    # Calcular total
    total = precio * cantidad

    st.write(f"**Total: S/ {total:.2f}**")

    # Botón para agregar
    if st.button("Agregar producto"):

        if nombre == "":
            st.warning("Ingresa el nombre del producto.")

        else:
            st.session_state.nombres = np.append(
                st.session_state.nombres,
                nombre
            )

            st.session_state.categorias = np.append(
                st.session_state.categorias,
                categoria
            )

            st.session_state.precios = np.append(
                st.session_state.precios,
                precio
            )

            st.session_state.cantidades = np.append(
                st.session_state.cantidades,
                cantidad
            )

            st.session_state.totales = np.append(
                st.session_state.totales,
                total
            )

            st.success("Producto agregado correctamente.")

    # Crear DataFrame
    df = pd.DataFrame({
        "Producto": st.session_state.nombres,
        "Categoría": st.session_state.categorias,
        "Precio": st.session_state.precios,
        "Cantidad": st.session_state.cantidades,
        "Total": st.session_state.totales
    })

    # Mostrar DataFrame
    st.markdown("### Registros")

    st.dataframe(df, use_container_width=True)

