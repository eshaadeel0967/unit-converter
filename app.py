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

st.form('Unit converter')
selected_category= st.selectbox('Types', measurement_categories)

if selected_category == 'Area':
    print('Area')
elif selected_category == 'Data Transfer Rate':
    print('Data Transfer Rate')
elif selected_category == 'Digital Storage':
    print('Digital Storage')
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

