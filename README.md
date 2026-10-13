
LIE DETECTION AI

A Machine Learning-Based Voice Analysis System

# 1. Abstract

The Lie Detection AI project is an artificial intelligence-based application designed to analyze selected characteristics of human speech using audio signal processing and machine learning techniques. The system allows users to upload an audio recording in WAV format, extracts numerical features from the audio signal, and processes these features using a Random Forest classifier to generate a binary prediction.

The application is developed using Python and integrates several libraries, including Streamlit for the user interface, Librosa for audio processing, NumPy for numerical computations, Pandas for data management, and Scikit-learn for machine learning.

The current prototype analyzes three features: voice stress, pause rate, and an estimated speech-related indicator. These features are passed to the classification model, which produces a predicted class displayed as either “LIE” or “TRUTH.” The application also provides a basic rule-based explanation based on the extracted features.

The primary objective of this project is to demonstrate the integration of audio signal processing, machine learning, and interactive web application development. However, the current implementation uses a very small synthetic dataset, and one of its features is artificially calculated. Therefore, its predictions are experimental and cannot be considered scientifically reliable evidence of deception or truthfulness.

**Keywords:** Artificial Intelligence, Machine Learning, Lie Detection, Audio Signal Processing, Random Forest, Python, Streamlit, Voice Analysis.
