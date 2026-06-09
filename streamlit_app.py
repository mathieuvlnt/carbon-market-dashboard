import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Configuration
st.set_page_config(
    page_title="Carbon Market Dashboard",
    layout="wide"
)

# Chargement données
@st.cache_data
def load_data():

    eua = pd.read_csv("European Union Carbon Permits Allowance (EUA) Yearly Futures Historical Data.csv")

    eua["Date"] = pd.to_datetime(eua["Date"], format="%m/%d/%Y")

    eua = (eua.sort_values("Date").set_index("Date"))

    ttf = yf.download("TTF=F",start="2018-01-01", progress=False)

    brent = yf.download("BZ=F", start="2018-01-01", progress=False)

    # Extraction des prix de clôture
    ttf_price = ttf[("Close", "TTF=F")]
    ttf_price.name = "TTF"

    brent_price = brent[("Close", "BZ=F")]
    brent_price.name = "BRENT"

    eua_price = eua["Price"].copy()
    eua_price.name = "EUA"

    # Fusion
    market_data = pd.concat([eua_price, ttf_price, brent_price], axis=1).dropna()

    return market_data


market_data = load_data()

# Sidebar
st.sidebar.title("Paramètres")

start_date = st.sidebar.date_input(
    "Date de début",
    value=market_data.index.min()
)

end_date = st.sidebar.date_input(
    "Date de fin",
    value=market_data.index.max()
)

market_data = market_data.loc[
    str(start_date):str(end_date)
]

# Titre
st.title("Carbon Market Dashboard & Risk Analysis")

st.markdown("""
**Mathieu Voluntario**  
EDHEC Business School  
Programme Grande École – Data Science & Finance
""")

st.markdown("""Analyse quantitative du marché européen du carbone (EUA) et de ses relations avec le gaz naturel TTF et le Brent.""")

# Principaux Indicateurs
st.header("Niveaux de marché")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Prix EUA",
    f"{market_data['EUA'].iloc[-1]:.2f} €/tCO₂"
)

col2.metric(
    "Prix TTF",
    f"{market_data['TTF'].iloc[-1]:.2f} €/MWh"
)

col3.metric(
    "Prix Brent",
    f"{market_data['BRENT'].iloc[-1]:.2f} $"
)

# Prix historiques
st.header("Marchés énergie & carbone")

fig_prices = px.line(
    market_data,
    title="Evolution des prix"
)

fig_prices.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Prix"
)

st.plotly_chart(
    fig_prices,
    use_container_width=True
)

# Performance relative
st.header("Performance relative (Base 100)")

normalized = market_data / market_data.iloc[0] * 100

fig_perf = px.line(
    normalized,
    title="Performance relative des actifs"
)

fig_perf.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Base 100"
)

st.plotly_chart(
    fig_perf,
    use_container_width=True
)

# Rendements
returns = market_data.pct_change().dropna()

# Volatilité EUA
st.header("Volatilité du marché carbone")

vol30 = (
    returns["EUA"]
    .rolling(30)
    .std()
    * np.sqrt(252)
)

vol90 = (
    returns["EUA"]
    .rolling(90)
    .std()
    * np.sqrt(252)
)

vol_df = pd.concat(
    [vol30, vol90],
    axis=1
)

vol_df.columns = [
    "Volatilité 30 jours",
    "Volatilité 90 jours"
]

fig_vol = px.line(
    vol_df,
    title="Volatilité glissante des EUA"
)

fig_vol.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Volatilité annualisée"
)

st.plotly_chart(
    fig_vol,
    use_container_width=True
)

# Drawdown
st.header("Drawdown historique")

cum_perf = (
    1 + returns["EUA"]
).cumprod()

drawdown = (
    cum_perf
    / cum_perf.cummax()
    - 1
)

fig_dd = px.line(
    drawdown,
    title="Drawdown historique du marché EUA"
)

fig_dd.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Drawdown"
)

fig_dd.update_traces(
    line_color="red"
)

st.plotly_chart(
    fig_dd,
    use_container_width=True
)

# Corrélations
st.header("Analyse des corrélations")

corr_matrix = returns.corr()

fig_corr = px.imshow(
    corr_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Matrice de corrélation des rendements"
)

fig_corr.update_layout(
    template="plotly_dark",
    title_x=0.5
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)

# Corrélation glissante EUA - TTF
st.header("Corrélation dynamique EUA - TTF")

rolling_corr = (returns["EUA"]
    .rolling(90)
    .corr(returns["TTF"]))

rolling_corr.name = "EUA-TTF"

fig_roll = px.line(
    rolling_corr,
    title="Corrélation glissante 90 jours entre EUA et TTF")

fig_roll.add_hline(
    y=0,
    line_dash="dash"
)

fig_roll.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Corrélation"
)

st.plotly_chart(
    fig_roll,
    use_container_width=True
)

# Indicateurs risque
st.header("Indicateurs de risque")

col1, col2, col3 = st.columns(3)

vol_current = (
    returns["EUA"]
    .rolling(30)
    .std()
    .iloc[-1]
    * np.sqrt(252)
)

drawdown_max = drawdown.min()

corr_current = rolling_corr.iloc[-1]

col1.metric("Volatilité 30 jours", f"{vol_current:.2%}")

col2.metric("Drawdown maximal", f"{drawdown_max:.2%}")

col3.metric("Corrélation EUA-TTF", f"{corr_current:.2f}")