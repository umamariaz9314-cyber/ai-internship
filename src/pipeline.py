"""
End-to-end training script for the Titanic survival model.
Run from the command line: python src/pipeline.py
"""
import sys
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

sys.path.append(os.path.dirname(__file__))
from features import engineer_features
from models import build_full_pipeline


def main():
    # Load raw data
    raw_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'titanic.csv')
    df = pd.read_csv(raw_path)

    # Feature engineering
    df = engineer_features(df)

    X = df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'])
    y = df['Survived']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Build and train pipeline
    pipeline = build_full_pipeline()
    pipeline.fit(X_train, y_train)

    test_score = pipeline.score(X_test, y_test)
    print(f"Test accuracy: {test_score:.4f}")

    # Save pipeline
    output_path = os.path.join(os.path.dirname(__file__), '..', 'experiments', 'titanic_pipeline.joblib')
    joblib.dump(pipeline, output_path)
    print(f"Pipeline saved to {output_path}")


if __name__ == '__main__':
    main()