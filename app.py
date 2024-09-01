import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

# Load the trained model
pickle_in = open("best_xgb_model.pkl", "rb")
best_xgb_model = pickle.load(pickle_in)

def predict_stage(features):
    """Function to predict the stage of cirrhosis using the XGBoost model."""
    prediction = best_xgb_model.predict([features])
    return prediction[0]

def main():
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
    
    # For categorical variables, display original categories
    Status = st.selectbox("Status", options=["C", "CL", "D"])
    Drug = st.selectbox("Drug", options=["Placebo", "D-penicillamine"])
    Sex = st.selectbox("Sex", options=["Female", "Male"])
    Ascites = st.selectbox("Ascites", options=["No", "Yes"])
    Hepatomegaly = st.selectbox("Hepatomegaly", options=["No", "Yes"])
    Spiders = st.selectbox("Spiders", options=["No", "Yes"])
    Edema = st.selectbox("Edema", options=["No Edema", "Edema Present or Resolved by Diuretics", "Edema Despite Diuretic Therapy"])
    
    # Map the selected options to their corresponding numerical values
    status_map = {"C": 0, "CL": 1, "D": 2}
    drug_map = {"Placebo": 0, "D-penicillamine": 1}
    sex_map = {"Female": 0, "Male": 1}
    ascites_map = {"No": 0, "Yes": 1}
    hepatomegaly_map = {"No": 0, "Yes": 1}
    spiders_map = {"No": 0, "Yes": 1}
    edema_map = {"No Edema": 0, "Edema Present or Resolved by Diuretics": 1, "Edema Despite Diuretic Therapy": 2}
    
    # Apply the mapping
    features = [
        N_Days, Bilirubin, Cholesterol, Albumin, Copper, SGOT, 
        Tryglicerides, Platelets, Prothrombin, Alk_Phos, Age,
        status_map[Status], drug_map[Drug], sex_map[Sex], 
        ascites_map[Ascites], hepatomegaly_map[Hepatomegaly], 
        spiders_map[Spiders], edema_map[Edema]
    ]
    
    # When the 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_stage(features)
        st.success(f"The predicted stage of cirrhosis is: {result}")

if __name__ == '__main__':
    main()
