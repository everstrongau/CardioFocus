
import streamlit as st

# Set page config and apply light theme
st.set_page_config(page_title="EverStrong CardioFocus", layout="centered", initial_sidebar_state="auto")

# Custom CSS for fonts, spacing, and background
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'League Spartan', sans-serif;
            font-size: 24px;
            background-color: #f2f2f2;
        }

        h1, h2, h3 {
            font-family: 'League Spartan', sans-serif;
            font-weight: 700;
            line-height: 1.1;
            margin-bottom: 0.3em;
        }

        .stTextInput input::-webkit-outer-spin-button,
        .stTextInput input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }

        .stTextInput input[type=number] {
            -moz-appearance: textfield;
        }

        .zone-box {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 8px;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>EverStrong CardioFocus</h1>", unsafe_allow_html=True)
st.markdown("<h2>Heart Rate Zone Calculator</h2>", unsafe_allow_html=True)

age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1, format="%d")

if age:
    hr_max = 220 - age
    zones = [
        ("Zone 5 – 90–100%", '#EB5757', round(hr_max * 0.90), hr_max),
        ("Zone 4 – 80–90%", '#F2994A', round(hr_max * 0.80), round(hr_max * 0.90)),
        ("Zone 3 – 70–80%", '#F2C94C', round(hr_max * 0.70), round(hr_max * 0.80)),
        ("Zone 2 – 60–70%", '#D8DC8D', round(hr_max * 0.60), round(hr_max * 0.70)),
        ("Zone 1 – 50–60%", '#B7DDB0', round(hr_max * 0.50), round(hr_max * 0.60)),
    ]

    for label, color, low, high in zones:
        st.markdown(f"<div class='zone-box' style='background-color:{color}'>{label}: {low}–{high} BPM</div>", unsafe_allow_html=True)

