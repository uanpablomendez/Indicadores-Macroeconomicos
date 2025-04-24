import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("datostaller.csv")

# Corregir nombre del método
st.title("Taller")

# Crear pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Tab1", "Tab2", "Tab3", "Tab4"])

with tab1:
    st.header("Análisis gráfico: Tasa de política monetaria")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    sns.scatterplot(data=df, x='Fecha', y='Tasa de política monetaria(Dato fin de mes)', ax=ax[0])
    ax[0].set_title("Fin de mes")
    sns.scatterplot(data=df, x='Fecha', y='Tasa de política monetaria(Dato fin de año)', ax=ax[1])
    ax[1].set_title("Fin de año")
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    st.header("Producto Interno Bruto (PIB) real")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    sns.scatterplot(
        data=df, x='Fecha',
        y='Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  año corrido)',
        ax=ax[0]
    )
    ax[0].set_title("Variación porcentual año corrido")
    sns.scatterplot(
        data=df, x='Fecha',
        y='Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)',
        ax=ax[1]
    )
    ax[1].set_title("Fin de trimestre")
    fig.tight_layout()
    st.pyplot(fig)

with tab3:
    st.header("Tasa de desempleo")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df, x='Fecha', y='Tasa de desempleo - total nacional(Dato fin de mes)', ax=ax)
    ax.set_title("Fin de mes")
    fig.tight_layout()
    st.pyplot(fig)

with tab4:
    st.header("Inflación total anual")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df, x='Fecha', y='Inflación total, anual(Dato fin de año)', ax=ax)
    ax.set_title("Fin de año")
    fig.tight_layout()
    st.pyplot(fig)
