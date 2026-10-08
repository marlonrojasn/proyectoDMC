import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Proyecto Análisis Churn",
    layout="wide"
)


# =========================
# TÍTULO E IMÁGENES
# =========================

st.title("Proyecto Análisis Churn")

st.image("imagen1.jpg")

st.sidebar.image("internet.jpg", width=150)


# =========================
# MENÚ PRINCIPAL
# =========================

Módulos = st.sidebar.selectbox(
    "Desplegar",
    [
        "Home",
        "Carga del Data Set",
        "Ítem 1: Información general",
        "Ítem 2: Clasificación de variables",
        "Ítem 3: Estadísticas descriptivas",
        "Ítem 4: Valores nulos",
        "Ítem 5: Distribución numérica",
        "Ítem 6: Variables categóricas",
        "Ítem 7: Numérico vs categórico",
        "Ítem 8: Categórico vs categórico",
        "Ítem 9: Parámetros seleccionados",
        "Ítem 10: Hallazgos clave"
    ]
)


# =========================
# HOME
# =========================

if Módulos == "Home":

    st.header("Telco Customer Churn")

    st.subheader("Objetivo del proyecto")

    st.write(
        """
        El objetivo de este proyecto es analizar el comportamiento de los
        clientes de una empresa de telecomunicaciones e identificar
        características y patrones relacionados con la cancelación del
        servicio (Churn), con la finalidad de apoyar la toma de decisiones.
        """
    )

    st.subheader("Datos del autor")

    st.write("**Nombre completo:** Marlon Jerson Rojas Novoa")
    st.write("**Curso / Especialización:** Data Science")
    st.write("**Año:** 2026")

    st.subheader("Descripción del dataset")

    st.write(
        """
        El dataset contiene información de clientes de una empresa de
        telecomunicaciones, incluyendo características demográficas,
        servicios contratados, información de facturación, antigüedad
        del cliente y la variable Churn.
        """
    )

    st.subheader("Tecnologías utilizadas")

    st.write(
        """
        - Python
        - Pandas
        - Streamlit
        - Matplotlib
        - Seaborn
        - NumPy
        """
    )


# =========================
# CARGA DEL DATA SET
# =========================

elif Módulos == "Carga del Data Set":

    st.header("Carga del Data Set")

    archivo = st.file_uploader(
        "Cargar archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        st.success("Archivo cargado correctamente.")

        df = pd.read_csv(
            archivo,
            sep=","
        )

        st.session_state["df"] = df

        st.subheader("Vista previa")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.subheader("Dimensiones del Data Set")

        filas, columnas = df.shape

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Número de filas",
                filas
            )

        with col2:
            st.metric(
                "Número de columnas",
                columnas
            )

    else:

        st.info(
            "Cargue un archivo CSV para comenzar el análisis."
        )


# =========================
# RESTO DE LOS ÍTEMS
# =========================

elif Módulos != "Home" and Módulos != "Carga del Data Set":

    if "df" not in st.session_state:

        st.warning(
            "Primero debe cargar un archivo CSV en 'Carga del Data Set'."
        )

    else:

        df = st.session_state["df"]


        # =========================
        # ÍTEM 1
        # =========================

        if Módulos == "Ítem 1: Información general":

            st.header("Ítem 1: Información general del Data Set")

            st.subheader("Información general")

            buffer = io.StringIO()

            df.info(buf=buffer)

            st.text(
                buffer.getvalue()
            )

            st.subheader("Tipos de datos")

            tipos_datos = pd.DataFrame(
                {
                    "Variable": df.columns,
                    "Tipo de dato": df.dtypes.astype(str)
                }
            )

            st.dataframe(
                tipos_datos,
                use_container_width=True
            )

            st.subheader("Valores nulos")

            valores_nulos = pd.DataFrame(
                {
                    "Variable": df.columns,
                    "Valores nulos": df.isnull().sum()
                }
            )

            st.dataframe(
                valores_nulos,
                use_container_width=True
            )

            st.write(
                f"El Data Set contiene **{df.shape[0]} filas** y "
                f"**{df.shape[1]} columnas**."
            )


        # =========================
        # ÍTEM 2
        # =========================

        elif Módulos == "Ítem 2: Clasificación de variables":

            st.header("Ítem 2: Clasificación de variables")

            def clasificar_variables(dataframe):

                variables_numericas = []
                variables_categoricas = []

                for columna in dataframe.columns:

                    if pd.api.types.is_numeric_dtype(
                        dataframe[columna]
                    ):

                        variables_numericas.append(columna)

                    else:

                        variables_categoricas.append(columna)

                return (
                    variables_numericas,
                    variables_categoricas
                )

            variables_numericas, variables_categoricas = (
                clasificar_variables(df)
            )

            st.subheader("Variables numéricas")

            st.write(
                f"Cantidad: **{len(variables_numericas)}**"
            )

            st.dataframe(
                pd.DataFrame(
                    {
                        "Variable": variables_numericas
                    }
                ),
                use_container_width=True
            )

            st.subheader("Variables categóricas")

            st.write(
                f"Cantidad: **{len(variables_categoricas)}**"
            )

            st.dataframe(
                pd.DataFrame(
                    {
                        "Variable": variables_categoricas
                    }
                ),
                use_container_width=True
            )

            st.subheader("Resumen")

            resumen = pd.DataFrame(
                {
                    "Tipo de variable": [
                        "Numéricas",
                        "Categóricas"
                    ],
                    "Cantidad": [
                        len(variables_numericas),
                        len(variables_categoricas)
                    ]
                }
            )

            st.dataframe(
                resumen,
                use_container_width=True
            )


        # =========================
        # ÍTEM 3
        # =========================

        elif Módulos == "Ítem 3: Estadísticas descriptivas":

            st.header("Ítem 3: Estadísticas descriptivas")

            st.subheader("Estadísticas descriptivas")

            st.dataframe(
                df.describe(),
                use_container_width=True
            )

            st.subheader("Interpretación")

            st.write(
                """
                La **media** representa el promedio de los valores.

                La **mediana** representa el valor central de los datos
                ordenados.

                La **desviación estándar** permite conocer la dispersión
                de los valores respecto a la media.
                """
            )


        # =========================
        # ÍTEM 4
        # =========================

        elif Módulos == "Ítem 4: Valores nulos":

            st.header("Ítem 4: Análisis de valores nulos")

            valores_nulos = df.isnull().sum()

            tabla_nulos = pd.DataFrame(
                {
                    "Variable": valores_nulos.index,
                    "Valores nulos": valores_nulos.values
                }
            )

            st.dataframe(
                tabla_nulos,
                use_container_width=True
            )

            total_nulos = valores_nulos.sum()

            st.write(
                f"Total de valores nulos: **{total_nulos}**"
            )

            if total_nulos > 0:

                columnas_con_nulos = valores_nulos[
                    valores_nulos > 0
                ]

                st.subheader(
                    "Visualización de valores nulos"
                )

                fig, ax = plt.subplots(
                    figsize=(10, 5)
                )

                columnas_con_nulos.plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_title(
                    "Cantidad de valores nulos por variable"
                )

                ax.set_xlabel(
                    "Variable"
                )

                ax.set_ylabel(
                    "Cantidad"
                )

                plt.xticks(
                    rotation=45
                )

                st.pyplot(fig)

                plt.close()

            else:

                st.success(
                    "No se encontraron valores nulos."
                )


        # =========================
        # ÍTEM 5
        # =========================

        elif Módulos == "Ítem 5: Distribución numérica":

            st.header(
                "Ítem 5: Distribución de variables numéricas"
            )

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            for variable in variables_numericas:

                st.subheader(
                    f"Distribución de {variable}"
                )

                fig, ax = plt.subplots(
                    figsize=(8, 4)
                )

                sns.histplot(
                    data=df,
                    x=variable,
                    kde=True,
                    ax=ax
                )

                ax.set_title(
                    f"Distribución de {variable}"
                )

                ax.set_xlabel(
                    variable
                )

                ax.set_ylabel(
                    "Frecuencia"
                )

                st.pyplot(fig)

                plt.close()


        # =========================
        # ÍTEM 6
        # =========================

        elif Módulos == "Ítem 6: Variables categóricas":

            st.header(
                "Ítem 6: Análisis de variables categóricas"
            )

            variables_categoricas = df.select_dtypes(
                exclude="number"
            ).columns.tolist()

            if not variables_categoricas:

                st.info(
                    "No se encontraron variables categóricas."
                )

            else:

                for variable in variables_categoricas:

                    st.subheader(
                        f"Variable: {variable}"
                    )

                    # -------------------------
                    # FRECUENCIAS
                    # -------------------------

                    conteo = df[
                        variable
                    ].value_counts(
                        dropna=False
                    )

                    tabla_conteo = (
                        conteo
                        .reset_index()
                    )

                    tabla_conteo.columns = [
                        "Categoría",
                        "Cantidad"
                    ]

                    st.write(
                        "Frecuencia absoluta:"
                    )

                    st.dataframe(
                        tabla_conteo,
                        use_container_width=True
                    )

                    # -------------------------
                    # PROPORCIONES
                    # -------------------------

                    proporciones = (
                        df[variable]
                        .value_counts(
                            normalize=True,
                            dropna=False
                        )
                        .mul(100)
                        .round(2)
                    )

                    tabla_proporciones = (
                        proporciones
                        .reset_index()
                    )

                    tabla_proporciones.columns = [
                        "Categoría",
                        "Proporción (%)"
                    ]

                    st.write(
                        "Proporciones:"
                    )

                    st.dataframe(
                        tabla_proporciones,
                        use_container_width=True
                    )

                    # -------------------------
                    # GRÁFICO DE BARRAS
                    # -------------------------

                    st.write(
                        "Gráfico de barras:"
                    )

                    fig, ax = plt.subplots(
                        figsize=(9, 5)
                    )

                    sns.countplot(
                        data=df,
                        x=variable,
                        order=conteo.index,
                        ax=ax
                    )

                    ax.set_title(
                        f"Distribución de {variable}"
                    )

                    ax.set_xlabel(
                        variable
                    )

                    ax.set_ylabel(
                        "Cantidad de clientes"
                    )

                    plt.xticks(
                        rotation=45,
                        ha="right"
                    )

                    plt.tight_layout()

                    st.pyplot(fig)

                    plt.close()

                    st.markdown("---")


        # =========================
        # ÍTEM 7
        # =========================

        elif Módulos == "Ítem 7: Numérico vs categórico":

            st.header(
                "Ítem 7: Análisis bivariado - Numérico vs Categórico"
            )

            if "Churn" not in df.columns:

                st.warning(
                    "La variable Churn no se encuentra en el Data Set."
                )

            else:

                variables_analizar = []

                if "MonthlyCharges" in df.columns:

                    if pd.api.types.is_numeric_dtype(
                        df["MonthlyCharges"]
                    ):

                        variables_analizar.append(
                            "MonthlyCharges"
                        )

                if "tenure" in df.columns:

                    if pd.api.types.is_numeric_dtype(
                        df["tenure"]
                    ):

                        variables_analizar.append(
                            "tenure"
                        )

                for variable in variables_analizar:

                    st.subheader(
                        f"{variable} vs Churn"
                    )

                    fig, ax = plt.subplots(
                        figsize=(7, 5)
                    )

                    sns.boxplot(
                        data=df,
                        x="Churn",
                        y=variable,
                        ax=ax
                    )

                    ax.set_title(
                        f"{variable} según Churn"
                    )

                    ax.set_xlabel(
                        "Churn"
                    )

                    ax.set_ylabel(
                        variable
                    )

                    st.pyplot(fig)

                    plt.close()

                    resumen = df.groupby(
                        "Churn"
                    )[variable].agg(
                        [
                            "mean",
                            "median",
                            "std"
                        ]
                    )

                    st.write(
                        "Estadísticas por Churn:"
                    )

                    st.dataframe(
                        resumen,
                        use_container_width=True
                    )


        # =========================
        # ÍTEM 8
        # =========================

        elif Módulos == "Ítem 8: Categórico vs categórico":

            st.header(
                "Ítem 8: Análisis bivariado - Categórico vs Categórico"
            )

            if "Churn" not in df.columns:

                st.warning(
                    "La variable Churn no se encuentra en el Data Set."
                )

            else:

                variables_analizar = []

                if "Contract" in df.columns:

                    variables_analizar.append(
                        "Contract"
                    )

                if "InternetService" in df.columns:

                    variables_analizar.append(
                        "InternetService"
                    )

                for variable in variables_analizar:

                    st.subheader(
                        f"{variable} vs Churn"
                    )

                    tabla = pd.crosstab(
                        df[variable],
                        df["Churn"]
                    )

                    st.write(
                        "Frecuencias:"
                    )

                    st.dataframe(
                        tabla,
                        use_container_width=True
                    )

                    porcentajes = pd.crosstab(
                        df[variable],
                        df["Churn"],
                        normalize="index"
                    ).mul(100).round(2)

                    st.write(
                        "Porcentajes:"
                    )

                    st.dataframe(
                        porcentajes,
                        use_container_width=True
                    )

                    fig, ax = plt.subplots(
                        figsize=(8, 5)
                    )

                    tabla.plot(
                        kind="bar",
                        ax=ax
                    )

                    ax.set_title(
                        f"{variable} vs Churn"
                    )

                    ax.set_xlabel(
                        variable
                    )

                    ax.set_ylabel(
                        "Cantidad de clientes"
                    )

                    plt.xticks(
                        rotation=45
                    )

                    st.pyplot(fig)

                    plt.close()


        # =========================
        # ÍTEM 9
        # =========================

        elif Módulos == "Ítem 9: Parámetros seleccionados":

            st.header(
                "Ítem 9: Análisis mediante parámetros seleccionados"
            )

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            variables_categoricas = df.select_dtypes(
                exclude="number"
            ).columns.tolist()

            if variables_numericas:

                variable_numerica = st.selectbox(
                    "Seleccione una variable numérica:",
                    variables_numericas
                )

                st.subheader(
                    f"Análisis de {variable_numerica}"
                )

                st.dataframe(
                    df[
                        variable_numerica
                    ].describe().to_frame(),
                    use_container_width=True
                )

                fig, ax = plt.subplots(
                    figsize=(8, 4)
                )

                sns.histplot(
                    data=df,
                    x=variable_numerica,
                    kde=True,
                    ax=ax
                )

                ax.set_title(
                    f"Distribución de {variable_numerica}"
                )

                st.pyplot(fig)

                plt.close()

            if variables_categoricas:

                variables_seleccionadas = st.multiselect(
                    "Seleccione una o más variables categóricas:",
                    variables_categoricas
                )

                for variable in variables_seleccionadas:

                    st.subheader(
                        f"Análisis de {variable}"
                    )

                    conteo = df[
                        variable
                    ].value_counts(
                        dropna=False
                    )

                    st.dataframe(
                        conteo.reset_index(
                            name="Cantidad"
                        ),
                        use_container_width=True
                    )

                    fig, ax = plt.subplots(
                        figsize=(8, 4)
                    )

                    sns.countplot(
                        data=df,
                        x=variable,
                        order=conteo.index,
                        ax=ax
                    )

                    ax.set_title(
                        f"Distribución de {variable}"
                    )

                    ax.set_xlabel(
                        variable
                    )

                    ax.set_ylabel(
                        "Cantidad"
                    )

                    plt.xticks(
                        rotation=45
                    )

                    plt.tight_layout()

                    st.pyplot(fig)

                    plt.close()


        # =========================
        # ÍTEM 10
        # =========================

        elif Módulos == "Ítem 10: Hallazgos clave":

            st.header(
                "Ítem 10: Hallazgos clave"
            )

            if "Churn" not in df.columns:

                st.warning(
                    "La variable Churn no se encuentra en el Data Set."
                )

            else:

                total_clientes = len(df)

                churn_normalizado = (
                    df["Churn"]
                    .astype(str)
                    .str.strip()
                    .str.lower()
                )

                clientes_churn = (
                    churn_normalizado == "yes"
                ).sum()

                tasa_churn = (
                    clientes_churn /
                    total_clientes
                ) * 100

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Total de clientes",
                        total_clientes
                    )

                with col2:

                    st.metric(
                        "Clientes con Churn",
                        clientes_churn
                    )

                with col3:

                    st.metric(
                        "Tasa de Churn",
                        f"{tasa_churn:.2f}%"
                    )

                st.subheader(
                    "Distribución de Churn"
                )

                conteo_churn = df[
                    "Churn"
                ].value_counts()

                fig, ax = plt.subplots(
                    figsize=(7, 4)
                )

                sns.barplot(
                    x=conteo_churn.index,
                    y=conteo_churn.values,
                    ax=ax
                )

                ax.set_title(
                    "Distribución de clientes según Churn"
                )

                ax.set_xlabel(
                    "Churn"
                )

                ax.set_ylabel(
                    "Cantidad de clientes"
                )

                st.pyplot(fig)

                plt.close()

                st.subheader(
                    "Principales hallazgos"
                )

                st.write(
                    f"""
                    - El Data Set contiene **{total_clientes} clientes**.
                    - Se identificaron **{clientes_churn} clientes** que abandonaron el servicio.
                    - La tasa general de Churn es de **{tasa_churn:.2f}%**.
                    """
                )

                if "tenure" in df.columns:

                    promedio_tenure = df.groupby(
                        "Churn"
                    )["tenure"].mean()

                    st.write(
                        "Antigüedad promedio según Churn:"
                    )

                    st.dataframe(
                        promedio_tenure.to_frame(
                            "Antigüedad promedio"
                        ),
                        use_container_width=True
                    )

                if "MonthlyCharges" in df.columns:

                    promedio_cargos = df.groupby(
                        "Churn"
                    )["MonthlyCharges"].mean()

                    st.write(
                        "Cargo mensual promedio según Churn:"
                    )

                    st.dataframe(
                        promedio_cargos.to_frame(
                            "Cargo mensual promedio"
                        ),
                        use_container_width=True
                    )

                st.info(
                    """
                    Estos resultados permiten identificar diferencias entre
                    los clientes que permanecen en el servicio y aquellos que
                    presentan Churn.
                    """
                )
