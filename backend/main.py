from fastapi import FastAPI, UploadFile, File
import pandas as pd 
from analyzer import analyze_flight

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result = analyze_flight(df)
    return result
