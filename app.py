import pandas as pd
from sqlalchemy import create_engine, text
import requests
import time

DB_ID = "admin"
DB_PW = "admin"
DB_HOST = "172.17.0.2"
DB_PORT = "5432"
DB_NAME = "postgres"

test_table_name = "test"
pred_table_name = "predict"

while 1:
    engine = create_engine(f'postgresql://{DB_ID}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    query = f"SELECT * FROM {test_table_name} ORDER BY RANDOM() LIMIT 1;"
    df = pd.read_sql(query, engine)
    
    dat = {"data": df.to_dict(orient="records")}
    response = requests.post(url="https://verbose-fishstick-wrwqjvrxgq6wfg9g4-8000.app.github.dev/predict", json=dat)
    pred = response.json()
    
    with engine.begin() as conn:
        conn.execute(text(f"""
            INSERT INTO {pred_table_name} (id, predict)
            VALUES (:id, :predict)
        """), {"id": int(df['ID'].values[0]), "predict": str(pred['prediction'][0][0])})
    
    engine.dispose()
    print(f"예측값 저장 완료: {pred['prediction'][0][0]}")
    time.sleep(1)
