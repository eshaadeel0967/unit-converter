import streamlit as st
import pint

# Create a UnitRegistry
ureg = pint.UnitRegistry()

# Unit category mapping
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

# Define measurement categories and their corresponding unit names
measurement_categories = list(unit_category_map.keys())

unit_type = {
    "Area": [
        "square_kilometer",
        "square_meter",
        "square_foot",
        "square_inch",
        "square_mile",
        "square_yard",
        "acre",
        "hectare",
    ],
    "Data Transfer Rate": [
        "bit / second",
        "kilobit / second",
        "kilobyte / second",
        "kibibit / second",
        "megabit / second",
        "megabyte / second",
        "mebibit / second",
        "gigabit / second",
        "gigabyte / second",
        "gibibit / second",
        "terabit / second",
        "terabyte / second",
        "tebibit / second",
    ],
    "Digital Storage": [
        "bit",
        "kilobit",
        "kibibit",
        "megabit",
        "gigabit",
        "gibibit",
        "terabit",
        "tebibit",
        "pebibit",
        "byte",
        "kilobyte",
        "kibibyte",
        "megabyte",
        "gigabyte",
        "gibibyte",
        "terabyte",
        "tebibyte",
        "petabyte",
        "pebibyte",
    ],
    "Energy": [
        "joule",
        "kilojoule",
        "calorie",
        "kilocalorie",
        "watt_hour",
        "kilowatt_hour",
        "electronvolt",
        "btu",
        "therm",
        "foot_pound",
    ],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": [
        "mile / gallon",
        "mile / us_gallon",
        "kilometer / liter",
        "liter / 100_kilometer",
    ],
    "Length": [
        "kilometer",
        "meter",
        "centimeter",
        "millimeter",
        "micrometer",
        "nanometer",
        "mile",
        "yard",
        "foot",
        "inch",
        "nautical_mile",
    ],
    "Mass": [
        "tonne",
        "kilogram",
        "gram",
        "milligram",
        "microgram",
        "imperial_ton",
        "us_ton",
        "stone",
        "pound",
        "ounce",
    ],
    "Plane Angle": [
        "arcsecond",
        "degree",
        "gradian",
        "milliradian",
        "arcminute",
        "radian",
    ],
    "Pressure": ["bar", "pascal", "psi", "atmosphere", "torr"],
    "Speed": [
        "mile / hour",
        "foot / second",
        "meter / second",
        "kilometer / hour",
        "knot",
    ],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": [
        "nanosecond",
        "microsecond",
        "millisecond",
        "second",
        "minute",
        "hour",
        "day",
        "week",
        "month",
        "year",
        "decade",
        "century",
    ],
    "Volume": [
        "us_gallon",
        "us_quart",
        "us_pint",
        "us_cup",
        "us_fluid_ounce",
        "us_tablespoon",
        "us_teaspoon",
        "cubic_meter",
        "liter",
        "milliliter",
        "imperial_gallon",
        "imperial_quart",
        "imperial_pint",
        "imperial_cup",
        "imperial_fluid_ounce",
        "imperial_tablespoon",
        "imperial_teaspoon",
        "cubic_foot",
        "cubic_inch",
    ],
}

# Streamlit UI
st.title("Unit Converter")

selected_category = st.selectbox("Select Measurement Type", measurement_categories)

from_unit = st.selectbox("From Unit:", unit_type[selected_category])
to_unit = st.selectbox("To Unit:", unit_type[selected_category])

# Input value
from_value = st.number_input("Enter Value:", min_value=1.0, format="%.2f")


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
