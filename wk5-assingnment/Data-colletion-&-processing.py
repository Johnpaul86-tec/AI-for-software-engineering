# ===== Quiz 2: Data Collection & Preprocessing =====
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# --- 1. Load datasets (EHR + demographics) ---
ehr_data = pd.read_csv("ehr_data.csv")          # structured EHR fields
demographics = pd.read_csv("demographics.csv")  # age, sex, ZIP code, etc.

# --- 2. Merge datasets on patient ID ---
data = pd.merge(ehr_data, demographics, on="patient_id", how="left")

# --- 3. Handle missing values ---
# For numerical features: median imputation
num_cols = data.select_dtypes(include=np.number).columns
num_imputer = SimpleImputer(strategy='median')
data[num_cols] = num_imputer.fit_transform(data[num_cols])

# For categorical features: fill missing with 'Unknown'
cat_cols = data.select_dtypes(include='object').columns
data[cat_cols] = data[cat_cols].fillna('Unknown')

# --- 4. Feature engineering ---
# Example: comorbidity index (simplified sum of diagnosis codes)
data['comorbidity_index'] = data[['diagnosis_1', 'diagnosis_2', 'diagnosis_3']].notnull().sum(axis=1)

# Prior hospital visits
data['prior_admissions'] = data.groupby('patient_id')['admission_date'].transform('count')

# Medication count
med_cols = ['med_1', 'med_2', 'med_3']
data['med_count'] = data[med_cols].notnull().sum(axis=1)

# --- 5. Encoding categorical features ---
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded_cat = encoder.fit_transform(data[cat_cols])
encoded_cat_df = pd.DataFrame(encoded_cat, columns=encoder.get_feature_names_out(cat_cols))
data = pd.concat([data.drop(columns=cat_cols), encoded_cat_df], axis=1)

# --- 6. Scaling numerical features ---
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

print("Preprocessed dataset shape:", data.shape)
