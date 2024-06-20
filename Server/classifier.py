from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import joblib
import os
import pandas as pd

class Issue(BaseModel):
    id: int
    state: str
    title: str
    body: str

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RUN_ID = '0579ea92a6c7494e9bfdf42813fe3867'
MODEL_NAME = 'nn'
EXPERIMENT_NAME = '2'
MODEL_URI = os.path.join('..', 'Models', 'mlartifacts', EXPERIMENT_NAME, RUN_ID, 'artifacts', MODEL_NAME, 'model.pkl')
binary_classifier = joblib.load(MODEL_URI)


def classify_texts(texts: List[str]) -> List[str]:
    predictions = binary_classifier.predict(texts)
    return predictions

@app.post("/classify_spam")
def classify_spam(issues: List[Dict]):
    df = pd.DataFrame([issue for issue in issues])
    df['concatenated_text'] = df['title'] + ' ' + df['body']
    df['label'] = classify_texts(df['concatenated_text'].tolist())
    
    results = df[['id', 'label']].to_dict(orient='records')
    return results
    #return [{"id": 1, "label": "spam"}]

# uvicorn classifier:app --reload --port 8080