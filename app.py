
import streamlit as st
import pint

st.set_page_config(page_title="Unit Converter by ABDULLAH RUSTAM",)

st.markdown("""
    <style>
	
        .tittle {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            padding: 20px;
            background-color: #f4f4f4;
            border-radius: 10px;
        }
        .stButton>button {
            background-image: linear-gradient(to right , #008bf8, #00abff, #00c5f2, #00d9c5, #00e78e, #00e78e, #00e78e, #00e78e, #00d9c5, #00c5f2, #00abff, #008bf8);	
            color: black;
            font-size: 19px;
            font-weight: bold;
            border-radius: 8px;
            padding: 12px;
            width: 100%;
            transition: all 0.3s ease-in-out;
            border: none;
        }
        .stButton>button:hover {
            background-image: linear-gradient(to left, #008bf8, #00abff, #00c5f2, #00d9c5, #00e78e, #00e78e, #00e78e, #00e78e, #00d9c5, #00c5f2, #00abff, #008bf8);	
            transform: scale(1.02);
            color: black;
        }
        .stSelectbox>div {
            border-radius: 8px;
            padding: 2px ;
            font-size: 18px;
            color: #2c3e50;
            background-image: linear-gradient(to right top, #008bf8, #00abff, #00c5f2, #00d9c5, #00e78e, #00e78e, #00e78e, #00e78e, #00d9c5, #00c5f2, #00abff, #008bf8);
            font-size: 16px;
        }
        .stNumberInput>div>div>div>input {
	    border-radius: 8px;
            padding: px;
            color: black;
	    font-size: 18px;
     font-weight: bold;
            background-image: linear-gradient(to right top, #008bf8, #00abff, #00c5f2, #00d9c5, #00e78e, #00e78e, #00e78e, #00e78e, #00d9c5, #00c5f2, #00abff, #008bf8);	
            }
            
        .stMarkdown {
            color: black;
            font-size: 18px;
        }
        
    </style>
""", unsafe_allow_html=True)

units = pint.UnitRegistry()

unit_categories = {
    " Length": ["meter", "kilometer", "centimeter", "millimeter", "foot", "inch",],
    " Temperature": ["celsius", "fahrenheit", "kelvin"],
    " Volume": ["liter", "milliliter", "cubic_centimeter", "gallon",],
    " Weight": ["gram", "kilogram", "milligram", "ton", "pound",],
    " Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    " Energy": ["joule", "kilojoule", "calorie", "kilocalorie"],
    " Pressure": ["pascal", "bar", "atmosphere", "torr", "psi"],
    " Angle": ["radian", "degree", "gradian", "arcmin", "arcsec"],
}

st.markdown("<h1 class='tittle'>Unit Converter</h1>", unsafe_allow_html=True)
st.subheader("Enter Conversion Details")

col1, col2,col3 = st.columns(3)
with col1:
    category = st.selectbox("Category", list(unit_categories.keys()))
with col2:
    from_unit = st.selectbox("From Unit", unit_categories[category])
with col3:
    to_unit = st.selectbox("To Unit", unit_categories[category])

value = st.number_input("Enter Value:")


def convert_Area(value, from_unit, to_unit):
        return value * units(from_unit**2).to(to_unit**2).magnitude


if st.button("Convert "):
        if value == 0.00 or from_unit is None or to_unit is None :
             st.warning("Please enter value and select units")
        else:
            result = value * units(from_unit).to(to_unit).magnitude 
            st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

   

