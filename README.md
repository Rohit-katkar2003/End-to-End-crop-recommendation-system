# Crop Recommendation System

## Overview

The Crop Recommendation System is a machine learning project designed to predict the most suitable crop to cultivate based on soil and environmental conditions. The system uses various features such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall to provide accurate recommendations.

## Features

- Predict the best crop for given soil and environmental conditions
- User-friendly interface for inputting data and viewing recommendations
- Supports multiple crops and diverse geographical regions

## Project Structure

├── .gitignore

├── .idea/

├── Crop_recommendation.csv

├── Images/

├── app.sav

├── crop.py

├── crop_recommendation.ipynb

├── requirements.txt

├── venv/

└── README.md


- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.idea/**: Contains project-specific settings and configurations for your IDE.
- **Crop_recommendation.csv**: The dataset used for training and testing the model.
- **Images/**: Directory for storing images related to the project.
- **app.sav**: The saved machine learning model.
- **crop.py**: The main script for running the crop recommendation system.
- **crop_recommendation.ipynb**: Jupyter Notebook containing the project workflow and model training process.
- **requirements.txt**: Lists the dependencies required to run the project.
- **venv/**: The virtual environment directory.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Rohit-katkar2003/crop-recommendation-system.git
    cd crop-recommendation-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the crop recommendation script:**
    ```bash
    python crop.py
    ```

2. **Interact with the system:**
   - Input the required features (nitrogen, phosphorus, potassium, temperature, humidity, pH, rainfall).
   - Get the recommended crop based on the input features.

## Dataset

The dataset (`Crop_recommendation.csv`) contains various features required for predicting the suitable crop. Each row represents a data point with the following columns:

- **N**: Nitrogen content in the soil
- **P**: Phosphorus content in the soil
- **K**: Potassium content in the soil
- **temperature**: Temperature of the environment
- **humidity**: Humidity of the environment
- **ph**: pH level of the soil
- **rainfall**: Rainfall amount
- **label**: Crop type (target variable)

## Model

The machine learning model used in this project is saved in `app.sav`. The model is trained using a combination of various algorithms to ensure high accuracy in crop prediction.



## Streamlit app demo: 
![image](https://github.com/user-attachments/assets/d7f9533d-cb86-4fe4-8791-01555c389163)


## Contact

For any questions or suggestions, please contact [katkarrohit203@gmail.com].




