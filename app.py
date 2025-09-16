import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre
st.title("🚀 Tableau de bord Trading")
st.write("Bienvenue dans mon application de trading basée sur l'analyse fondamentale et graphique.")

# Exemple de signal
st.subheader("Exemple de signal fictif")
signal = "Achat fort sur EUR/USD"
st.success(f"Signal actuel : {signal}")

# Générer des données fictives (simuler un prix EUR/USD)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Afficher un graphique
st.subheader("Graphique EUR/USD")
fig, ax = plt.subplots()
ax.plot(x, y, label="Prix EUR/USD")
ax.legend()
st.pyplot(fig)
