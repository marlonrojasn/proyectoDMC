import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc


st.title("TRABAJO PRÁCTICO MÓDULO I")

st.sidebar.markdown(
    "<h2 style='text-align: center;'>Módulos</h2>",
    unsafe_allow_html=True)

st.sidebar.image("Python.png", width=150)

Módulos = st.sidebar.selectbox(
    "Desplegar",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])


# ==========================================================
# HOME
# ==========================================================

if Módulos == "Home":

    st.write("Trabajo Módulo I")
    st.image("prog.png", width=300)
    st.write("Marlon Jerson Rojas Novoa")
    st.write("Módulo I")

    st.write(
        "Ingeniero con interés en tecnología, análisis y gestión de datos, "
        "orientado al aprendizaje continuo y la innovación")

    st.write("Año: 2026")

    st.write(
        "Aplicación web desarrollada en Python para realizar cálculos, "
        "registrar resultados históricos y visualizar información mediante "
        "una interfaz interactiva.")

    st.write(
        "Desarrollo de una aplicación interactiva para el procesamiento, "
        "registro y visualización de datos, utilizando Python y Streamlit.")


# ==========================================================
# EJERCICIO 1
# ==========================================================

elif Módulos == "Ejercicio 1":

    st.markdown("**Esta Plantilla Nos Ayuda A Registrar Nuestras Finanzas**")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    Movimiento = st.text_input("Concepto")

    st.markdown("**Datos del movimiento**")

    Tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"])

    Valor = st.number_input(
        "Valor",
        min_value=0.0,
        value=0.0)

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
        if movimiento["Tipo"] == "Ingreso")

    total_gastos = sum(
        movimiento["Valor"]
        for movimiento in st.session_state.movimientos
        if movimiento["Tipo"] == "Gasto")

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


# ==========================================================
# EJERCICIO 2
# ==========================================================

elif Módulos == "Ejercicio 2":

    st.title("Registro de Productos")

    st.markdown(
        """
        Esta aplicación permite registrar productos mediante un formulario.
        Cada registro contiene el nombre, categoría, precio, cantidad y total.
        Al presionar el botón "Agregar producto", la información se almacena
        y se muestra en una tabla actualizada.
        """)

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
        ["Bebidas", "Alimentos", "Limpieza", "Tecnología"])

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.10)

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1)

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
                nombre)

            st.session_state.categorias = np.append(
                st.session_state.categorias,
                categoria)

            st.session_state.precios = np.append(
                st.session_state.precios,
                precio)

            st.session_state.cantidades = np.append(
                st.session_state.cantidades,
                cantidad)

            st.session_state.totales = np.append(
                st.session_state.totales,
                total)

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


# ==========================================================
# EJERCICIO 3
# ==========================================================

elif Módulos == "Ejercicio 3":

    st.write("Solución Ejercicio 3")

    # Selector de función

    funcion = st.selectbox(
        "Seleccione una función:",
        ["Calcular IMC"])

    if funcion == "Calcular IMC":

        # Ingreso de parámetros

        peso = st.number_input(
            "Ingrese su peso (kg):",
            min_value=1.0,
            value=70.0,
            step=0.1)

        altura = st.number_input(
            "Ingrese su altura (m):",
            min_value=0.5,
            value=1.70,
            step=0.01)

        # Botón para ejecutar

        if st.button("Calcular IMC"):

            # Usamos la función de la librería

            resultado = lf.calcular_imc(peso, altura)

            # Mostrar resultado

            st.write("Resultado del cálculo:")
            st.write("IMC:", resultado["imc"])
            st.write("Clasificación:", resultado["clasificacion"])

            # Guardar resultado

            registro = {
                "Peso (kg)": peso,
                "Altura (m)": altura,
                "IMC": resultado["imc"],
                "Clasificación": resultado["clasificacion"]
            }

            if "historico_imc" not in st.session_state:
                st.session_state.historico_imc = []

            st.session_state.historico_imc.append(registro)

    # Mostrar histórico

    st.write("Histórico de resultados:")

    if "historico_imc" in st.session_state:

        df_historico = pd.DataFrame(
            st.session_state.historico_imc)

        st.dataframe(df_historico)

    else:
        st.write("Aún no hay resultados registrados.")


# ==========================================================
# EJERCICIO 4 - CRUD CON CLASE EMPLEADO
# ==========================================================

elif Módulos == "Ejercicio 4":

    st.write("Administración de Empleados")

    # Crear lista de empleados

    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    # ======================================================
    # CREAR
    # ======================================================

    st.markdown("### Crear empleado")

    nombre = st.text_input("Nombre del empleado")

    salario = st.number_input(
        "Salario base",
        min_value=0.0,
        value=0.0,
        step=100.0)

    bono = st.number_input(
        "Porcentaje de bono (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0)

    descuento = st.number_input(
        "Porcentaje de descuento (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0)

    if st.button("Crear empleado"):

        if nombre == "":
            st.warning("Ingrese el nombre del empleado.")

        elif salario <= 0:
            st.warning("El salario debe ser mayor que 0.")

        else:

            empleado = lc.Empleado(
                nombre,
                salario,
                bono,
                descuento)

            st.session_state.empleados.append(empleado)

            st.success("Empleado creado correctamente.")

    # ======================================================
    # LEER
    # ======================================================

    st.markdown("### Lista de empleados")

    if len(st.session_state.empleados) > 0:

        datos = []

        for empleado in st.session_state.empleados:
            datos.append(empleado.resumen())

        df_empleados = pd.DataFrame(datos)

        st.dataframe(
            df_empleados,
            use_container_width=True)

    else:

        st.info("Aún no hay empleados registrados.")

    # ======================================================
    # ACTUALIZAR
    # ======================================================

    st.markdown("### Actualizar empleado")

    if len(st.session_state.empleados) > 0:

        nombres = [
            empleado.nombre
            for empleado in st.session_state.empleados
        ]

        empleado_seleccionado = st.selectbox(
            "Seleccione el empleado:",
            nombres)

        indice = nombres.index(empleado_seleccionado)

        empleado = st.session_state.empleados[indice]

        nuevo_nombre = st.text_input(
            "Nuevo nombre",
            value=empleado.nombre)

        nuevo_salario = st.number_input(
            "Nuevo salario base",
            min_value=0.0,
            value=float(empleado.salario_base),
            step=100.0)

        nuevo_bono = st.number_input(
            "Nuevo porcentaje de bono (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(empleado.porcentaje_bono),
            step=1.0)

        nuevo_descuento = st.number_input(
            "Nuevo porcentaje de descuento (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(empleado.porcentaje_descuento),
            step=1.0)

        if st.button("Actualizar empleado"):

            empleado.nombre = nuevo_nombre
            empleado.salario_base = nuevo_salario
            empleado.porcentaje_bono = nuevo_bono
            empleado.porcentaje_descuento = nuevo_descuento

            st.success("Empleado actualizado correctamente.")

    else:

        st.info("No hay empleados para actualizar.")

    # ======================================================
    # ELIMINAR
    # ======================================================

    st.markdown("### Eliminar empleado")

    if len(st.session_state.empleados) > 0:

        nombres_eliminar = [
            empleado.nombre
            for empleado in st.session_state.empleados
        ]

        empleado_eliminar = st.selectbox(
            "Seleccione el empleado a eliminar:",
            nombres_eliminar,
            key="empleado_eliminar")

        if st.button("Eliminar empleado"):

            indice = nombres_eliminar.index(empleado_eliminar)

            st.session_state.empleados.pop(indice)

            st.success("Empleado eliminado correctamente.")

    else:

        st.info("No hay empleados para eliminar.")
