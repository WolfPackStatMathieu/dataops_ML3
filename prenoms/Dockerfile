# Utiliser une image Python officielle comme base
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur à /app/
COPY ./pyproject.toml /app/
COPY ./poetry.lock /app/

# Installer les dépendances
RUN pip install poetry && poetry install

# Copier le reste des fichiers dans le conteneur à /app/
COPY . /app/

# Exposer le port 5000 (le port par défaut utilisé par Flask)
EXPOSE 5000

# Commande à exécuter à chaque démarrage du conteneur
# CMD ["poetry", "run", "python", "api.py"]
CMD ["bash", "-c", "flask --app api run --host 0.0.0.0 --port $FLASK_PORT"]