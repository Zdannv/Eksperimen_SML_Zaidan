import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess(input_path, output_path="processed_heart.csv"):
    df = pd.read_csv(input_path)
    df.columns = df.columns.str.replace('\ufeff', '')

    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # Separate features and target
    X = df.drop("target", axis=1)
    y = df["target"]

    # Scale numerical features
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X),
        columns=X.columns
    )

    processed = X_scaled.copy()
    processed["target"] = y.values

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    processed.to_csv(output_path, index=False)

    print(f"Processed dataset saved to: {output_path}")
    return processed


if __name__ == "__main__":
    INPUT = "../raw_dataset/heart.csv"
    OUTPUT = "processed_heart.csv"
    preprocess(INPUT, OUTPUT)
