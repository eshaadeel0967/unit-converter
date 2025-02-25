import streamlit as st
import pint

# Initialize unit registry
ureg = pint.UnitRegistry()

# Dictionary to map category names to their unit registry names
unit_category_map = {
    "Area": "area",
    "Data Transfer Rate": "data_rate",
    "Digital Storage": "digital",
    "Energy": "energy",
    "Frequency": "frequency",
    "Fuel Economy": "fuel_efficiency",
    "Length": "length",
    "Mass": "mass",
    "Plane Angle": "angle",
    "Pressure": "pressure",
    "Speed": "speed",
    "Temperature": "temperature",
    "Time": "time",
    "Volume": "volume",
}

# Streamlit UI
st.title('🌍 Google-Like Unit Converter')

# Select measurement category
measurement_categories = list(unit_category_map.keys())
selected_category = st.selectbox("Select Measurement Type", measurement_categories)

# Define unit options for each category
unit_options = {
    "Area": ["square_meter", "square_kilometer", "square_mile", "square_yard", "acre", "hectare"],
    "Data Transfer Rate": ["bit_per_second", "kilobit_per_second", "megabit_per_second", "gigabit_per_second"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["mile_per_gallon", "kilometer_per_liter"],
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Mass": ["kilogram", "gram", "milligram", "ton", "pound", "ounce"],
    "Plane Angle": ["radian", "degree", "gradian"],
    "Pressure": ["pascal", "bar", "psi", "atm", "torr"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "knot"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Volume": ["liter", "milliliter", "cubic_meter", "gallon", "quart", "pint", "cup", "fluid_ounce"]
}

# Select units
from_unit = st.selectbox("From Unit:", unit_options[selected_category])
to_unit = st.selectbox("To Unit:", unit_options[selected_category])

# Input value
from_value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Function to handle conversion
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude, result.units
    except Exception as e:
        return None, str(e)

# Convert button
if st.button("Convert"):
    result, unit = convert_units(from_value, from_unit, to_unit)
    if result is not None:
        st.success(f"{from_value} {from_unit} = {result:.4f} {unit}")
    else:
        st.error(f"Conversion error: {unit}")
