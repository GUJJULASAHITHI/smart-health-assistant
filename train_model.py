"""
Model Training & Comparison Script for Smart Health Assistant
Trains and evaluates Decision Tree, Random Forest, and Logistic Regression models.
Selects the best performing model based on balanced F1-score and saves joblib artifacts.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

from preprocessing import prepare_train_test_data

def train_and_compare_models():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(models_dir, exist_ok=True)

    print("Step 1: Preparing preprocessed train/test datasets...")
    X_train, X_test, y_train, y_test, preprocessor, feature_names, X_train_raw, X_test_raw = prepare_train_test_data()

    # Define candidate classifiers
    candidate_models = {
        "Decision Tree": DecisionTreeClassifier(
            criterion="gini",
            max_depth=7,
            min_samples_split=6,
            min_samples_leaf=3,
            random_state=42
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=120,
            max_depth=9,
            min_samples_split=4,
            min_samples_leaf=2,
            random_state=42
        ),
        "Logistic Regression": LogisticRegression(
            solver="lbfgs",
            max_iter=1000,
            C=1.0,
            random_state=42
        )
    }

    results = {}
    fitted_models = {}
    classes = np.unique(y_train)

    print("\nStep 2: Training and evaluating candidate models...")
    for name, model in candidate_models.items():
        print(f"--> Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        prec_macro = precision_score(y_test, y_pred, average="macro", zero_division=0)
        prec_weighted = precision_score(y_test, y_pred, average="weighted", zero_division=0)
        rec_macro = recall_score(y_test, y_pred, average="macro", zero_division=0)
        rec_weighted = recall_score(y_test, y_pred, average="weighted", zero_division=0)
        f1_macro = f1_score(y_test, y_pred, average="macro", zero_division=0)
        f1_weighted = f1_score(y_test, y_pred, average="weighted", zero_division=0)

        results[name] = {
            "accuracy": round(float(acc), 4),
            "precision_macro": round(float(prec_macro), 4),
            "precision_weighted": round(float(prec_weighted), 4),
            "recall_macro": round(float(rec_macro), 4),
            "recall_weighted": round(float(rec_weighted), 4),
            "f1_macro": round(float(f1_macro), 4),
            "f1_weighted": round(float(f1_weighted), 4),
            "classification_report": classification_report(y_test, y_pred, output_dict=True, zero_division=0)
        }
        fitted_models[name] = model

        print(f"    Accuracy: {acc:.4f} | F1 (Macro): {f1_macro:.4f} | F1 (Weighted): {f1_weighted:.4f}")

    # Step 3: Selection based on balanced weighted F1-score and generalization
    best_name = max(results.keys(), key=lambda k: results[k]["f1_weighted"])
    best_model = fitted_models[best_name]
    print(f"\nStep 3: Best Model Selected: [{best_name}] with Weighted F1-Score: {results[best_name]['f1_weighted']:.4f}")

    # Step 4: Save artifacts
    print("\nStep 4: Saving Joblib artifacts and metadata...")
    best_model_path = os.path.join(models_dir, "best_health_model.joblib")
    preprocessor_path = os.path.join(models_dir, "scaler_encoder.joblib")
    all_models_path = os.path.join(models_dir, "all_models.joblib")

    joblib.dump(best_model, best_model_path)
    joblib.dump(preprocessor, preprocessor_path)
    joblib.dump(fitted_models, all_models_path)

    metadata = {
        "best_model_name": best_name,
        "classes": list(classes),
        "feature_names": feature_names,
        "results": results,
        "feature_importances": None
    }

    if hasattr(best_model, "feature_importances_"):
        importances = dict(zip(feature_names, [round(float(x), 4) for x in best_model.feature_importances_]))
        metadata["feature_importances"] = importances

    metadata_path = os.path.join(models_dir, "model_metadata.json")
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    # Step 5: Generate Visualizations
    print("\nStep 5: Generating evaluation plots...")
    generate_comparison_plot(results, os.path.join(models_dir, "model_comparison.png"))
    generate_confusion_matrix_plot(best_model, X_test, y_test, classes, best_name, os.path.join(models_dir, "confusion_matrix.png"))

    print("\nAll training and evaluation steps successfully completed!")
    return results, best_name

def generate_comparison_plot(results, out_path):
    models = list(results.keys())
    metrics = ["accuracy", "precision_weighted", "recall_weighted", "f1_weighted"]
    labels = ["Accuracy", "Precision (W)", "Recall (W)", "F1-Score (W)"]
    
    x = np.arange(len(models))
    width = 0.18

    fig, ax = plt.subplots(figsize=(9, 5))
    colors = ["#2b5c8f", "#38a169", "#d69e2e", "#e53e3e"]

    for i, (m, label) in enumerate(zip(metrics, labels)):
        vals = [results[model][m] for model in models]
        rects = ax.bar(x + (i - 1.5) * width, vals, width, label=label, color=colors[i], alpha=0.9)
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f"{height:.2f}",
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha="center", va="bottom", fontsize=8)

    ax.set_ylabel("Score (0.0 to 1.0)", fontsize=11, fontweight="bold")
    ax.set_title("Model Performance Comparison: Decision Tree vs Random Forest vs Logistic Regression", fontsize=12, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11, fontweight="bold")
    ax.set_ylim(0, 1.15)
    ax.legend(loc="upper right", frameon=True)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()
    print(f"Saved model comparison plot to {out_path}")

def generate_confusion_matrix_plot(model, X_test, y_test, classes, model_name, out_path):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=classes)

    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=[c[:16] + "..." if len(c) > 16 else c for c in classes],
           yticklabels=[c[:16] + "..." if len(c) > 16 else c for c in classes],
           title=f"Confusion Matrix ({model_name})",
           ylabel="True Clinical Health Category",
           xlabel="Predicted Category")

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=9)
    plt.setp(ax.get_yticklabels(), fontsize=9)

    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], "d"),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black",
                    fontweight="bold")

    fig.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()
    print(f"Saved confusion matrix plot to {out_path}")

if __name__ == "__main__":
    train_and_compare_models()
