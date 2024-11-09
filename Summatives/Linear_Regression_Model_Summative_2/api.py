from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np 


model = joblib.load('heart_disease_model.joblib')
app = FastAPI()
class PredictionRequest(BaseModel):
    HighBP: int
    BMI: float
    Smoker: int
    Sex: int

@app.post('/predict')
def predict(data: PredictionRequest):
    
    input_data = np.array([[data.HighBP, data.BMI, data.Smoker, data.Sex]])
    # Get continuous prediction 
    y_pred_continuous = model.predict(input_data)[0]
    threshold = 0.5
    y_pred_binary = 1 if y_pred_continuous >= threshold else 0
    
    
    return {'heart_disease_risk': y_pred_binary}
