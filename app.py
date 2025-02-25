import streamlit as st
import pint

measurement_categories = [
    "Area",
    "Data Transfer Rate",
    "Digital Storage",
    "Energy",
    "Frequency",
    "Fuel Economy",
    "Length",
    "Mass",
    "Plane Angle",
    "Pressure",
    "Speed",
    "Temperature",
    "Time",
    "Volume"
]
st.title('Unit Converter')

selected_category= st.selectbox('', measurement_categories)

ureg = pint.UnitRegistry()



if selected_category == 'Area':
    unit_type = [
    "Square kilometre",
    "Square metre",
    "Square foot", 
    "Square inch", 
    "Square mile" ,
    "Square yard",
    "Acre", 
    "Hectare"
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
]
    from_value= st.text_input("From:")
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
    unit_type = [
    "Hertz",
    "Kilohertz",
    "Megahertz",
    "Gigahertz"
]
    from_value= st.text_input("From:")
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
    unit_type = [
    "Mile per US gallon",
    "Mile per gallon",
    "Kilometer per liter",
    "Litre per 100 kilometres"
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
]
    from_value= st.text_input("From:")
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
    unit_type =[
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
]
    from_value= st.text_input("From:")
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
    unit_type = [
    "Arcsecond",
    "Degree",
    "Gradian",
    "Milliradian",
    "Minute of arc",
    "Radian"
]
    from_value= st.text_input("From:")
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
    unit_type =[
    "Bar", 
    "Pascal", 
    "Pound per square inch", 
    "Standard atmosphere", 
    "Torr"]
    from_value= st.text_input("From:")
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
    unit_type = [
    "Mile per hour", 
    "Foot per second", 
    "Metre per second", 
    "Kilometre per hour", 
    "Knot"
]
    from_value= st.text_input("From:")
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
    unit_type = [
    "Degree Celsius", 
    "Fahrenheit", 
    "Kelvin"
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
]
    from_value= st.text_input("From:")
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
    unit_type = [
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
    from_value= st.text_input("From:")
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