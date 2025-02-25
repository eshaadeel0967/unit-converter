import streamlit as st

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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
    
elif selected_category == 'Frequency':
    unit_type = [
    "Hertz",
    "Kilohertz",
    "Megahertz",
    "Gigahertz"
]
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
elif selected_category == 'Fuel Economy':
    unit_type = [
    "Mile per US gallon",
    "Mile per gallon",
    "Kilometer per liter",
    "Litre per 100 kilometres"
]
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
elif selected_category == 'Pressure':
    unit_type =[
    "Bar", 
    "Pascal", 
    "Pound per square inch", 
    "Standard atmosphere", 
    "Torr"]
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
    
elif selected_category == 'Speed':
    unit_type = [
    "Mile per hour", 
    "Foot per second", 
    "Metre per second", 
    "Kilometre per hour", 
    "Knot"
]
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )
elif selected_category == 'Temperature':
    unit_type = [
    "Degree Celsius", 
    "Fahrenheit", 
    "Kelvin"
]
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
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
    input= st.text_input("From:")
    unit = st.selectbox(
       "From unit:", 
       unit_type , 
        index=1  
    )

