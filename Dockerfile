# Utiliser l'image officielle de Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app/

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000 pour l'application FastAPI
EXPOSE 8000

# Lancer Uvicorn pour démarrer l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
