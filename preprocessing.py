"""
Data Preprocessing Pipeline for Health Classification
Handles data loading, missing value imputation, encoding, and train-test splitting.
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

BINARY_FEATURES = [
    "fever",
    "cough",
    "headache",
    "loose_stools",
    "vomiting",
    "mild_stomach_pain",
    "weakness_fatigue",
    "dehydration_signs",
    "loss_of_appetite",
    "body_ache",
    "chills"
]

NUMERIC_FEATURES = [
    "symptom_duration_days",
    "severity_score"
]

CATEGORICAL_FEATURES = [
    "age_group"
]

TARGET_COLUMN = "health_category"

def load_data(file_path=None):
    """Load raw dataset from disk."""
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "data", "health_concerns_data.csv")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}. Please run generate_dataset.py first.")
        
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """Clean and impute any missing values in raw dataframe."""
    df_clean = df.copy()

    # Impute numeric features with median
    for col in NUMERIC_FEATURES:
        if col in df_clean.columns and df_clean[col].isnull().any():
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)

    # Impute categorical features with mode
    for col in CATEGORICAL_FEATURES:
        if col in df_clean.columns and df_clean[col].isnull().any():
            mode_val = df_clean[col].mode()[0]
            df_clean[col] = df_clean[col].fillna(mode_val)

    # Ensure binary features are integer 0 or 1
    for col in BINARY_FEATURES:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna(0).astype(int)

    return df_clean

def build_preprocessor():
    """
    Constructs a ColumnTransformer to handle binary, numeric, and categorical features.
    """
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUMERIC_FEATURES),
            ("cat", categorical_transformer, CATEGORICAL_FEATURES),
            ("bin", "passthrough", BINARY_FEATURES)
        ],
        remainder="drop"
    )
    return preprocessor

def prepare_train_test_data(test_size=0.20, random_state=42):
    """
    Loads, cleans, splits, and fits the preprocessor.
    Returns: X_train_proc, X_test_proc, y_train, y_test, preprocessor, feature_names
    """
    df = load_data()
    df_clean = clean_data(df)

    feature_cols = NUMERIC_FEATURES + CATEGORICAL_FEATURES + BINARY_FEATURES
    X = df_clean[feature_cols]
    y = df_clean[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    preprocessor = build_preprocessor()
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc = preprocessor.transform(X_test)

    # Retrieve feature names after one-hot encoding
    cat_encoder = preprocessor.named_transformers_["cat"].named_steps["encoder"]
    cat_feature_names = list(cat_encoder.get_feature_names_out(CATEGORICAL_FEATURES))
    feature_names = NUMERIC_FEATURES + cat_feature_names + BINARY_FEATURES

    return X_train_proc, X_test_proc, y_train, y_test, preprocessor, feature_names, X_train, X_test

if __name__ == "__main__":
    X_train_p, X_test_p, y_train, y_test, prep, feat_names, _, _ = prepare_train_test_data()
    print("Preprocessing completed successfully!")
    print(f"X_train shape: {X_train_p.shape}, X_test shape: {X_test_p.shape}")
    print(f"Total features after encoding: {len(feat_names)}")
    print("Engineered feature names:", feat_names)
