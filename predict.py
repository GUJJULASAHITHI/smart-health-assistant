"""
Inference & Prediction Pipeline for Smart Health Assistant
Loads trained models, performs feature engineering on user input,
and calculates prediction probabilities and uncertainty metrics.
"""

import os
import joblib
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

class HealthPredictor:
    def __init__(self, model_name=None):
        self.best_model_path = os.path.join(MODELS_DIR, "best_health_model.joblib")
        self.preprocessor_path = os.path.join(MODELS_DIR, "scaler_encoder.joblib")
        self.all_models_path = os.path.join(MODELS_DIR, "all_models.joblib")

        if not os.path.exists(self.best_model_path) or not os.path.exists(self.preprocessor_path):
            raise FileNotFoundError("Trained model artifacts missing. Run train_model.py first.")

        self.preprocessor = joblib.load(self.preprocessor_path)
        
        if os.path.exists(self.all_models_path):
            self.all_models = joblib.load(self.all_models_path)
        else:
            self.all_models = {}

        if model_name and model_name in self.all_models:
            self.model = self.all_models[model_name]
            self.current_model_name = model_name
        else:
            self.model = joblib.load(self.best_model_path)
            self.current_model_name = "Random Forest (Default Best)"

    def predict(self, user_input: dict):
        """
        Accepts a dictionary of symptom inputs:
        user_input example: {
            "fever": 1, "cough": 0, "headache": 1, "loose_stools": 0,
            "vomiting": 0, "mild_stomach_pain": 0, "weakness_fatigue": 1,
            "dehydration_signs": 0, "loss_of_appetite": 1, "body_ache": 1,
            "chills": 1, "symptom_duration_days": 2,
            "age_group": "Young Adult (18-35)", "severity_score": 3
        }
        """
        from preprocessing import NUMERIC_FEATURES, CATEGORICAL_FEATURES, BINARY_FEATURES
        feature_cols = NUMERIC_FEATURES + CATEGORICAL_FEATURES + BINARY_FEATURES

        # Ensure all columns present
        row = {}
        for col in feature_cols:
            row[col] = [user_input.get(col, 0)]

        df_input = pd.DataFrame(row)
        X_proc = self.preprocessor.transform(df_input)

        predicted_class = self.model.predict(X_proc)[0]

        # Probabilities
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(X_proc)[0]
            classes = self.model.classes_
            prob_dict = {cls: round(float(p) * 100, 2) for cls, p in zip(classes, probs)}
            sorted_probs = sorted(prob_dict.items(), key=lambda x: x[1], reverse=True)
            top_prob = sorted_probs[0][1]
            second_prob = sorted_probs[1][1] if len(sorted_probs) > 1 else 0.0

            # Uncertainty calculation
            margin = top_prob - second_prob
            if top_prob >= 70.0 and margin >= 25.0:
                uncertainty_level = "Low"
                uncertainty_explanation = "Distinct, well-delineated symptom constellation."
            elif top_prob >= 45.0:
                uncertainty_level = "Moderate"
                uncertainty_explanation = "Moderate symptom overlap with secondary conditions."
            else:
                uncertainty_level = "High"
                uncertainty_explanation = "Significant overlap; symptoms present in multiple categories."
        else:
            sorted_probs = [(predicted_class, 100.0)]
            top_prob = 100.0
            uncertainty_level = "Not applicable"
            uncertainty_explanation = "Deterministic decision rule."

        # Active symptoms list
        active_symptoms = [k.replace("_", " ").title() for k, v in user_input.items() if v == 1 and k in BINARY_FEATURES]

        return {
            "predicted_category": predicted_class,
            "confidence_pct": top_prob,
            "uncertainty_level": uncertainty_level,
            "uncertainty_explanation": uncertainty_explanation,
            "sorted_probabilities": sorted_probs,
            "active_symptoms": active_symptoms,
            "model_used": self.current_model_name,
            "duration_days": user_input.get("symptom_duration_days", 1),
            "age_group": user_input.get("age_group", "Unknown"),
            "severity_score": user_input.get("severity_score", 1),
            "disclaimer": (
                "EDUCATIONAL DISCLAIMER: This machine learning prediction is generated for health education "
                "and triage awareness. It is NOT a clinical diagnosis and does not prescribe medicine. "
                "If severe red flags are present, consult a licensed healthcare practitioner immediately."
            )
        }

if __name__ == "__main__":
    predictor = HealthPredictor()
    test_input = {
        "fever": 1,
        "cough": 0,
        "headache": 1,
        "loose_stools": 0,
        "vomiting": 0,
        "mild_stomach_pain": 0,
        "weakness_fatigue": 1,
        "dehydration_signs": 0,
        "loss_of_appetite": 1,
        "body_ache": 1,
        "chills": 1,
        "symptom_duration_days": 2,
        "age_group": "Young Adult (18-35)",
        "severity_score": 3
    }
    result = predictor.predict(test_input)
    print("Inference Test Output:")
    print("Predicted Category:", result["predicted_category"])
    print("Confidence:", f"{result['confidence_pct']}%")
    print("Uncertainty Level:", result["uncertainty_level"])
    print("Probabilities:", result["sorted_probabilities"][:3])
