from sqlalchemy import create_engine
import pandas as pd
import os

# Encode @ in password as %40
db_user = "root"
db_password = "Durgamegala%40123"  # <- '@' replaced with '%40'
db_host = "localhost"
db_port = "3306"
db_name = "diabetes_db"

data_dir = "C:/Users/Durga Vishalini/diabetes-risk-prediction/data"
tables = {
    "patients": "patients.csv",
    "hospital_visits": "hospital_visits.csv",
    "lab_results": "lab_results.csv",
    "medications": "medications.csv"
}

engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

for table_name, filename in tables.items():
    csv_path = os.path.join(data_dir, filename)
    print(f"📥 Loading {table_name} from {csv_path}...")
    df = pd.read_csv(csv_path)
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print(f"✅ Loaded {table_name} into MySQL!")

print("🚀 All tables successfully loaded!")
