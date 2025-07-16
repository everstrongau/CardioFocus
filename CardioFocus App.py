
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
        display: flex;
        justify-content: space-between;
    }

    .left-box, .right-box {
        flex: 1;
        padding: 20px;
        margin: 5px;
        border-radius: 10px;
        color: black;
        font-weight: bold;
        text-align: center;
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

zone_labels = [
    "ZONE 5<br>90–100% MaxHR",
    "ZONE 4<br>80–90% MaxHR",
    "ZONE 3<br>70–80% MaxHR",
    "ZONE 2<br>60–70% MaxHR",
    "ZONE 1<br>50–60% MaxHR"
]

zone_colors_left = ['#EB5757', '#F2994A', '#F2C94C', '#D8DC8D', '#B7DDB0']
zone_colors_right = ['#FFCFCF', '#FFE4C2', '#FFF1BF', '#F9F9C5', '#EDFDF3']
output_texts = [""] * 5

if st.button("Calculate HR Zones"):
    hr_max = 220 - age
    zones = [
        (round(hr_max * 0.90), hr_max),
        (round(hr_max * 0.80), round(hr_max * 0.90)),
        (round(hr_max * 0.70), round(hr_max * 0.80)),
        (round(hr_max * 0.60), round(hr_max * 0.70)),
        (round(hr_max * 0.50), round(hr_max * 0.60))
    ]
    for i in range(5):
        output_texts[i] = f"{zones[i][0]}–{zones[i][1]} BPM"

# Display side-by-side zone boxes
for i in range(5):
    st.markdown(f"""
        <div class="zone-box">
            <div class="left-box" style="background-color: {zone_colors_left[i]};">
                <div style="font-size: 28px;">{zone_labels[i]}</div>
            </div>
            <div class="right-box" style="background-color: {zone_colors_right[i]};">
                <div style="font-size: 28px;">{output_texts[i]}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# VO2max Estimator
st.markdown("""<br><div class='big-font'>VO₂max calculator (3-minute step test)</div>""", unsafe_allow_html=True)
gender = st.selectbox("Select your gender:", ["Male", "Female"])
height = st.number_input("Enter your height (cm):", min_value=100, max_value=220, value=170, step=1, format="%d")
weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70, step=1, format="%d")
recovery_hr = st.number_input("Enter your heart rate (1-minute post test):", min_value=40, max_value=200, value=100, step=1, format="%d")

if st.button("Calculate VO₂max"):
    if gender == "Male":
        vo2max = 70.597 - 0.246 * age - 0.122 * weight - 0.265 * recovery_hr + 0.106 * height
    else:
        vo2max = 70.597 - 0.185 * age - 0.118 * weight - 0.218 * recovery_hr + 0.074 * height

    st.markdown(f"<div style='font-weight:bold; font-size:28px;'>Estimated VO₂max: {vo2max:.2f} ml/kg/min</div>", unsafe_allow_html=True)

