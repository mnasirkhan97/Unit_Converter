import streamlit as st
from googletrans import Translator

def google_unit_converter(value, from_unit, to_unit):
    translator = Translator()
    query = f"{value} {from_unit} to {to_unit}"
    translated = translator.translate(query, src='en', dest='en')
    return translated.text

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    st.title("🔄 Unit Converter")
    st.write("Convert units using Google's translation API.")
    
    # Theme Toggle
    dark_mode = st.toggle("🌙 Dark Mode")
    if dark_mode:
        st.markdown("""<style>body { background-color: #121212; color: white; }</style>""", unsafe_allow_html=True)
    
    # Unit Categories
    unit_categories = {
        "Length": ["meters", "feet", "inches", "kilometers", "miles"],
        "Weight": ["kilograms", "pounds", "grams", "ounces"],
        "Temperature": ["celsius", "fahrenheit", "kelvin"],
        "Volume": ["liters", "milliliters", "gallons", "cups"]
    }
    
    # Select Category
    category = st.selectbox("Select Unit Category:", list(unit_categories.keys()))
    
    # Value Input
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)
    
    # Dropdowns for Unit Selection
    from_unit = st.selectbox("From Unit:", unit_categories[category])
    to_unit = st.selectbox("To Unit:", unit_categories[category])
    
    # Convert Button
    if st.button("Convert 🔄"):
        if value and from_unit and to_unit:
            result = google_unit_converter(value, from_unit, to_unit)
            st.success(f"Converted: {result}")
        else:
            st.warning("Please enter all values correctly.")
    
    # Conversion History
    if "history" not in st.session_state:
        st.session_state.history = []
    if st.button("📜 Show History"):
        st.write("### Conversion History:")
        for record in st.session_state.history[-5:]:  # Show last 5 conversions
            st.write(record)
    
    if value and from_unit and to_unit:
        st.session_state.history.append(f"{value} {from_unit} → {to_unit}")

if __name__ == "__main__":
    main()
