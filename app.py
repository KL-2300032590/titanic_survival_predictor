import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Titanic Survival Predictor")
st.subheader("Enter the Passenger Details Below:-")

pclass = st.selectbox("Passenger Class (1=Upper,2=Middle ,3=Lower)",[1,2,3])
sex = st.selectbox("Sex",["male","female"])
age = st.slider("Age",1,80,25)
sibsp = st.slider("Number of Siblings/Spoues aboard",0,5,0)
fare = st.slider("Fare Paid",0.0,500.0,50.0)

sex_num = 0 if sex =="male" else 1
input_data = [[pclass,sex_num,age,sibsp,fare]]

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    result = "Survived" if prediction[0] == 1 else "Did Not Survive"
    st.success(f"Prediction: {result}")
