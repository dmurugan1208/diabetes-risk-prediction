# 🩺 diabetes-risk-prediction

## 🎯 Objective

The objective of this project is to develop an **end-to-end data pipeline and predictive analytics system** that identifies diabetes patients at high risk of hospital readmission.  
By leveraging structured healthcare data, machine learning models, and interactive visualizations, the system aims to:

- Assist healthcare providers in proactively managing patient outcomes  
- Optimize treatment strategies  
- Reduce the likelihood of preventable readmissions  

---

## 📦 Phase 1: Data Collection

- **Source**: UCI Diabetes 130-US hospitals dataset  
- **Files Used**: `patients.csv`, `hospital_visits.csv`, `lab_results.csv`, `medications.csv`  
- **Storage**: Raw files are stored in the `data/` directory

---

## 🧹 Phase 2: Data Cleaning & ETL

- Performed cleaning to fix column names, remove nulls, and ensure consistency  
- Maintained **referential integrity**:
  - `patient_nbr` links `patients` and `hospital_visits`  
  - `encounter_id` (renamed `visit_id` in `hospital_visits`) links to `lab_results` and `medications`  
- Added validation steps to confirm foreign keys exist before loading

---

## 🧱 Schema Design Summary

- `patients(encounter_id, patient_nbr, race, gender, age)`  
- `hospital_visits(visit_id, patient_nbr, admission_type, discharge_disposition, admission_source)`  
- `lab_results(encounter_id, test_name, result_value)`  
- `medications(encounter_id, drug_name, dosage)`

---

## ⚙️ ETL Pipeline Script

- The Python script `etl_pipeline.py` automates:
  - Reading each CSV from `data/`
  - Connecting to the MySQL database
  - Creating and replacing tables using Pandas `to_sql()`
- Output messages confirm success after each load

---

## ✅ Validation Summary

- Ensures:
  - All `patient_nbr` in `hospital_visits` exist in `patients`  
  - All `encounter_id` in `lab_results` and `medications` exist in `hospital_visits`  
- These checks ensure accurate joins and reliable analytics downstream
