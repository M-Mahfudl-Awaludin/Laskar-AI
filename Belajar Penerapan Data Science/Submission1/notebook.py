# -*- coding: utf-8 -*-
"""notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1saZz5Nu-FvVDk5HVx7fgoeZ3tpOhxES3

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

- Nama: M Mahfudl Awaludin
- Email:mahfudlawaludin.26@gmail.com

## Persiapan

### Menyiapkan library yang dibutuhkan
"""

# Import library yang dibutuhkan
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

"""### Menyiapkan data yang akan diguankan

## Data Understanding
"""

# Baca dataset
df = pd.read_csv("/content/employee_data (1).csv")  # Ganti dengan path lokal jika beda

# Lihat struktur data
print(df.info())

# Deskripsi statistik
print(df.describe())

# Cek nilai kosong
print(df.isnull().sum())

"""## Data Preparation / Preprocessing"""

# Hapus baris dengan nilai kosong di kolom target
df = df.dropna(subset=["Attrition"])

# Ubah tipe target jadi integer
df["Attrition"] = df["Attrition"].astype(int)

# Label Encoding kolom kategorikal
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# Pisahkan fitur dan target
X = df.drop(columns=["EmployeeId", "Attrition"])
y = df["Attrition"]

# Standardisasi fitur
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)



"""## Modeling"""

# Inisiasi model Random Forest
model = RandomForestClassifier(random_state=42)

# Training model
model.fit(X_train, y_train)

"""## Evaluation"""

# Prediksi
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print(classification_report(y_test, y_pred))

# Cek pentingnya fitur
importances = model.feature_importances_
feature_names = X.columns
feat_imp = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

# Visualisasi Top 10
plt.figure(figsize=(8, 5))
sns.barplot(x="Importance", y="Feature", data=feat_imp.head(10))
plt.title("Top 10 Important Features")
plt.show()

import joblib
# 4. Simpan model dan scaler
joblib.dump(model, "model_attrition.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model dan scaler berhasil disimpan!")

import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("/content/model_attrition.pkl")
scaler = joblib.load("/content/scaler.pkl")

# Get the feature names the scaler was trained on
feature_names = scaler.get_feature_names_out() # Get the feature names the scaler was trained with

# Contoh data karyawan baru (bisa dari input user atau file)
# Angka ini harus sesuai urutan dan jumlah kolom seperti pada X saat training
data_baru = pd.DataFrame([[
    32,     # Age
    3,      # BusinessTravel
    2,      # DailyRate
    1,      # Department
    0,      # DistanceFromHome
    2,      # Education
    3,      # EducationField
    2,      # EnvironmentSatisfaction
    1,      # Gender
    5,      # JobLevel
    5000,   # MonthlyIncome
    3,      # JobSatisfaction
    0,      # MaritalStatus
    5,      # NumCompaniesWorked
    3,      # OverTime
    10      # TotalWorkingYears
    # Tambahkan fitur lainnya sesuai dataset kamu - Make sure to include all 33 features
]], columns=[
    'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender',
    'JobLevel', 'MonthlyIncome', 'JobSatisfaction', 'MaritalStatus',
    'NumCompaniesWorked', 'OverTime', 'TotalWorkingYears'
    # Tambahkan nama fitur lainnya jika ada - Add the remaining feature names here
])


# Reindex data_baru to include all features, filling missing ones with 0
data_baru = data_baru.reindex(columns=feature_names, fill_value=0)


# Normalisasi
data_baru_scaled = scaler.transform(data_baru)

# Prediksi
prediksi = model.predict(data_baru_scaled)
hasil = "Akan Resign" if prediksi[0] == 1 else "Tidak Resign"

print(f"Hasil Prediksi: {hasil}")

df.to_csv("employee_cleaned_data.csv", index=False)

!pip freeze > requirements.txt