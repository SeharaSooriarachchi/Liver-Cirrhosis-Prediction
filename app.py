import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("best_xgb_model.pkl","rb")
best_xgb_model=pickle.load(pickle_in)

# Load the trained model
#model_path = "best_xgb_model.pkl"  # Update this with the correct path if needed
#with open(model_path, 'rb') as file:
#    best_xgb_model = pickle.load(file)

def predict_stage(features):
    """Function to predict the stage of cirrhosis using the XGBoost model."""
    prediction = best_xgb_model.predict([features])
    return prediction[0]

def main():
    #st.title("CIRRHOSIS STAGE PREDICTOR")

    # HTML for styling
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">CIRRHOSIS STAGE PREDICTOR</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create input fields for each feature
    N_Days = st.number_input("N_Days", min_value=0, step=1)
    Bilirubin = st.number_input("Bilirubin", format="%.2f")
    Cholesterol = st.number_input("Cholesterol", format="%.2f")
    Albumin = st.number_input("Albumin", format="%.2f")
    Copper = st.number_input("Copper", format="%.2f")
    SGOT = st.number_input("SGOT", format="%.2f")
    Tryglicerides = st.number_input("Tryglicerides", format="%.2f")
    Platelets = st.number_input("Platelets", format="%.2f")
    Prothrombin = st.number_input("Prothrombin", format="%.2f")
    Alk_Phos = st.number_input("Alk_Phos", format="%.2f")
    Age = st.number_input("Age", min_value=0, step=1)
    
    # For categorical variables, use select boxes
    Status = st.selectbox("Status", options=[0, 1, 2])  # Adjust based on your mapping
    Drug = st.selectbox("Drug", options=[0, 1])  # Adjust based on your mapping
    Sex = st.selectbox("Sex", options=[0, 1])  # Adjust based on your mapping
    Ascites = st.selectbox("Ascites", options=[0, 1])  # Adjust based on your mapping
    Hepatomegaly = st.selectbox("Hepatomegaly", options=[0, 1])  # Adjust based on your mapping
    Spiders = st.selectbox("Spiders", options=[0, 1])  # Adjust based on your mapping
    Edema = st.selectbox("Edema", options=[0, 1, 2])  # Adjust based on your mapping
    
    # Collect all the input features into a list
    features = [
        N_Days, Bilirubin, Cholesterol, Albumin, Copper, SGOT, 
        Tryglicerides, Platelets, Prothrombin,Alk_Phos, Age, Status, 
        Drug,Sex, Ascites, Hepatomegaly, Spiders, Edema
    ]
    
    # When the 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_stage(features)
        st.success(f"The predicted stage of cirrhosis is: {result}")

if __name__ == '__main__':
    main()

