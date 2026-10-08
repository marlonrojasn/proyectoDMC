```python
import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Proyecto Análisis Churn")

st.image("imagen1.jpg")

st.sidebar.image("internet.jpg", width=150)

Módulos = st.sidebar.selectbox(
    "Desplegar",
    ["Home", "Carga del Data Set", "Items"]
)

if Módulos == "Home":

    st.header("Telco Customer Churn")

    st.subheader("Objetivo del análisis")

    st.write(
        "El objetivo de este proyecto es analizar la pérdida de clientes "
        "en la empresa Telco (Customer Churn), identificando características "
        "y patrones relacionados con la salida de los clientes. "
        "El análisis permitirá explorar los datos y obtener información "
        "que pueda contribuir a la toma de decisiones."
    )

    st.subheader("Datos del autor")

    st.write("Nombre completo: Marlon Jerson Rojas Novoa")
    st.write("Curso / Especialización: Data Science")
    st.write("Año: 2026")

    st.subheader("Descripción del Dataset")

    st.write(
        "El dataset corresponde a información de clientes de una empresa "
        "de telecomunicaciones. Contiene variables relacionadas con las "
        "características de los clientes, los servicios contratados, "
        "información de facturación y la variable Churn, que indica si "
        "el cliente abandonó o no la empresa."
    )

    st.subheader("Tecnologías utilizadas")

    st.write(
        "Python: lenguaje utilizado para el desarrollo del proyecto.\n\n"
        "Pandas: utilizada para la carga, manipulación y análisis de los datos.\n\n"
        "Streamlit: utilizada para desarrollar la aplicación web interactiva.\n\n"
        "Matplotlib / Seaborn: utilizadas para la generación de visualizaciones.\n\n"
        "NumPy: utilizada para operaciones y procesamiento numérico."
    )


elif Módulos == "Carga del Data Set":

    st.header("Carga del Data Set")

    st.write(
        "Seleccione el archivo CSV para cargar "
        "y visualizar la información del dataset."
    )

    archivo = st.file_uploader(
        "Cargar archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        st.success("El archivo fue cargado correctamente.")

        df = pd.read_csv(archivo, sep=",")

        st.session_state["df"] = df

        st.subheader("Vista previa del Dataset")

        st.dataframe(df.head())

        st.subheader("Dimensiones del Dataset")

        filas, columnas = df.shape

        st.write(f"Filas: {filas}")
        st.write(f"Columnas: {columnas}")

    else:

        st.info("Por favor, cargue un archivo CSV.")


elif Módulos == "Items":

    st.header("Ítems de Análisis")

    if "df" not in st.session_state:

        st.warning(
            "Primero debe cargar un archivo CSV "
            "en el módulo Carga del Data Set."
        )

    else:

        df = st.session_state["df"]

        st.subheader("Ítem 1: Información general del dataset")

        st.write(
            "En este ítem se analiza la estructura general del dataset, "
            "identificando el número de registros, las variables, "
            "los tipos de datos y la cantidad de valores nulos."
        )

        st.write("Información general del dataset")

        buffer = io.StringIO()

        df.info(buf=buffer)

        st.text(buffer.getvalue())

        st.write("Tipos de datos")

        tipos = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de dato": df.dtypes.astype(str).values
        })

        st.dataframe(tipos)

        st.write("Conteo de valores nulos")

        nulos = df.isnull().sum()

        tabla_nulos = pd.DataFrame({
            "Variable": nulos.index,
            "Valores nulos": nulos.values
        })

        st.dataframe(tabla_nulos)

        st.write(f"Total de filas: {df.shape[0]}")
        st.write(f"Total de columnas: {df.shape[1]}")


        st.subheader("Ítem 2: Clasificación de variables")

        st.write(
            "En este ítem se clasifican las variables del dataset "
            "en numéricas y categóricas mediante una función personalizada."
        )

        def clasificar_variables(dataframe):

            numericas = []
            categoricas = []

            for columna in dataframe.columns:

                if pd.api.types.is_numeric_dtype(dataframe[columna]):
                    numericas.append(columna)

                else:
                    categoricas.append(columna)

            return numericas, categoricas

        variables_numericas, variables_categoricas = clasificar_variables(df)

        st.write("Variables numéricas")

        st.write(
            f"Cantidad de variables numéricas: "
            f"{len(variables_numericas)}"
        )

        st.dataframe(
            pd.DataFrame({
                "Variable": variables_numericas
            })
        )

        st.write("Variables categóricas")

        st.write(
            f"Cantidad de variables categóricas: "
            f"{len(variables_categoricas)}"
        )

        st.dataframe(
            pd.DataFrame({
                "Variable": variables_categoricas
            })
        )

        st.write("Conteo de variables")

        conteo_variables = pd.DataFrame({
            "Tipo de variable": [
                "Numéricas",
                "Categóricas"
            ],
            "Cantidad": [
                len(variables_numericas),
                len(variables_categoricas)
            ]
        })

        st.dataframe(conteo_variables)


        st.subheader("Ítem 3: Estadísticas descriptivas")

        st.write(
            "En este ítem se presentan las principales estadísticas "
            "descriptivas de las variables numéricas del dataset. "
            "Se analizan medidas como la media, mediana y dispersión."
        )

        st.dataframe(df.describe())

        st.write(
            "La media representa el valor promedio de una variable, "
            "mientras que la mediana corresponde al valor central "
            "cuando los datos se ordenan. La desviación estándar "
            "permite observar el nivel de dispersión de los datos "
            "respecto a su media."
        )


        st.subheader("Ítem 4: Análisis de valores faltantes")

        st.write(
            "En este ítem se analiza la cantidad de valores faltantes "
            "presentes en cada variable del dataset."
        )

        valores_faltantes = df.isnull().sum()

        faltantes = pd.DataFrame({
            "Variable": valores_faltantes.index,
            "Valores faltantes": valores_faltantes.values
        })

        faltantes = faltantes[
            faltantes["Valores faltantes"] > 0
        ]

        if len(faltantes) > 0:

            st.dataframe(faltantes)

            fig, ax = plt.subplots()

            ax.bar(
                faltantes["Variable"],
                faltantes["Valores faltantes"]
            )

            ax.set_title("Valores faltantes por variable")
            ax.set_xlabel("Variable")
            ax.set_ylabel("Cantidad de valores faltantes")

            plt.xticks(rotation=90)

            st.pyplot(fig)

            st.write(
                "Se identifican las variables que presentan valores "
                "faltantes. Estos valores deben ser evaluados antes "
                "de realizar análisis posteriores, ya que podrían "
                "afectar los resultados."
            )

        else:

            st.success(
                "No se encontraron valores faltantes en el dataset."
            )


        st.subheader("Ítem 5: Distribución de variables numéricas")

        st.write(
            "En este ítem se utilizan histogramas para observar "
            "la distribución de las variables numéricas."
        )

        variables_numericas = df.select_dtypes(
            include="number"
        ).columns

        for variable in variables_numericas:

            fig, ax = plt.subplots()

            sns.histplot(
                data=df,
                x=variable,
                kde=True,
                ax=ax
            )

            ax.set_title(
                f"Distribución de {variable}"
            )

            ax.set_xlabel(variable)
            ax.set_ylabel("Frecuencia")

            st.pyplot(fig)

        st.write(
            "Los histogramas permiten observar la concentración "
            "de los datos, su dispersión y posibles valores extremos. "
            "La forma de cada distribución ayuda a identificar "
            "si los valores se concentran en determinados rangos."
        )


        st.subheader("Ítem 6: Análisis de variables categóricas")

        st.write(
            "En este ítem se analizan las variables categóricas "
            "mediante conteos, gráficos de barras y proporciones."
        )

        variables_categoricas = df.select_dtypes(
            exclude="number"
        ).columns

        for variable in variables_categoricas:

            conteo = df[variable].value_counts()

            porcentaje = (
                df[variable]
                .value_counts(normalize=True)
                .mul(100)
                .round(2)
            )

            tabla = pd.DataFrame({
                "Categoría": conteo.index,
                "Conteo": conteo.values,
                "Proporción (%)": porcentaje.values
            })

            st.write(f"Variable: {variable}")

            st.dataframe(tabla)

            fig, ax = plt.subplots()

            sns.countplot(
                data=df,
                x=variable,
                ax=ax
            )

            ax.set_title(
                f"Conteo de {variable}"
            )

            ax.set_xlabel(variable)
            ax.set_ylabel("Cantidad")

            plt.xticks(rotation=45)

            st.pyplot(fig)
```

Este código ya deja desarrollados los **Ítems 1 al 6**.

Una observación importante: en el **Ítem 5** y el **Ítem 6** estamos generando un gráfico por cada variable. Eso puede producir bastantes gráficos en el caso de este dataset, pero **cumple con la visualización y el análisis solicitado**.
