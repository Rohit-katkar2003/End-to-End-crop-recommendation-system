import streamlit as st
import pickle
from PIL import Image
import pandas as pd
st.set_page_config(layout='wide' , page_title='Crop Recommender' ,page_icon='🌳')

pickle_file = "pickle_model/app.sav"
load_model = pickle.load(open(pickle_file,'rb'))

class_name = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

def make_prediction(input_data, model, class_name=class_name):
    pred = model.predict([input_data])
    op = class_name[pred[0] - 1]
    if op == 'coffee':
        desc = st.success("the predicted crop is " + str(op) )
        im = st.image('Images/coffee.jpg')
        return desc , im
    elif op =='rice':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/rice.jpg')
        return desc, im
    elif op =='maize':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/maize.jpg')
        return desc, im
    elif op == 'chickpea':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/chickpea.jpg')
        return desc, im
    elif op == 'kidneybeans':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/kidneybeans.jpg')
        return desc, im
    elif op =='pigeonpeas':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/pigeonpeas.jpg')
        return desc, im
    elif op =='mothbeans':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/mothbeans.jpg')
        return desc, im
    elif op == 'mungbean':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/mungbean.jpg')
        return desc, im
    elif op == 'blackgram':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/blackgram.jpg')
        return desc, im
    elif op =='lentil':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/lentil.jpg')
        return desc, im
    elif op =='pomegranate':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/pomegranate.jpg')
        return desc, im
    elif op == 'banana':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/banana.jpg')
        return desc, im
    elif op == 'mango':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/mango.jpg')
        return desc, im
    elif op == 'grapes':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/grapes.jpg')
        return desc, im
    elif op =='watermelon':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/watermelon.jpg')
        return desc, im
    elif op =='muskmelon':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/muskmelon.jpg')
        return desc, im
    elif op == 'apple':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/apple.jpg')
        return desc, im
    elif op == 'orange':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/orange.jpg')
        return desc, im
    elif op =='papaya':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/papaya.jpg')
        return desc, im
    elif op =='coconut':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/coconut.jpg')
        return desc, im
    elif op =='cotton':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/cotton.jpg')
        return desc, im
    elif op =='jute':
        desc = st.success("the predicted crop is " + str(op))
        im = st.image('Images/jute.jpg')
        return desc, im


st.markdown(
    """
    <style>
    .stButton button {
        width: 200px;
        height: 50px;
        font-size: 20px;
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Crop Recommendation System')
tab1 , tab2 = st.tabs(['crop recomendor' , 'project Description'])

with tab1:
    col1, col2, col3 = st.columns([3, 3, 3])
    col4 , col5 , col6  =st.columns([3,3,3])
    _, col7, _ = st.columns([3, 3, 3])
    _ , bt1 , _ = st.columns([3,3,3])

    with col1:
        nitrogen = st.number_input(label='Enter Nitrogen content in soil' ,value=80.90 , min_value=0.0 ,
                                   max_value=140.0,help='plz nitrogen of your soil')
    with col2:
        phosphorous = st.number_input(label='Enter phosporous content in soil' ,value=40.0 , max_value=145.0 ,
                                      min_value=5.0 ,  help='plz phosphorous of your soil')
    with col3:
        potassium = st.number_input(label='Enter potassium content in soil', value=69.90,
                                    max_value=205.0, min_value=5.0 , help='plz potassium of your soil')

    with col4:
        tempreture = st.number_input(label='Enter current Tempreture(in degree/celsius)' , value=34.0 ,
                                     max_value=48.0 , min_value=8.0,help='plz enter tempreture ')

    with col5:
        humidity = st.number_input(label='Enter current humidity(in percentage)', value=34.0, max_value=100.0,min_value=14.0)
    with col6:
        ph = st.number_input(label='Enter current ph level of soil', value=6.0, max_value=10.0, min_value=2.0)

    with col7:
        rainfall =st.number_input(label='Enter rainfall in area ', value=150.0, max_value=300.0, min_value=20.0)
    with bt1:
        if st.button('submit'):
            input_data1 = [nitrogen , phosphorous, potassium ,tempreture,humidity,ph,rainfall]
            make_prediction(input_data=input_data1 ,model=load_model )

with tab2:
    with st.expander('See Explanation'):
        st.markdown(''' ## Project Description: Predicting Optimal Crops for Soil Conditions
### Introduction
- Agriculture is a crucial part of the global economy and the primary source of livelihood for many communities. The success of agricultural practices heavily depends on understanding and optimizing soil conditions to grow the best possible crops. This project aims to leverage data-driven approaches to predict the optimal crop for a given set of soil and environmental conditions. By analyzing key soil and climate features, we aim to assist farmers and agricultural experts in making informed decisions to enhance crop yield and sustainability.
''')
        st.image('Images/pexels-flambo-388007-1112080.jpg')

        st.markdown('''### Objective
         
The main objective of this project is to build a predictive model that identifies the most suitable crop for a given soil sample based on the following features:

- Nitrogen (N): Essential for plant growth and development, nitrogen is a major component of chlorophyll and amino acids.
- Phosphorous (P): Crucial for energy transfer and photosynthesis, phosphorous plays a significant role in root development and crop maturity.
- Potassium (K): Helps in water regulation, enzyme activation, and photosynthesis, potassium is vital for plant health.
- Temperature (°C): The ambient temperature affects seed germination, plant growth, and crop yield.
- Humidity (%): Moisture in the air influences transpiration rates and overall plant health.
- pH Level: Soil pH affects nutrient availability and microbial activity in the soil.
- Rainfall (mm): Adequate water supply is critical for crop growth, affecting both soil moisture and nutrient uptake.

### Methodology
#### Data Collection:
- Gather data on various crops and their corresponding soil and environmental conditions.
- Data sources may include agricultural databases, research papers, and field surveys.

#### Data Preprocessing:
- Clean and preprocess the data to handle missing values, outliers, and inconsistencies.
- Normalize or standardize the features as required.

#### Feature Engineering:
- Create additional features if needed, such as soil texture, organic matter content, or elevation.

#### Model Training:
- Split the data into training and testing sets.
- Train various machine learning models (e.g., Decision Trees, Random Forests, Gradient Boosting) to predict the optimal crop based on the input features.
- Incorporate monotonic constraints to ensure model predictions align with agronomic principles.

#### Model Evaluation:
- Evaluate model performance using metrics such as accuracy, precision, recall, and F1-score.
- Perform cross-validation to ensure the model's robustness.

#### Model Interpretation and Deployment:
- Interpret the model to understand feature importance and decision rules.
- Deploy the model as a web application using Streamlit, allowing users to input soil and environmental conditions and receive crop recommendations.

### Tools and Technologies
1) Python: Programming language for data analysis and model building.
2) scikit-learn: Machine learning library for model training and evaluation.
3) Random Forest : random forest is powerful algorithm.
4) Pandas: Data manipulation and analysis library.
5) NumPy: Numerical computing library.
6) Matplotlib/Plotly: Visualization libraries for plotting decision trees and feature importance.
7) Streamlit: Framework to deploy the predictive model as an interactive web application.

### Expected Outcomes
By the end of this project, we expect to have a robust predictive model that:

- Accurately predicts the optimal crop for a given set of soil and environmental conditions.
- Provides insights into how different soil properties and climate factors influence crop suitability.
- Offers an easy-to-use web interface for farmers and agricultural experts to make data-driven decisions.


### Impact
This project has the potential to:

- Enhance crop yield and quality by recommending the best-suited crops for specific soil conditions.
- Promote sustainable agricultural practices by optimizing resource use.
- Support farmers in making informed decisions, thereby improving their livelihood and contributing to food security.

            ''')





