"""
Model Evaluation Script
Loads saved model and metadata, prints detailed evaluation metrics, classification reports,
and generates performance tables for academic reporting.
"""

import os
import json
import joblib
import pandas as pd
from sklearn.metrics import classification_report

from preprocessing import prepare_train_test_data

def evaluate_saved_models():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, "models")
    
    metadata_path = os.path.join(models_dir, "model_metadata.json")
    if not os.path.exists(metadata_path):
        print("Metadata not found. Please run train_model.py first.")
        return

    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    print("=" * 60)
    print("        SMART HEALTH ASSISTANT - MODEL EVALUATION REPORT")
    print("=" * 60)
    print(f"Best Selected Model: {meta['best_model_name']}")
    print(f"Number of Target Classes: {len(meta['classes'])}")
    print(f"Engineered Feature Count: {len(meta['feature_names'])}")
    print("\nModel Comparison Summary Table:")
    print("-" * 60)
    
    rows = []
    for model_name, metrics in meta["results"].items():
        rows.append({
            "Model": model_name,
            "Accuracy": f"{metrics['accuracy']:.4f}",
            "Precision (W)": f"{metrics['precision_weighted']:.4f}",
            "Recall (W)": f"{metrics['recall_weighted']:.4f}",
            "F1-Score (W)": f"{metrics['f1_weighted']:.4f}",
            "F1-Score (Macro)": f"{metrics['f1_macro']:.4f}"
        })
    df_metrics = pd.DataFrame(rows)
    print(df_metrics.to_string(index=False))

    if meta.get("feature_importances"):
        print("\nTop 7 Most Important Features (Random Forest):")
        print("-" * 60)
        sorted_fi = sorted(meta["feature_importances"].items(), key=lambda x: x[1], reverse=True)[:7]
        for rank, (feat, imp) in enumerate(sorted_fi, 1):
            print(f" {rank}. {feat:<28} : {imp * 100:.2f}%")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    evaluate_saved_models()
