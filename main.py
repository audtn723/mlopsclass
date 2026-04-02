import os
import pickle
import json
import pandas as pd
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("config.json", "r") as f:
    config = json.load(f)

class Dataset(BaseModel):
    data: List

app = FastAPI()

@app.post("/predict")
def get_prediction(dataset: Dataset):
    xcols = config['xcols']
    data = pd.DataFrame(dict(dataset)["data"])[xcols]
    prediction = model.predict(data).tolist()
    log_proba = model.predict_proba(data).tolist()
    return {"prediction": prediction, "log_proba": log_proba}