from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Lolo !</p>"

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Si le formulaire est soumis, récupérer le prénom à partir du formulaire
        prenom = request.form['prenom']
        prenom_lettres = prenom

        # Charger le modèle avec joblib
        prenom_encoded = encode_prenom(prenom)
        # Appliquer le modèle PyTorch avec .predict
        result = make_prediction(prenom_encoded)

        # Retourner le résultat
        return render_template('predict_result.html', prenom=prenom_lettres, result=result)

    # Si la méthode est GET, simplement afficher le formulaire
    return render_template('predict_form.html')

def encode_prenom(prenom: str) -> pd.Series:
    alphabet = "abcdefghijklmnopqrstuvwxyzé-'"
    prenom = prenom.lower()

    return pd.Series([letter in prenom for letter in alphabet]).astype(int)

def make_prediction(prenom):
    regr_loaded = joblib.load("model.v2.bin")
    prediction = regr_loaded.predict([prenom])
    return prediction.item()

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
