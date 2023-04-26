# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:27:57 2023

@author: Analytics
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
 
# Creating FastAPI instance
app = FastAPI()
 
# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    age: int
    private_school: int
    matric_maths: int
    matric_english: int
    urban: int
 
model = joblib.load('lrincomepredictor.sav')
 
# Creating an Endpoint to receive the data
# on which to make a prediction
@app.post('/predict')
def predict(data : request_body):
    # Transforming the data into a form suitable for prediction
    test_data = [[
            data.age,
            data.private_school,
            data.matric_maths,
            data.matric_english,
            data.urban
    ]]
     
    # Predicting the Class
    income_pred = round(model.predict(test_data)[0],0)
     
    # Return the Result
    return { 'prediction' : income_pred}