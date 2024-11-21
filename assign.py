import streamlit as st

# Set the title of the web application
st.title("Thevenins theorem - 2205A21068")  # Replace with your roll number

# Function to calculate IL and PL
def calculate(Vth, Rth, RL):
    IL = Vth / (Rth + RL)  # Load current (IL)
    PL = IL * IL * RL      # Load power (PL)
    return IL, PL

# Input fields for Vth, Rth, and RL
Vth = st.number_input("Enter Vth (Volts):", value=0.0)
Rth = st.number_input("Enter Rth (Ohms):", value=0.0)
RL = st.number_input("Enter RL (Ohms):", value=0.0)

# Button to perform calculation
if st.button("Calculate"):
    IL, PL = calculate(Vth, Rth, RL)
    st.write(f"Load Current (IL): {IL:.4f} A")
    st.write(f"Load Power (PL): {PL:.4f} W")