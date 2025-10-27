import streamlit as st
import numpy as np

st.set_page_config(page_title="Drehzahl-Visualisierung", page_icon="⚙️", layout="centered")

st.title("⚙️ Drehzahl-Visualisierung (flüssig)")
st.write("Gib die **U/min** und den **Kreisdurchmesser (in cm)** ein:")

rpm = st.number_input("Umdrehungen pro Minute (U/min)", 1.0, 10000.0, 60.0, 1.0)
durchmesser = st.number_input("Kreisdurchmesser (cm)", 0.1, 1000.0, 10.0, 0.1)

radius = durchmesser / 2
umfang = np.pi * durchmesser
v = umfang * rpm / 60 / 100  # m/s

st.write(f"**Umfangsgeschwindigkeit:** {v:.2f} m/s ({v*3.6:.2f} km/h)")

canvas_html = f"""
<canvas id="circleCanvas" width="300" height="300"></canvas>
<script>
const canvas = document.getElementById('circleCanvas');
const ctx = canvas.getContext('2d');
const rpm = {rpm};
let angle = 0;
function draw() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.arc(150, 150, 100, 0, 2*Math.PI);
  ctx.strokeStyle = '#888';
  ctx.lineWidth = 3;
  ctx.stroke();
  const rad = angle * Math.PI / 180;
  const x = 150 + 100 * Math.cos(rad);
  const y = 150 + 100 * Math.sin(rad);
  ctx.beginPath();
  ctx.moveTo(150,150);
  ctx.lineTo(x,y);
  ctx.strokeStyle = 'red';
  ctx.lineWidth = 4;
  ctx.stroke();
  angle += rpm * 360 / 60 / 60; // 60 fps
  if (angle > 360) angle -= 360;
  requestAnimationFrame(draw);
}}
draw();
</script>
"""

st.components.v1.html(canvas_html, height=320)
