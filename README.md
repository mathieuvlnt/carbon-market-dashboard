# Carbon Market Dashboard & Risk Analysis

## Présentation

Ce projet a pour objectif d'analyser le marché européen des quotas carbone (EUA) ainsi que ses interactions avec les principaux marchés de l'énergie.

L'étude repose sur les prix des EUA, du gaz naturel TTF et du Brent afin d'examiner :

* l'évolution du marché carbone depuis 2018 ;
* les rendements et la volatilité ;
* les drawdowns ;
* les corrélations avec les marchés énergétiques ;
* l'impact de la crise énergétique européenne de 2022 ;
* la capacité de certaines variables de marché à expliquer les rendements futurs des EUA.

---

## Principaux résultats

* Les EUA sont passés d'environ **8 €/tCO₂** en 2018 à près de **100 €/tCO₂** en 2023.
* La volatilité historique annualisée du marché carbone ressort à environ **42 %**.
* La relation entre les EUA et le TTF varie fortement selon les périodes de marché.
* La crise énergétique européenne de 2022 s'accompagne d'une rupture temporaire de la corrélation EUA–TTF.
* Les variables de marché simples présentent un pouvoir prédictif limité sur les rendements futurs des EUA.

---

## Dashboard Streamlit

Le projet comprend également un dashboard interactif permettant de visualiser :

* les prix historiques ;
* la performance relative des actifs ;
* la volatilité du marché carbone ;
* les drawdowns ;
* les corrélations ;
* la corrélation glissante EUA–TTF ;
* plusieurs indicateurs de risque.

---

## Outils utilisés

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* yfinance
* scikit-learn

---

## Limites

Cette étude repose principalement sur des données de marché publiques et sur des méthodes volontairement simples et interprétables.

Les résultats pourraient être enrichis par l'intégration de données fondamentales du système ETS et des marchés européens de l'électricité.

---

# English Version

## Overview

This project analyzes the European carbon market (EUA) and its interactions with major energy markets.

Using historical EUA, Dutch TTF natural gas and Brent crude oil prices, the study focuses on:

* carbon market dynamics since 2018;
* returns and volatility;
* drawdowns;
* correlations with energy markets;
* the impact of the 2022 European energy crisis;
* the ability of simple market variables to explain future EUA returns.

---

## Key Findings

* EUA prices increased from roughly **€8/tCO₂** in 2018 to nearly **€100/tCO₂** in 2023.
* Historical annualized volatility is approximately **42%**.
* The relationship between EUA and TTF varies significantly across market regimes.
* The 2022 European energy crisis led to a temporary breakdown in the usual EUA–TTF relationship.
* Simple market variables provide limited predictive power for short-term EUA returns.

---

## Streamlit Dashboard

The project also includes an interactive dashboard featuring:

* historical prices;
* relative performance analysis;
* carbon market volatility;
* drawdowns;
* correlation analysis;
* rolling EUA–TTF correlations;
* market risk indicators.

---

## Tools

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* yfinance
* scikit-learn

---

## Limitations

This study mainly relies on public market data and intentionally uses simple and interpretable methodologies.

The analysis could be extended by incorporating ETS fundamental data and European power market data.
