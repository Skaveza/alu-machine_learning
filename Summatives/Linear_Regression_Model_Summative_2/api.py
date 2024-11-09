from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np 

model = joblib.load('heart_disease_model.joblib')
app = FastAPI

class PredictionRequest(BaseModel):
  HighBP:int
  BMI:float
  Smoker:int
  Sex:int