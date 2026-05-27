# 📊 Real-Time Portfolio Optimization & Value at Risk (VaR) Engine

[![Streamlit App](https://streamlit.io)](https://financiero-2026.streamlit.app/)

## 🎯 Objetivo del Proyecto
Este proyecto es una aplicación web interactiva diseñada para analistas financieros y gestores de riesgos. Permite calcular la distribución óptima de un portafolio de inversión en tiempo real utilizando la API de Yahoo Finance y cuantificar la pérdida máxima potencial mediante la métrica **Value at Risk (VaR)** bajo el enfoque histórico (95% de confianza).

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3
* **Librerías Clave:** 
  * `Streamlit` (Interfaz web e interactividad)
  * `yfinance` (Ingesta de datos financieros en tiempo real)
  * `NumPy` & `Pandas` (Cálculo matricial y manipulación de series temporales)
  * `SciPy` (Cálculo estadístico)

## 📊 Conceptos Financieros Implementados
1. **Retorno Diario de Portafolio:** Cálculo matricial del rendimiento ponderado basado en los cierres ajustados históricos de los activos seleccionados.
2. **Value at Risk (VaR) Histórico:** Determinación no paramétrica de la pérdida máxima potencial. Un VaR diario del 95% indica que existe solo un 5% de probabilidad de sufrir una pérdida superior al monto calculado en un solo día de mercado.

## 🚀 Cómo Ejecutar el Proyecto Localmente

1. Clonar el repositorio:
   ```bash
   git clone https://github.com
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Correr la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📈 Impacto de Negocio
Sustituye los procesos manuales de extracción de datos con archivos Excel por un pipeline automatizado y una interfaz limpia que permite realizar simulaciones de riesgo al instante frente a clientes o comités de inversión.
