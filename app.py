import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:  # Default case (replaces the empty elif)
        return "Conversion not supported."

# Streamlit UI
st.title("Unit Converter")
st.write("Welcome to the Unit Converter!")

value = st.number_input("Enter the value you want to convert:", min_value=0.0)
units = ["meters", "kilometers", "grams", "kilograms"]
unit_from = st.selectbox("Enter the value you want to Convert from:", units)
unit_to = st.selectbox("Convert to:", units)

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write("Converted value:", result)   
