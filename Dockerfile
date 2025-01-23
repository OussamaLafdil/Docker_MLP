# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-pip \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installer les bibliothèques Python nécessaires
RUN pip install --upgrade pip && \
    pip install tensorflow pandas scikit-learn pickle5

# Copier les fichiers du projet dans le conteneur
COPY train_model.py /app/
COPY ecg.csv /app/

# Commande par défaut pour exécuter le script Python
CMD ["python", "train_model.py"]
