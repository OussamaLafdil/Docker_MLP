# Étape 3 : Entraînement dans un conteneur Docker

# Importation des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import pickle

# Charger le fichier ecg.csv
data = pd.read_csv('ecg.csv')

# Diviser les données en jeux d'entraînement et de test
X = data.iloc[:, :-1]  # Toutes les colonnes sauf la dernière
y = data.iloc[:, -1]   # La dernière colonne


# Définir le modèle de réseau de neurones
model = Sequential()
model.add(Dense(16, input_dim=X.shape[1], activation='sigmoid'))  # Première couche cachée
model.add(Dense(8, activation='sigmoid'))  # Deuxième couche cachée
model.add(Dense(1, activation='sigmoid'))  # Couche de sortie

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(X, y, epochs=50, batch_size=4, verbose=1)


# Sauvegarder le modèle avec Pickle
with open('ecg_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

