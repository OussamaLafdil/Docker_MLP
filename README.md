# ECG Classification Project

This project demonstrates the end-to-end process of developing, training, and deploying a machine learning model for ECG classification. A core feature of the project is the use of Docker to ensure reproducibility, portability, and ease of deployment.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Docker Overview](#docker-overview)
- [Training Environment](#training-environment)
- [Deployment Environment](#deployment-environment)
- [Setup and Usage](#setup-and-usage)
- [Training the Model in Docker](#training-the-model-in-docker)
- [Deploying the API with Docker](#deploying-the-api-with-docker)
- [Results](#results)
- [Docker Images](#docker-images)


## Introduction
This project uses a machine learning model to classify ECG (Electrocardiogram) data into normal or abnormal categories. The entire workflow, from training to deployment, is containerized with Docker to ensure:

- **Reproducibility**: Identical environments across systems.
- **Portability**: Easily shareable images on Docker Hub.
- **Simplicity**: Quick and consistent setup for both training and deployment.

## Project Structure

├── Dockerfile # Dockerfile for training the model
├── a.Dockerfile # Dockerfile for deploying the Flask API
├── train_model.py # Script for training and saving the model
├── app.py # Flask API for predictions
├── ecg_model.pkl # Saved model
├── ecg.csv # ECG dataset
├── venv/ # Local virtual environment (optional)

## Docker Overview

### Training Environment
**Dockerfile:**
- Uses a lightweight python:3.9-slim base image.
- Installs required libraries like TensorFlow, Pandas, and Pickle.
- Automates the training process, including model serialization.

**Benefits:**
- Ensures consistency in training environments.
- Eliminates dependency issues across different machines.

### Deployment Environment
**a.Dockerfile:**
- Configures a minimal Flask API environment.
- Copies the saved model and API script (app.py) into the container.
- Exposes port 3000 for accessing the API.

**Benefits:**
- Seamlessly deploys the trained model as a RESTful API.
- Provides real-time predictions through HTTP requests.

## Setup and Usage

### Prerequisites
- Install Docker on your machine.

### Training the Model in Docker
1. Build the training Docker image:
```bash
docker build -t ecg-train -f Dockerfile .
```
2. Run the training container:
```bash
docker run --rm ecg-train
```
This will train the model and save it as ecg_model.pkl.

### Deploying the API with Docker
1. Build the API Docker image:
```bash
docker build -t ecg-api -f a.Dockerfile .
```
2. Run the API container:
```bash
docker run -p 3000:3000 ecg-api
```
3. Access the API:
- Open your browser or use tools like Postman to access http://localhost:3000
- Use the HTML interface to upload a JSON file for predictions
### Results
Model Accuracy:
- 99.3% on the test dataset.
Containerized Environment:
- Training and deployment environments are fully isolated.
- Deployment is portable and replicable across systems.

### Docker Images
The following images are available on Docker Hub:

1. Training Image: [ECG Training Environment](https://hub.docker.com/r/oussamalatardo/lafdil_oussama_env)
2. Deployment Image: [ECG API Environment](https://hub.docker.com/r/oussamalatardo/lafdil_oussama_dep)

To pull these images:

```bash
docker pull oussamalatardo/lafdil_oussama_env
docker pull oussamalatardo/lafdil_oussama_dep
```