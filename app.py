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
    print('Energy')
elif selected_category == 'Frequency':
    print('Frequency')
elif selected_category == 'Fuel Economy':
    print('Fuel Economy')
elif selected_category == 'Length':
    print('Length')
elif selected_category == 'Mass':
    print('Mass')
elif selected_category == 'Plane Angle':
    print('Plane Angle')
elif selected_category == 'Pressure':
    print('Pressure')
elif selected_category == 'Speed':
    print('Speed')
elif selected_category == 'Temperature':
    print('Temperature')
elif selected_category == 'Time':
    print('Time')

