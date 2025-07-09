import streamlit as st
import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Student performance prediction")

feature1 = st.number_input("Enter student id:")
feature2 = st.number_input("enter gender ('2' for others, '1' for male , '2' for female):")
feature3= st.number_input("enter age:")
feature4 = st.number_input("enter grade level:")
feature5 = st.number_input("enter math score:")
feature6 = st.number_input("enter reading score:")
feature7 = st.number_input("enter writing score:")
feature8 = st.number_input("enter attendance rate:")
feature9 = st.number_input("enter study hours:")
feature10 = st.number_input("enter internet access ('1' for yes ,'0' for no):")
feature11 = st.number_input("enter lunch type('0' for reduced , '1' for standard)")
feature12 = st.number_input("enter extra activities ('1' for yes , '0' for no)")

if st.button("Predict"):
    prediction = model.predict(np.array([[feature1,feature2,feature3,feature4,feature5,feature6,
                                            feature7,feature8,feature9,feature10,feature11,feature12]]))
    # if prediction>=0.5:
    #     print("pass")
    # else:
    #     print('fail')
    # st.success(f"Prediction: {prediction[0]}")
    result = "Pass" if prediction >= 0.5 else "Fail"

    st.markdown(f"### 🧠 Prediction: **{result}**")
    st.write(f"Model confidence (probability of 'Pass'): **{prediction[0]:.2f}**")
