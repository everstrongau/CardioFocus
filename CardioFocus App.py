
import streamlit as st
import math

# Set page config
st.set_page_config(page_title="EverStrong CardioFocus", layout="centered")

# Apply custom font and style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'League Spartan', sans-serif;
        font-size: 24px;
        background-color: #f2f2f2;
    }

    .big-font {
        font-size: 36px !important;
        font-weight: bold;
        line-height: 1.2;
        margin-bottom: 0.5em;
    }

    .zone-box {
        margin-bottom: 10px;
    }

    .main-title {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 30px;
    }

    .main-title span.ever {
        color: white;
    }

    .main-title span.strong {
        color: #6bc370;
    }

    .main-title span.cardiofocus {
        color: white;
    }

    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
      -webkit-appearance: none;
      margin: 0; 
    }

    input[type=number] {
      -moz-appearance: textfield;
    }
    </style>
""", unsafe_allow_html=True)

# Title with color blocks
st.markdown("""
    <div class="main-title big-font">
        <span class="ever">Ever</span><span class="strong">Strong</span> <span class="cardiofocus">CardioFocus</span>
    </div>
""", unsafe_allow_html=True)

# Heart Rate Zone Calculator Section
st.markdown('<div class="big-font">Heart Rate Zone Calculator</div>', unsafe_allow_html=True)
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=50, step=1, format="%d")

if age:
    hr_max = 220 - age
    zones = [
        (round(hr_max * 0.90), hr_max),
        (round(hr_max * 0.80), round(hr_max * 0.90)),
        (round(hr_max * 0.70), round(hr_max * 0.80)),
        (round(hr_max * 0.60), round(hr_max * 0.70)),
        (round(hr_max * 0.50), round(hr_max * 0.60))
    ]

    zone_labels = [
        "Zone 5 – 90–100%", "Zone 4 – 80–90%", "Zone 3 – 70–80%", "Zone 2 – 60–70%", "Zone 1 – 50–60%"
    ]
    zone_colors = ['#EB5757', '#F2994A', '#F2C94C', '#D8DC8D', '#B7DDB0']

    for i in range(5):
        st.markdown(f"""
            <div class="zone-box" style='background-color: {zone_colors[i]}; padding: 10px; border-radius: 5px;'>
                <strong style='color:black'>{zone_labels[i]}:</strong> <span style='color:black'>{zones[i][0]}–{zones[i][1]} BPM</span>
            </div>
        """, unsafe_allow_html=True)

# VO2max Estimator
st.markdown("""<br><div class='big-font'>VO₂max calculator (3-minute step test)</div>""", unsafe_allow_html=True)
gender = st.selectbox("Select your gender:", ["Male", "Female"])
height = st.number_input("Enter your height (cm):", min_value=100, max_value=220, value=170, step=1, format="%d")
weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70, step=1, format="%d")
recovery_hr = st.number_input("Enter your heart rate (1-minute post test):", min_value=40, max_value=200, value=100, step=1, format="%d")

if st.button("Estimate VO₂max"):
    if gender == "Male":
        vo2max = 70.597 - 0.246 * age - 0.122 * weight - 0.265 * recovery_hr + 0.106 * height
    else:
        vo2max = 70.597 - 0.185 * age - 0.118 * weight - 0.218 * recovery_hr + 0.074 * height

    st.success(f"Estimated VO₂max: {vo2max:.2f} ml/kg/min")

