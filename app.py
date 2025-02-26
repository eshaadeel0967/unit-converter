import streamlit as st
import pint

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

measurement_categories = list(unit_category_map.keys())
unit_type = {
    "Area":[
        "Square kilometre",
        "Square metre",
        "Square foot", 
        "Square inch", 
        "Square mile" ,
        "Square yard",
        "Acre", 
        "Hectare"],
    "Data Transfer Rate":[
    "Bit per second",
    "Kilobit per second",
    "Kilobyte per second",
    "Kibibit per second",
    "Megabit per second",
    "Megabyte per second",
    "Mebibit per second",
    "Gigabit per second",
    "Gigabyte per second",
    "Gibibit per second",
    "Terabit per second",
    "Terabyte per second",
    "Tebibit per second"
],
    "Digital Storage":[
    "Bit",
    "Kilobit",
    "Kibibit",
    "Megabit",
    "Gigabit",
    "Gibibit",
    "Terabit",
    "Tebibit",
    "Pebibit",
    "Byte",
    "Kilobyte",
    "Kibibyte",
    "Megabyte",
    "Gigabyte",
    "Gibibyte",
    "Terabyte",
    "Tebibyte",
    "Petabyte",
    "Pebibyte"
],
    "Energy": [
    "Joule",
    "Kilojoule",
    "Gram calorie",
    "Kilocalorie",
    "Watt hour",
    "Kilowatt-hour",
    "Electronvolt",
    "British thermal unit",
    "US therm",
    "Foot-pound"
],
    "Frequency": [
    "Hertz",
    "Kilohertz",
    "Megahertz",
    "Gigahertz"
],
    "Fuel Economy" : [
    "Mile per US gallon",
    "Mile per gallon",
    "Kilometer per liter",
    "Litre per 100 kilometres"
],
    "Length" : [
    "Kilometre",
    "Metre",
    "Centimetre",
    "Millimetre",
    "Micrometre",
    "Nanometre",
    "Mile",
    "Yard",
    "Foot",
    "Inch",
    "Nautical mile"
],
    "Mass" : [
    "Tonne",
    "Kilogram",
    "Gram",
    "Milligram",
    "Microgram",
    "Imperial ton",
    "US ton",
    "Stone",
    "Pound",
    "Ounce"
],
    "Plane Angle" : [
    "Arcsecond",
    "Degree",
    "Gradian",
    "Milliradian",
    "Minute of arc",
    "Radian"
],
    "Pressure" : [
    "Bar", 
    "Pascal", 
    "Pound per square inch", 
    "Standard atmosphere", 
    "Torr"],
    "Speed" :  [
    "Mile per hour", 
    "Foot per second", 
    "Metre per second", 
    "Kilometre per hour", 
    "Knot"
],
    "Temperature" :  [
    "Degree Celsius", 
    "Fahrenheit", 
    "Kelvin"
],
    "Time" : [
    "Nanosecond", 
    "Microsecond", 
    "Millisecond",
    "Second", 
    "Minute",
    "Hour", 
    "Day", 
    "Week", 
    "Month", 
    "Calendar year", 
    "Decade", 
    "Century"
],
    "Volume" : [
    "US liquid gallon",  
    "US liquid quart" ,
    "US liquid pint",
    "US legal cup"   , 
    "US fluid ounce" ,
    "US tablespoon"  ,
    "US teaspoon"  ,
    "Cubic meter"   , 
    "Liter"  ,
    "Milliliter",  
    "Imperial gallon",  
    "Imperial quart"  ,
    "Imperial pint"  ,
    "Imperial cup"  ,
    "Imperial fluid ounce",
    "Imperial tablespoon"  ,
    "Imperial teaspoon"  ,
    "Cubic foot"  ,
    "Cubic inch"  
]
}
st.title('Unit Converter')

selected_category= st.selectbox('Select Measurement Type', measurement_categories)

ureg = pint.UnitRegistry()

from_unit = st.selectbox("From Unit:", unit_type[selected_category])
to_unit = st.selectbox("To Unit:", unit_type[selected_category])



if selected_category == 'Area':
    from_value= st.number_input("From:", min_value=1)
    from_unit = st.selectbox(
       "From unit:", 
       unit_type ,
    )
    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )

elif selected_category == 'Data Transfer Rate':
   
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
   
elif selected_category == 'Digital Storage':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Energy':
    
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
    
elif selected_category == 'Frequency':

    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Fuel Economy':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )

elif selected_category == 'Length':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )

elif selected_category == 'Mass':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Plane Angle':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Pressure':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
    
    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )

elif selected_category == 'Speed':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Temperature':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )
elif selected_category == 'Time':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )

elif selected_category == 'Volume':
    from_value= st.number_input("From:")
    from_unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

    result= st.text_input("To:")
    to_unit = st.selectbox(
       "To unit:", 
       unit_type ,
    )