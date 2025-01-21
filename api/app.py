from fastapi import FastAPI
import joblib
import pandas as pd

# Charger le modèle et le vectorizer
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('encoder.pkl')


# Charger l'encodeur préalablement sauvegardé
encoder = joblib.load('encoder.pkl')
app = FastAPI()


def encode_prenom(prenom_a_encoder):
    # Exemple de prénom à encoder

    # Créer un DataFrame avec le prénom
    df_prenom = pd.DataFrame([prenom_a_encoder], columns=['preusuel'])

    # Encoder le prénom avec des variables fictives
    prenom_encoded = encoder.transform(df_prenom['preusuel'].values.reshape(-1, 1))
    return prenom_encoded

# End-point pour la prédiction via GET
@app.get("/predict/")
async def predict_sexe(prenom: str):
    # Transformer le prénom avec le vectorizer
    X_input = encode_prenom(prenom)

    # Prédire le sexe
    pred = model.predict(X_input)

    # Traduire l'étiquette numérique en label de sexe
    label_map = {"1": 'Homme', "2": 'Femme'}
    prediction = label_map[pred[0]]

    return {"prenom": prenom, "sexe": prediction}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)