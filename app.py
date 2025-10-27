import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Drehzahl-Visualisierung", page_icon="⚙️", layout="centered")

st.title("⚙️ Drehzahl-Visualisierung")
st.write("Gib die **U/min** und den **Kreisdurchmesser (in cm)** ein, um die Bewegung zu sehen:")

# Eingaben
rpm = st.number_input("Umdrehungen pro Minute (U/min)", min_value=1.0, max_value=10000.0, value=60.0, step=1.0)
durchmesser = st.number_input("Kreisdurchmesser (cm)", min_value=0.1, max_value=1000.0, value=10.0, step=0.1)

# Berechnungen
radius = durchmesser / 2 / 100  # in Meter
umfang = 2 * np.pi * radius
u_pro_sekunde = rpm / 60
v = umfang * u_pro_sekunde  # m/s

st.write(f"**Umfangsgeschwindigkeit:** {v:.2f} m/s ({v*3.6:.2f} km/h)")

# Session-State für Start/Stopp speichern
if "running" not in st.session_state:
    st.session_state.running = False

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start"):
        st.session_state.running = True
with col2:
    if st.button("⏸️ Stopp"):
        st.session_state.running = False

# Platzhalter für Plot
plot_area = st.empty()

# Animation
while st.session_state.running:
    angle = (time.time() * u_pro_sekunde * 2 * np.pi) % (2 * np.pi)

    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, color='lightgray', fill=False, linewidth=3)
    ax.add_artist(circle)
    ax.plot([0, radius * np.cos(angle)], [0, radius * np.sin(angle)], color='red', linewidth=3)

    ax.set_xlim(-radius * 1.2, radius * 1.2)
    ax.set_ylim(-radius * 1.2, radius * 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    plot_area.pyplot(fig)
    plt.close(fig)
    time.sleep(0.05)
