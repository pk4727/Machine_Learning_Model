import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('Diabetes_prediction_trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_prediction_trained_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model_p.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes_Predection by ML',
                           'Heart_Diseases_Predection by ML',
                           'Parkinsons_Predection by ML'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    

# ----------------------------------------------------------------------------------------------------------------------------------

# creating diabetes_model system
if selected == 'Diabetes_Predection by ML':
    st.title('Diabetes Predection System')

    # input data for diabetes_model form user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies     = st.text_input('Number Of Pregnancies')
    with col2:
        Glucose         = st.text_input('Glucose Level')
    with col3:
        BloodPressure   = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness   = st.text_input('Skin Thickness Value')
    with col2:
        Insulin         = st.text_input('Insulin Level')
    with col3:
        BMI             = st.text_input('Number of BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    with col2:
        Age             = st.text_input('Age Of The Person')

    # create input data
    diab_diagnosis = ''
    # create a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    #  [8,183,64,0,0,23.3,0.672,32] = 1   , [1,89,66,23,94,28.1,0.167,21] = 0     for checking

        if diab_prediction[0] == 0:
            diab_diagnosis = 'Person have NOT Diabetes.'
        elif diab_prediction[0] == 1:
            diab_diagnosis = 'Person have Diabetes.'

    st.success(diab_diagnosis)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# creating Heart Disease_model system
if selected == 'Heart_Diseases_Predection by ML':
    # giving a title for the web
    st.title('Heart Diseases Predection System')
    
    # input data
    col1, col2, col3 = st.columns(3)
    with col1:
        age      = st.text_input('Value of Age')
    with col2:
        sex      = st.text_input('Value of Sex')
    with col3:
        cp       = st.text_input('Value of cp')
    with col1:
        trestbps = st.text_input('Value of trestbps')
    with col2:
        chol     = st.text_input('Value of chol')
    with col3:
        fbs      = st.text_input('Value of fbs')
    with col1:
        restecg  = st.text_input('Value of restecg')
    with col2:
        thalach  = st.text_input('Value of thalach')
    with col3:
        exang    = st.text_input('Value of exang')
    with col1:
        oldpeak  = st.text_input('Value of oldpeak')
    with col2:
        slope    = st.text_input('Value of Slope')
    with col3:
        ca       = st.text_input('Value of ca')
    with col1:
        thal     = st.text_input('Value of thal')

    # for prediction
    heart_result = ''
    # create a button for prediction
    if st.button('Heart_Diseases Test Result'):
        heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg) ,float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal) ]])
        #  [41,1,0,110,172,0,0,158,0,0,2,0,3] = 0    [63,1,3,145,233,1,0,150,0,2.3,0,0,1] = 1  for check
        
        if heart_prediction[0]==0:
            heart_result = ' Person have NOT Heart Diseases.'
        elif heart_prediction[0]==1:     
            heart_result = ' Person have Heart Diseases. '

    st.success(heart_result)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# creating parkinsons_prediction system
if selected == 'Parkinsons_Predection by ML':
    # giving a title for the web
    st.title('Parkinsons Predection System')

    # user input 
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo          = st.text_input('Value of MDVP_Fo(Hz)')
    with col2:
        MDVP_Fhi         = st.text_input('Value of MDVP_Fhi(Hz)')
    with col3:
        MDVP_Flo         = st.text_input('Value of MDVP_Flo(Hz)')
    with col1:
        MDVP_Jitter1      = st.text_input('Value of MDVP_Jitter(%)')
    with col2:
        MDVP_Jitter2      = st.text_input('Value of MDVP_Jitter(Abs)')
    with col3:
        MDVP_RAP         = st.text_input('Value of MDVP_RAP')
    with col1:
        MDVP_PPQ         = st.text_input('Value of MDVP_PPQ')
    with col2:
        Jitter_DDP       = st.text_input('Value of Jitter_DDP')
    with col3:
        MDVP_Shimmer1     = st.text_input('Value of MDVP_Shimmer')
    with col1:
        MDVP_Shimmer2     = st.text_input('Value of MDVP_Shimmer(dB)')
    with col2:
        Shimmer_APQ3     = st.text_input('Value of Shimmer_APQ3')
    with col3:
        Shimmer_APQ5     = st.text_input('Value of Shimmer_APQ5')
    with col1:
        MDVP_APQ         = st.text_input('Value of MDVP_APQ')
    with col2:
        Shimmer_DDA      = st.text_input('Value of Shimmer_DDA')
    with col3:
        NHR              = st.text_input('Value of NHR')
    with col1:
        HNR              = st.text_input('Value of HNR')
    with col2:
        RPDE             = st.text_input('Value of RPDE')
    with col3:
        DFA              = st.text_input('Value of DFA')
    with col1:
        spread1          = st.text_input('Value of spread1')
    with col2:
        spread2          = st.text_input('Value of spread2')
    with col3:
        D2               = st.text_input('Value of D2')
    with col1:
        PPE              = st.text_input('Value of PPE')

    # for prediction
    parkinsons_result = ''
    # create a button for prediction
    if st.button('Parkinsons Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[ MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter1, MDVP_Jitter2, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer1, MDVP_Shimmer2, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE ]])
        #  phon_R01_S01_1 = 1 ,     phon_R01_S07_1 = 0      (checking)
        if (parkinsons_prediction[0] == 1):
            parkinsons_result = "The person has Parkinson's disease"
        else:
            parkinsons_result = "The person does not have Parkinson's disease"

    st.success(parkinsons_result)
