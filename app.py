# ==================================================
# MENÚ PRINCIPAL
# ==================================================

modulo = st.sidebar.selectbox(
    "Desplegar",
    [
        "Home",
        "Carga del Data Set",
        "Items"
    ]
)


# ==================================================
# ITEMS
# ==================================================

elif modulo == "Items":

    # Los 10 ITEMS aparecen en la PÁGINA PRINCIPAL
    # y NO en el sidebar.

    st.header("Análisis Exploratorio de Datos")

    item = st.selectbox(
        "Seleccionar Item",
        [
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

    if "df" not in st.session_state:

        st.warning(
            "Primero debe cargar el archivo CSV "
            "en 'Carga del Data Set'."
        )

    else:

        df = st.session_state["df"]

        # ==========================================
        # ITEM 1
        # ==========================================

        if item == "Ítem 1: Información general":

            st.subheader("Ítem 1: Información general")

            filas, columnas = df.shape

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Número de filas", filas)

            with col2:
                st.metric("Número de columnas", columnas)

            informacion = pd.DataFrame({
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str).values,
                "Valores no nulos": df.notnull().sum().values,
                "Valores nulos": df.isnull().sum().values
            })

            st.dataframe(
                informacion,
                use_container_width=True
            )


        # ==========================================
        # ITEM 2
        # ==========================================

        elif item == "Ítem 2: Clasificación de variables":

            st.subheader(
                "Ítem 2: Clasificación de variables"
            )

            variables_numericas = []
            variables_categoricas = []

            for columna in df.columns:

                if pd.api.types.is_numeric_dtype(
                    df[columna]
                ):
                    variables_numericas.append(columna)
                else:
                    variables_categoricas.append(columna)

            st.write("### Variables numéricas")

            st.dataframe(
                pd.DataFrame({
                    "Variable": variables_numericas,
                    "Tipo": "Numérica"
                }),
                use_container_width=True
            )

            st.metric(
                "Cantidad de variables numéricas",
                len(variables_numericas)
            )

            st.write("### Variables categóricas")

            st.dataframe(
                pd.DataFrame({
                    "Variable": variables_categoricas,
                    "Tipo": "Categórica"
                }),
                use_container_width=True
            )

            st.metric(
                "Cantidad de variables categóricas",
                len(variables_categoricas)
            )


        # ==========================================
        # ITEM 3
        # ==========================================

        elif item == "Ítem 3: Estadísticas descriptivas":

            st.subheader(
                "Ítem 3: Estadísticas descriptivas"
            )

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            estadisticas = df[
                variables_numericas
            ].describe().T

            estadisticas["mediana"] = df[
                variables_numericas
            ].median()

            st.dataframe(
                estadisticas.round(2),
                use_container_width=True
            )


        # ==========================================
        # ITEM 4
        # ==========================================

        elif item == "Ítem 4: Valores nulos":

            st.subheader(
                "Ítem 4: Valores nulos"
            )

            nulos = df.isnull().sum()

            tabla = pd.DataFrame({
                "Variable": df.columns,
                "Valores nulos": nulos.values
            })

            st.dataframe(
                tabla,
                use_container_width=True
            )

            total_nulos = int(
                df.isnull().sum().sum()
            )

            st.metric(
                "Total de valores nulos",
                total_nulos
            )

            variables_con_nulos = tabla[
                tabla["Valores nulos"] > 0
            ]

            if len(variables_con_nulos) > 0:

                fig, ax = plt.subplots(
                    figsize=(10, 5)
                )

                ax.bar(
                    variables_con_nulos["Variable"],
                    variables_con_nulos["Valores nulos"]
                )

                ax.set_title(
                    "Valores nulos por variable"
                )

                plt.xticks(rotation=45)

                st.pyplot(fig)

                plt.close(fig)


        # ==========================================
        # ITEM 5
        # ==========================================

        elif item == "Ítem 5: Distribución numérica":

            st.subheader(
                "Ítem 5: Distribución de variables numéricas"
            )

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            for variable in variables_numericas:

                datos = pd.to_numeric(
                    df[variable],
                    errors="coerce"
                ).dropna()

                if len(datos) == 0:
                    continue

                st.write(
                    f"### Distribución de {variable}"
                )

                fig, ax = plt.subplots(
                    figsize=(9, 5)
                )

                ax.hist(
                    datos,
                    bins=20
                )

                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")
                ax.set_title(
                    f"Distribución de {variable}"
                )

                st.pyplot(fig)

                plt.close(fig)


        # ==========================================
        # ITEM 6
        # ==========================================

        elif item == "Ítem 6: Variables categóricas":

            st.subheader(
                "Ítem 6: Variables categóricas"
            )

            variables_categoricas = df.select_dtypes(
                include=["object", "category"]
            ).columns.tolist()

            for variable in variables_categoricas:

                st.write(
                    f"### {variable}"
                )

                conteo = (
                    df[variable]
                    .fillna("Valores nulos")
                    .astype(str)
                    .value_counts()
                )

                porcentaje = (
                    conteo / conteo.sum() * 100
                ).round(2)

                tabla = pd.DataFrame({
                    "Categoría": conteo.index,
                    "Frecuencia": conteo.values,
                    "Porcentaje (%)": porcentaje.values
                })

                st.dataframe(
                    tabla,
                    use_container_width=True
                )

                fig, ax = plt.subplots(
                    figsize=(10, 5)
                )

                ax.bar(
                    conteo.index.astype(str),
                    conteo.values
                )

                ax.set_title(
                    f"Distribución de {variable}"
                )

                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                plt.xticks(
                    rotation=45,
                    ha="right"
                )

                st.pyplot(fig)

                plt.close(fig)


        # ==========================================
        # ITEM 7
        # ==========================================

        elif item == "Ítem 7: Numérico vs categórico":

            st.subheader(
                "Ítem 7: Numérico vs categórico"
            )

            if "Churn" in df.columns:

                for variable in [
                    "MonthlyCharges",
                    "tenure"
                ]:

                    if (
                        variable in df.columns
                        and pd.api.types.is_numeric_dtype(
                            df[variable]
                        )
                    ):

                        st.write(
                            f"### {variable} vs Churn"
                        )

                        fig, ax = plt.subplots(
                            figsize=(8, 5)
                        )

                        sns.boxplot(
                            data=df,
                            x="Churn",
                            y=variable,
                            ax=ax
                        )

                        st.pyplot(fig)

                        plt.close(fig)

                        resumen = df.groupby(
                            "Churn"
                        )[variable].agg(
                            ["mean", "median", "std"]
                        )

                        st.dataframe(
                            resumen.round(2),
                            use_container_width=True
                        )


        # ==========================================
        # ITEM 8
        # ==========================================

        elif item == "Ítem 8: Categórico vs categórico":

            st.subheader(
                "Ítem 8: Categórico vs categórico"
            )

            if "Churn" in df.columns:

                for variable in [
                    "Contract",
                    "InternetService"
                ]:

                    if variable in df.columns:

                        st.write(
                            f"### {variable} vs Churn"
                        )

                        tabla = pd.crosstab(
                            df[variable],
                            df["Churn"]
                        )

                        st.dataframe(
                            tabla,
                            use_container_width=True
                        )

                        fig, ax = plt.subplots(
                            figsize=(9, 5)
                        )

                        tabla.plot(
                            kind="bar",
                            ax=ax
                        )

                        ax.set_title(
                            f"{variable} vs Churn"
                        )

                        ax.set_ylabel(
                            "Cantidad de clientes"
                        )

                        plt.xticks(
                            rotation=45,
                            ha="right"
                        )

                        st.pyplot(fig)

                        plt.close(fig)


        # ==========================================
        # ITEM 9
        # ==========================================

        elif item == "Ítem 9: Parámetros seleccionados":

            st.subheader(
                "Ítem 9: Parámetros seleccionados"
            )

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            variable = st.selectbox(
                "Seleccione una variable numérica",
                variables_numericas
            )

            datos = pd.to_numeric(
                df[variable],
                errors="coerce"
            ).dropna()

            fig, ax = plt.subplots(
                figsize=(9, 5)
            )

            ax.hist(
                datos,
                bins=20
            )

            ax.set_title(
                f"Distribución de {variable}"
            )

            st.pyplot(fig)

            plt.close(fig)


        # ==========================================
        # ITEM 10
        # ==========================================

        elif item == "Ítem 10: Hallazgos clave":

            st.subheader(
                "Ítem 10: Hallazgos clave"
            )

            if "Churn" in df.columns:

                churn = (
                    df["Churn"]
                    .astype(str)
                    .value_counts()
                )

                total = len(df)

                clientes_churn = churn.get(
                    "Yes",
                    0
                )

                tasa = (
                    clientes_churn / total * 100
                    if total > 0
                    else 0
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Clientes analizados",
                        total
                    )

                with col2:
                    st.metric(
                        "Tasa de Churn",
                        f"{tasa:.2f}%"
                    )

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.bar(
                    churn.index.astype(str),
                    churn.values
                )

                ax.set_title(
                    "Distribución de Churn"
                )

                ax.set_ylabel(
                    "Cantidad de clientes"
                )

                st.pyplot(fig)

                plt.close(fig)
