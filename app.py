import streamlit as st
from googletrans import Translator

def google_unit_converter(value, from_unit, to_unit):
    translator = Translator()
    query = f"{value} {from_unit} to {to_unit}"
    translated = translator.translate(query, src='en', dest='en')
    return translated.text

def main():
    st.title("Google Unit Converter")
    st.write("Convert units using Google's translation API.")
    
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)
    from_unit = st.text_input("From Unit (e.g., meters, kg, celsius):")
    to_unit = st.text_input("To Unit (e.g., feet, pounds, fahrenheit):")
    
    if st.button("Convert"):
        if value and from_unit and to_unit:
            result = google_unit_converter(value, from_unit, to_unit)
            st.success(f"Converted: {result}")
        else:
            st.warning("Please enter all values correctly.")

if __name__ == "__main__":
    main()
