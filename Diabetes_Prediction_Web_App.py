import numpy as np
import pickle
import streamlit as st
import joblib

# loading the saved model
# loaded_model = pickle.load(open('C:/Users/user/Desktop/Machine Learning Projects/Diabetes Prediction/Deploying Diabetes Prediction/trained_model.sav','rb'))
# loaded_model = pickle.load(open('C:/Users/DELL/Desktop/ML Deployment/Deploying_Diabetes_Prediction/trained_model.sav', 'rb'))

loaded_model = joblib.load(open('C:/Users/DELL/Desktop/ML Deployment/Deploying_Diabetes_Prediction/trained_model.sav', 'rb'))
# creating a funtion for prediction

def diabetes_prediction(input_data):
    
    input_data_numpy = np.asarray(input_data)

    input_data_reshaped = input_data_numpy.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if prediction[0]==0:
        return "Patient is not Diabetic"
    else:
        return "Patient is Diabetic"

def main():
    
    st.title('Diabetes Prediction Web App') #giving a title
    
    st.write("You will need below parameters value")
    
    #getting the input data from the user
    Pregnancies = st.text_input("No of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thicknes Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFuntion = st.text_input("Diabetes Pedigree Funtion")
    Age = st.text_input("Age of the Patient")
    
    #Code for Prediction
    diagnosis = ""
    
    #Creating a button
    if st.button('Am I Diabetic?'):
        diagnosis = diabetes_prediction([Pregnancies,
                                        Glucose,
                                        BloodPressure,
                                        SkinThickness,
                                        Insulin,
                                        BMI,
                                        DiabetesPedigreeFuntion,
                                        Age])
    st.success(diagnosis)
    
    
if __name__ == "__main__":
    main()
    
