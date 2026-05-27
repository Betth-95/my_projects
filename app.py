import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide") # Configura la app en modo ancho para mejores gráficos
st.title("📊 Optimizador de Portafolios & Gestión de Riesgo (VaR)")

# 1. Inputs dinámicos para el usuario
tickers_input = st.text_input("Ingresa los tickers separados por coma:", "AAPL, MSFT, GOOGL, AMZN")
tickers = [t.strip().upper() for t in tickers_input.split(",")]
monto = st.number_input("Monto total a invertir ($ USD):", value=1000000)

if st.button("Calcular Portafolio Óptimo y Riesgo"):
    # 2. Descarga de datos en tiempo real (último año)
    datos = yf.download(tickers, period='1y')['Adj Close']
    rendimientos = datos.pct_change().dropna()
    
    # 3. Asignación equitativa (Pesos del portafolio)
    pesos = np.array([1 / len(tickers)] * len(tickers))
    rend_portafolio = rendimientos.dot(pesos)
    
    # 4. Cálculo de VaR Histórico (95% de confianza)
    var_95_pct = -np.percentile(rend_portafolio, 5)
    var_95_usd = var_95_pct * monto
    
    # 5. Despliegue de métricas principales
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"### Rendimiento Promedio Diario: {rend_portafolio.mean()*100:.4f}%")
    with col2:
        st.metric(label="Valor en Riesgo (VaR 95% Diario)", value=f"${var_95_usd:,.2f} USD", 
                  delta=f"-{var_95_pct*100:.2f}% del capital", delta_color="inverse")
        
    st.markdown("---")
    
    # --- GRÁFICOS INTERACTIVOS CON PLOTLY ---
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        st.subheader("📈 Rendimiento Histórico Normalizado (Base 100)")
        # Normalizamos los precios para que todos partan desde 100 y sean comparables
        datos_normalizados = (datos / datos.iloc[0]) * 100
        fig_lineas = px.line(datos_normalizados, labels={'value': 'Precio Normalizado', 'fecha': 'Fecha'})
        fig_lineas.update_layout(legend_title_text='Activos', margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_lineas, use_container_width=True)
        
    with col_graf2:
        st.subheader("📊 Distribución de Rendimientos y Zona de Riesgo (VaR)")
        # Creamos el histograma interactivo
        df_hist = pd.DataFrame({'Rendimientos (%)': rend_portafolio * 100})
        fig_hist = px.histogram(df_hist, x='Rendimientos (%)', nbins=50, 
                                title=None, color_discrete_sequence=['#2b5c8f'])
        
        # Añadimos la línea roja interactiva del VaR
        fig_hist.add_vline(x=-var_95_pct * 100, line_dash="dash", line_color="red", line_width=3,
                           annotation_text=f"VaR 95% ({ -var_95_pct * 100:.2f}%)", annotation_position="top left")
        
        fig_hist.update_layout(yaxis_title_text='Frecuencia (Días)', margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_hist, use_container_width=True)
        