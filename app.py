import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Df = pd.read_csv("datostaller.csv")

st.tittle("Taller")

tab1, tab2, tab3, tab4 = st.tabs(["Tab1", "Tab2", "Tab3", "Tab4"])

with tab1:
    st.header("Analisis grafico")

    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    sns.scatterplot(data = Df, x='Fecha', y='Tasa de política monetaria(Dato fin de mes)', ax=ax[0])
    sns.scatterplot(data = Df, x='Fecha', y='Tasa de política monetaria(Dato fin de año)', ax=ax[1])
    fig.tight_layout()

    st.pyplot(fig)

with tab2:


    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    sns.scatterplot(data = Df, x='Fecha', y= 'Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  año corrido)', ax=ax[0])
    sns.scatterplot(data = Df, x='Fecha', y='Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)', ax=ax[1])
    fig.tight_layout()

    st.pyplot(fig)

with tab3:

    
    fig, ax = plt.subplots(1, figsize=(10,4))
    sns.scatterplot(data = Df, x='Fecha', y='Tasa de desempleo - total nacional(Dato fin de mes)', ax=ax[0])
    fig.tight_layout()

    st.pyplot(fig)

with tab4:
    fig, ax = plt.subplots(1, figsize=(10,4))
    sns.scatterplot(data = Df, x='Fecha', y= 'Inflación total, anual(Dato fin de año)', ax=ax[0])
    fig.tight_layout()

    st.pyplot(fig)