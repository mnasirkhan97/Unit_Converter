import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"meters": 1, "feet": 3.28084, "inches": 39.3701, "kilometers": 0.001, "miles": 0.000621371},
        "Weight": {"kilograms": 1, "pounds": 2.20462, "grams": 1000, "ounces": 35.274},
        "Temperature": {"celsius": 1, "fahrenheit": 1.8, "kelvin": 1},
        "Volume": {"liters": 1, "milliliters": 1000, "gallons": 0.264172, "cups": 4.22675}
    }
    
    if category == "Temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5/9
        elif from_unit == "celsius" and to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            return value - 273.15
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    
    return value * conversion_factors[category][to_unit] / conversion_factors[category][from_unit]

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    st.title("🔄 Unit Converter")
    st.write("Convert units instantly and accurately.")
    
    # Dark Mode Toggle
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
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"Converted: {value} {from_unit} = {result:.4f} {to_unit}")
    
    # Conversion History
    if "history" not in st.session_state:
        st.session_state.history = []
    if st.button("📜 Show History"):
        st.write("### Conversion History:")
        for record in st.session_state.history[-5:]:  # Show last 5 conversions
            st.write(record)
    
    if value and from_unit and to_unit:
        st.session_state.history.append(f"{value} {from_unit} → {to_unit} = {result:.4f}")

if __name__ == "__main__":
    main()

