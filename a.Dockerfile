# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installer les bibliothèques Python nécessaires
RUN pip install --upgrade pip && \
    pip install flask tensorflow pandas pickle5 numpy

# Copier les fichiers du projet
COPY app.py /app/
COPY ecg_model.pkl /app/

# Exposer le port utilisé par Flask
EXPOSE 3000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]
