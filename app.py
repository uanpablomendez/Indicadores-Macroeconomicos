import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Cargar datos y formatear fechas
df = pd.read_csv("datostaller.csv").dropna()
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

st.title("Taller Indicadores Macroeconómicos")

# Crear pestañas con títulos claros
tab1, tab2, tab3, tab4 = st.tabs([
    "Tasa de política monetaria",
    "Producto Interno Bruto (PIB)",
    "Tasa de desempleo",
    "Inflación anual"
])

with tab1:
    st.header("Tasa de política monetaria")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    
    sns.lineplot(data=df, x='Fecha', y='Tasa de política monetaria(Dato fin de mes)', ax=ax[0])
    ax[0].set_title("Fin de mes")
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax[0].tick_params(axis='x', rotation=45)

    sns.lineplot(data=df, x='Fecha', y='Tasa de política monetaria(Dato fin de año)', ax=ax[1])
    ax[1].set_title("Fin de año")
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax[1].tick_params(axis='x', rotation=45)

    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    st.header("Producto Interno Bruto (PIB) real")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    
    sns.lineplot(
        data=df, x='Fecha',
        y='Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  año corrido)',
        ax=ax[0]
    )
    ax[0].set_title("Variación porcentual año corrido")
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax[0].tick_params(axis='x', rotation=45)

    sns.lineplot(
        data=df, x='Fecha',
        y='Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)',
        ax=ax[1]
    )
    ax[1].set_title("Fin de trimestre")
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax[1].tick_params(axis='x', rotation=45)

    fig.tight_layout()
    st.pyplot(fig)

with tab3:
    st.header("Tasa de desempleo")
    fig, ax = plt.subplots(figsize=(10, 4))
    
    sns.lineplot(data=df, x='Fecha', y='Tasa de desempleo - total nacional(Dato fin de mes)', ax=ax)
    ax.set_title("Fin de mes")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.tick_params(axis='x', rotation=45)
    
    fig.tight_layout()
    st.pyplot(fig)

with tab4:
    st.header("Inflación total anual")
    fig, ax = plt.subplots(figsize=(10, 4))
    
    sns.lineplot(data=df, x='Fecha', y='Inflación total, anual(Dato fin de año)', ax=ax)
    ax.set_title("Fin de año")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.tick_params(axis='x', rotation=45)
    
    fig.tight_layout()
    st.pyplot(fig)
