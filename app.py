import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open('Student.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🎓 Student Performance Prediction")

# Text inputs (blank by default)
feature1 = st.text_input("Enter student id:")
feature2 = st.text_input("Enter gender ('2' for others, '1' for male, '0' for female):")
feature3 = st.text_input("Enter age:")
feature4 = st.text_input("Enter grade level:")
feature5 = st.text_input("Enter math score:")
feature6 = st.text_input("Enter reading score:")
feature7 = st.text_input("Enter writing score:")
feature8 = st.text_input("Enter attendance rate:")
feature9 = st.text_input("Enter study hours:")
feature10 = st.text_input("Enter internet access ('1' for yes, '0' for no):")
feature11 = st.text_input("Enter lunch type ('0' for reduced, '1' for standard):")
feature12 = st.text_input("Enter extra activities ('1' for yes, '0' for no):")

# Check if all fields are filled
inputs = [feature1, feature2, feature3, feature4, feature5, feature6,
          feature7, feature8, feature9, feature10, feature11, feature12]

if st.button("Predict"):
    if all(inputs):
        try:
            # Convert all inputs to float
            features = [float(i) for i in inputs]
            prediction = model.predict([features])

            # You can use thresholding logic or model.predict_proba() if available
            result = "Pass" if prediction[0] >= 0.5 else "Fail"

            st.markdown(f"### 🧠 Prediction: **{result}**")
            st.write(f"Model confidence (raw output): **{prediction[0]:.2f}**")

        except ValueError:
            st.error("❌ Please enter valid numbers in all fields.")
    else:
        st.warning("⚠️ Please fill in all the fields before predicting.")
