# Flight-Data-Analysis-Visualization-Platform
A platform that reads flight data, detects anomalies (unsafe events), visualize flight paths and metrics and generates a safety report.

Everytime before using the app: 

<!-- cd backend
source venv/bin/activate
python -m pip install ...
python main.py -->
source venv/bin/activate
python -m uvicorn main:app --reload