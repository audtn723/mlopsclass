import pandas as pd
from sqlalchemy import create_engine

def db_to_df(DB_HOST, DB_NAME, table_name):
    DB_ID = "admin"
    DB_PW = "admin"
    DB_PORT = "5432"
    engine = create_engine(f'postgresql://{DB_ID}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    query = f"SELECT * FROM {table_name}"
    result = pd.read_sql(query, engine)
    engine.dispose()
    return result
