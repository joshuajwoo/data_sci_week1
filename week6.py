import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load data
df = pd.read_csv("employee.csv")          # Your combined train‑and‑validate file
test_df = pd.read_csv("employee_test.csv")  # Unseen data for final predictions

TARGET_COL = "Salary"                     # Change to the variable you want to predict

X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

# Identify column types
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = X.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

# Build preprocessing + model pipeline
numeric_pipe = Pipeline(
    steps=[
        ("scaler", StandardScaler())
    ]
)

categorical_pipe = Pipeline(
    steps=[
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipe, numeric_cols),
        ("cat", categorical_pipe, categorical_cols)
    ]
)

model = LinearRegression()

pipe = Pipeline(
    steps=[
        ("prep", preprocessor),
        ("lm", model)
    ]
)

# Train/validation split and metrics
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_val)

mae = mean_absolute_error(y_val, y_pred)
rmse = np.sqrt(mean_squared_error(y_val, y_pred))

print(f"Validation MAE:  {mae:,.2f}")
print(f"Validation RMSE: {rmse:,.2f}")

# Retrain on full data and predict on held‑out test set
pipe.fit(X, y)

test_preds = pipe.predict(test_df)

# Add predictions to a copy of the test DataFrame (optional)
output = test_df.copy()
output["Predicted_" + TARGET_COL] = test_preds

# Save to CSV
output.to_csv("employee_test_predictions.csv", index=False)
print("Predictions saved to employee_test_predictions.csv")