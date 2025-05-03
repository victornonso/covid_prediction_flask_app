import xgboost, joblib, pandas as pd, numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

model  = joblib.load('models/best_covid_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Try the model’s names first, else use the scaler’s:
try:
    FEATURE_NAMES = list(model.feature_names_in_)
except AttributeError:
    FEATURE_NAMES = list(scaler.feature_names_in_)

@app.route('/', methods=['GET','POST'])
def index():
    prediction = None
    probability = None

    if request.method == 'POST':
        # Build one‑row dict of inputs
        data = {}
        for feat in FEATURE_NAMES:
            if feat == 'Sex':
                sex = request.form.get('Sex', 'female').lower()
                data['Sex'] = 1 if sex == 'male' else 0

            elif feat == 'Age':
                # we collect Birth_Year, then compute Age
                byear = int(request.form.get('Birth_Year', 2025))
                data['Age'] = 2025 - byear

            else:
                # all other features ⇒ YES/NO radios
                val = request.form.get(feat, 'no').lower()
                data[feat] = 1 if val == 'yes' else 0

        # Create DataFrame, enforce column order and fill any missing with 0
        X = pd.DataFrame([data])
        X = X.reindex(columns=FEATURE_NAMES, fill_value=0)

        # Scale & predict
        X_scaled = scaler.transform(X.astype(np.float32))
        prob_pos = model.predict_proba(X_scaled)[0, 1]

        prediction = 'POSITIVE' if prob_pos >= 0.5 else 'NEGATIVE'
        probability = f"{prob_pos:.2%}"

    return render_template(
        'index.html',
        feature_names=FEATURE_NAMES,
        prediction=prediction,
        probability=probability
    )

if __name__ == '__main__':
    app.run(debug=False)
