import pandas as pd
from connectSql import get_mysql_engine

dataFrame = pd.read_csv('Overløp (Alarm)-data-90_dagar.csv')

print(dataFrame.head())

engine = get_mysql_engine()

try:
    dataFrame.to_sql('Overløp_90d', con=engine, if_exists='replace', index=False)
    print("Data uploaded successfully!")
except Exception as e:
    print(f"An error occurred while uploading data: {e}")

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")