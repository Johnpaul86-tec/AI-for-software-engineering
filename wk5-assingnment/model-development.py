# ===== Quiz 3: Model Development =====
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# --- 1. Load preprocessed data ---
# Assuming 'data' from Quiz 2 and label column 'readmission_30d' exists
X = data.drop(columns=['patient_id', 'readmission_30d'])
y = data['readmission_30d']

# --- 2. Split data into train/validation/test sets ---
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

# --- 3. Define and train the model ---
model = XGBClassifier(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric='logloss',
    use_label_encoder=False
)

model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=50,
    verbose=True
)

# --- 4. Predict on test set ---
y_pred = model.predict(X_test)

# --- 5. Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# --- 6. Precision, Recall, F1-score ---
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Optional: feature importance
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
xgb_importances = model.feature_importances_
plt.barh(X.columns, xgb_importances)
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.title("XGBoost Feature Importance")
plt.show()
