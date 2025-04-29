import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    roc_curve, auc, silhouette_score
)
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

# --- Example Dataset (replace with your food-nutrients CSV) ---
np.random.seed(0)
df = pd.DataFrame({
    'feature1': np.random.randn(200),
    'feature2': np.random.choice(['A','B','C'], size=200),
    'target': np.random.binomial(1, 0.3, size=200)
})

# --- 1) Threshold sweep on single feature ---
X = df[['feature1']]
y = df['target']
lr = LogisticRegression(solver='liblinear').fit(X, y)
probs = lr.predict_proba(X)[:,1]

thresholds = np.linspace(0, 1, 101)
metrics = {'threshold': [], 'accuracy': [], 'precision': [], 'recall': []}
for t in thresholds:
    preds = (probs >= t).astype(int)
    metrics['threshold'].append(t)
    metrics['accuracy'].append(accuracy_score(y, preds))
    metrics['precision'].append(precision_score(y, preds, zero_division=0))
    metrics['recall'].append(recall_score(y, preds))

mdf = pd.DataFrame(metrics)
plt.figure(figsize=(6,4))
plt.plot(mdf['threshold'], mdf['accuracy'], label='Accuracy')
plt.plot(mdf['threshold'], mdf['precision'], label='Precision')
plt.plot(mdf['threshold'], mdf['recall'], label='Recall')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Threshold vs Metrics (feature1)')
plt.legend()
plt.show()

# --- 2) Full logistic regression with preprocessing ---
numeric = ['feature1']
categorical = ['feature2']
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric),
    ('cat', OneHotEncoder(drop='first'), categorical)
])
pipe = Pipeline([
    ('prep', preprocessor),
    ('lr', LogisticRegression(solver='liblinear'))
])

X_full = df[numeric + categorical]
X_train, X_test, y_train, y_test = train_test_split(
    X_full, y, stratify=y, random_state=0)
pipe.fit(X_train, y_train)
y_prob = pipe.predict_proba(X_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(5,5))
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0,1], [0,1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# --- 3) K-Means clustering analysis ---
features = df[['feature1']]  # extend this list to all your numeric features
for scale_flag in [False, True]:
    Z = features.values
    if scale_flag:
        Z = StandardScaler().fit_transform(Z)
    inertias, sils = [], []
    Ks = range(2, 11)
    for k in Ks:
        km = KMeans(n_clusters=k, random_state=0).fit(Z)
        inertias.append(km.inertia_)
        sils.append(silhouette_score(Z, km.labels_))
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(Ks, inertias, '-o')
    plt.title(f'Inertia (scaled={scale_flag})')
    plt.subplot(1,2,2)
    plt.plot(Ks, sils, '-o')
    plt.title(f'Silhouette (scaled={scale_flag})')
    plt.show()