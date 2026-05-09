import pandas as pd

def analyze_flight(df: pd.DataFrame):
    events = []

    df['altitude'] = pd.to_numeric(df['altitude'], errors='coerce')
    df['speed'] = pd.to_numeric(df['speed'], errors='coerce')
    df['pitch'] = pd.to_numeric(df['pitch'], errors='coerce')

    df = df.dropna()

    df['altitude_diff'] = df['altitude'].diff()

    for _, row in df[df['speed'] > 480].iterrows():
        events.append({
            "type": "Overspeed",
            "time": row['time']
        })

    for _, row in df[df['pitch'].abs() > 10].iterrows():
        events.append({
            "type": "Unstable Pitch",
            "time": row['time']
        })

    return {
        "events": events,
        "total_events": len(events)
    }            