import streamlit as st

# Set page configuration
st.set_page_config(page_title="CardioFocus Calculator", layout="centered")

# Title
st.title("CardioFocus Training Tools")

# --- Heart Rate Zone Calculator ---
st.header("Heart Rate Zone Calculator")

# Input for age
age = st.number_input("Enter your age", min_value=1, max_value=120, value=50)

# Calculate HR zones
if age:
    hr_max = 220 - age
    zones = {
        "Zone 5 (90–100%)": f"{round(hr_max * 0.90)}–{hr_max} BPM",
        "Zone 4 (80–90%)": f"{round(hr_max * 0.80)}–{round(hr_max * 0.90)} BPM",
        "Zone 3 (70–80%)": f"{round(hr_max * 0.70)}–{round(hr_max * 0.80)} BPM",
        "Zone 2 (60–70%)": f"{round(hr_max * 0.60)}–{round(hr_max * 0.70)} BPM",
        "Zone 1 (50–60%)": f"{round(hr_max * 0.50)}–{round(hr_max * 0.60)} BPM",
    }

    st.subheader("Your Heart Rate Zones:")
    for zone, bpm in zones.items():
        st.text(f"{zone}: {bpm}")

# --- VO2max Calculator ---
st.header("VO₂max Calculator (3-Minute Step Test)")

# Inputs
gender = st.selectbox("Select your gender", ["Male", "Female"])
height_cm = st.number_input("Enter your height (cm)", min_value=100, max_value=250, value=170)
weight_kg = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, value=70)
hr_post = st.number_input("Enter your 1-minute post-exercise HR", min_value=30, max_value=200, value=90)

# Calculate VO2max
if gender and age and height_cm and weight_kg and hr_post:
    if gender == "Male":
        vo2max = 70.597 - (0.246 * age) + (0.077 * height_cm) - (0.222 * weight_kg) - (0.147 * hr_post)
    else:
        vo2max = 70.597 - (0.185 * age) + (0.097 * height_cm) - (0.246 * weight_kg) - (0.122 * hr_post)

    vo2max = round(vo2max, 2)
    st.success(f"Estimated VO₂max: {vo2max} mL/kg/min")
