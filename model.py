import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# -----------------------------
# Chargement des données
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, "covid19_data.csv"))

# -----------------------------
# Prétraitement (IDENTIQUE À TON CODE)
# -----------------------------
df["COVID_POSITIVE"] = df["CLASIFFICATION_FINAL"].apply(
    lambda x: 1 if x in [1, 2, 3] else 2
)
df = df[df["COVID_POSITIVE"] == 1]

cols = df.columns.drop("AGE")
df[cols] = df[cols].replace([97, 98, 99], np.nan)

df["DATE_DIED"] = df["DATE_DIED"].replace("9999-99-99", pd.NA)
df["DEATH"] = df["DATE_DIED"].notna().map({True: 1, False: 2})
df.drop(columns=["DATE_DIED"], inplace=True)

df.loc[df["SEX"] == 2, "PREGNANT"] = 2
df["PREGNANT"] = df["PREGNANT"].fillna(2)

# -----------------------------
# Imputation des valeurs manquantes
# -----------------------------

# Colonnes binaires
colonne_binaire = [
    "DIABETES", "COPD", "ASTHMA", "INMSUPR",
    "HIPERTENSION", "OTHER_DISEASE", "CARDIOVASCULAR",
    "OBESITY", "RENAL_CHRONIC", "TOBACCO"
]

# Imputation des colonnes binaires avec le mode
df[colonne_binaire] = df[colonne_binaire].fillna(df.mode().iloc[0])

# Imputation de l'âge avec la médiane
df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
df["AGE"] = df["AGE"].fillna(df["AGE"].median())

# Groupes d'âge
df["AGE_GROUP"] = pd.cut(
    df["AGE"],
    bins=[0, 12, 18, 35, 55, 120],
    labels=[1, 2, 3, 4, 5],
    include_lowest=True
)

# Imputation de la pneumonie avec le mode
df["PNEUMONIA"] = df["PNEUMONIA"].fillna(df["PNEUMONIA"].mode()[0])

# ICU
icu_vars = [
    "AGE_GROUP", "SEX", "PREGNANT", "PNEUMONIA", "DIABETES",
    "CARDIOVASCULAR", "OBESITY",
    "RENAL_CHRONIC", "INMSUPR",
    "OTHER_DISEASE", "INTUBED"
]

df["ICU"] = df.groupby(icu_vars)["ICU"].transform(
    lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 2)
)

# INTUBED
intubed_var = [
    "AGE_GROUP", "SEX", "PREGNANT", "PNEUMONIA", "DIABETES",
    "HIPERTENSION", "CARDIOVASCULAR", "OBESITY",
    "RENAL_CHRONIC", "COPD", "INMSUPR",
    "OTHER_DISEASE", "TOBACCO" , 
]

df["INTUBED"] = df.groupby(intubed_var)["INTUBED"].transform(
    lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 2)
)

# Imputation de toutes les autres colonnes restantes
df[colonne_binaire] = df[colonne_binaire].fillna(df.mode().iloc[0])

# Suppression des doublons
df.drop_duplicates(inplace=True)

# -----------------------------
# HAUT_RISQUE (LOGIQUE MÉTIER)
# -----------------------------
df["HAUT_RISQUE"] = np.where(
    (df["INTUBED"] == 1) | (df["DEATH"] == 1) | (df["ICU"] == 1),
    1,
    2
)

# -----------------------------
# Features
# -----------------------------
features = [
    "AGE_GROUP", "SEX", "PREGNANT", "PNEUMONIA", "DIABETES",
    "HIPERTENSION", "CARDIOVASCULAR", "OBESITY",
    "RENAL_CHRONIC", "COPD", "ASTHMA", "INMSUPR",
    "OTHER_DISEASE", "TOBACCO"
]

X = df[features]
y = df["HAUT_RISQUE"]

# -----------------------------
# Vérification des NaN avant le split
# -----------------------------
print(f"Nombre de NaN dans les features : \n{X.isna().sum()}")

# -----------------------------
# Split des données en train/test
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# -----------------------------
# Standardisation des données
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# -----------------------------
# Modèle FINAL
# -----------------------------
model = LinearSVC(
    C=0.1,
    class_weight={1: 3, 2: 1},
    max_iter=10000,
    random_state=42
)

# Entraînement du modèle
model.fit(X_train_scaled, y_train)

# -----------------------------
# Sauvegarde
# -----------------------------
joblib.dump(model, "svm_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Modèle entraîné")
