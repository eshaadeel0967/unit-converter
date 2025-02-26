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
    "Frequency": [
        "hertz", 
        "kilohertz", 
        "megahertz", 
        "gigahertz"
    ],
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

import pint

# Create a custom unit registry
ureg = pint.UnitRegistry()

ureg.define("square_meter = meter ** 2 = sq_m")
ureg.define("square_kilometer = 1e6 * square_meter = sq_km")
ureg.define("square_yard = 0.836127 * square_meter = sq_yd")
ureg.define("kilobit_per_second = 1000 * bit / second")
ureg.define("kibibit_per_second = 1024 * bit / second")
ureg.define("mebibit_per_second = 1024 ** 2 * bit / second")
ureg.define("gibibit_per_second = 1024 ** 3 * bit / second")
ureg.define("tebibit_per_second = 1024 ** 4 * bit / second")
ureg.define("kibibit = 1024 * bit")
ureg.define("mebibit = 1024 ** 2 * bit")
ureg.define("gibibit = 1024 ** 3 * bit")
ureg.define("tebibit = 1024 ** 4 * bit")
ureg.define("pebibit = 1024 ** 5 * bit")
ureg.define("kibibyte = 1024 * byte")
ureg.define("mebibyte = 1024 ** 2 * byte")
ureg.define("gibibyte = 1024 ** 3 * byte")
ureg.define("tebibyte = 1024 ** 4 * byte")
ureg.define("pebibyte = 1024 ** 5 * byte")
ureg.define("gram_calorie = 4.184 * joule")  # 1 calorie (small calorie) = 4.184 joules
ureg.define("kilocalorie = 4184 * joule")  # 1 kilocalorie (food calorie) = 4184 joules
ureg.define("watt_hour = 3600 * joule")  # 1 Wh = 3600 joules
ureg.define("kilowatt_hour = 3.6e6 * joule")  # 1 kWh = 3.6e6 joules
ureg.define("electronvolt = 1.602176634e-19 * joule = eV")
ureg.define("btu = 1055.06 * joule")
ureg.define("us_therm = 105505585.257 * joule")  # US therm (approximate)
ureg.define("foot_pound = 1.3558179483314004 * joule")  # 1 foot-pound ≈ 1.35582 joules
ureg.define("us_gallon = 3.785411784 * liter")
ureg.define("imperial_gallon = 4.54609 * liter")
ureg.define("mile_per_us_gallon = mile / us_gallon")
ureg.define("mile_per_imperial_gallon = mile / imperial_gallon")
ureg.define("kilometer_per_liter = kilometer / liter")
ureg.define("liter_per_100km = 0.01 * liter / kilometer")
ureg.define("arcminute = 1/60 * degree")
ureg.define("arcsecond = 1/60 * arcminute")
ureg.define("gradian = 0.9 * degree")  # 1 gradian = 0.9 degrees
ureg.define("milliradian = 1e-3 * radian")
ureg.define("standard_atmosphere = 101325 * pascal")
ureg.define("torr = 133.322368 * pascal")
ureg.define("calendar_year = 365.25 * day")  # Average year accounting for leap years
ureg.define("decade = 10 * calendar_year")
ureg.define("century = 100 * calendar_year")
ureg.define("us_liquid_gallon = 3.785411784 * liter")
ureg.define("us_liquid_quart = us_liquid_gallon / 4")
ureg.define("us_liquid_pint = us_liquid_quart / 2")
ureg.define("us_fluid_ounce = us_liquid_gallon / 128")
ureg.define("us_tablespoon = us_fluid_ounce / 2")
ureg.define("us_teaspoon = us_tablespoon / 3")
ureg.define("imperial_gallon = 4.54609 * liter")
ureg.define("imperial_quart = imperial_gallon / 4")
ureg.define('imperial_ton = 1016.0469088 * kilogram')
ureg.define("imperial_pint = imperial_quart / 2")
ureg.define("imperial_cup = imperial_gallon / 10")  # Note: definitions for a cup can vary
ureg.define("imperial_fluid_ounce = imperial_gallon / 160")
ureg.define("imperial_tablespoon = imperial_fluid_ounce / 2")
ureg.define("imperial_teaspoon = imperial_tablespoon / 3")
ureg.define("cubic_foot = foot ** 3")
ureg.define("cubic_inch = inch ** 3")


st.title("Unit Converter")

selected_category = st.selectbox("Select Measurement Type", measurement_categories)

from_unit = st.selectbox("From Unit:", unit_type[selected_category])
to_unit = st.selectbox("To Unit:", unit_type[selected_category])


from_value = st.number_input("From:", min_value=1.0, format="%.2f")


def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude, result.units
    except Exception as e:
        return None, str(e)


result, unit = convert_units(from_value, from_unit, to_unit)
if result is not None:
    st.success(f"{from_value} {from_unit} = {result:.4f} {unit}")
else:
    st.error(f"Conversion error: {unit}")
