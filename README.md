
LIE DETECTION AI

A Machine Learning-Based Voice Analysis System


![image alt](https://github.com/BenkhiraAhmedBaderEddine1/LIE-DETECTION-AI/blob/fcb5776c9013746e8cb3c818de39c741cb210c2c/image123.png)



# 1. Abstract

The Lie Detection AI project is an artificial intelligence-based application designed to analyze selected characteristics of human speech using audio signal processing and machine learning techniques. The system allows users to upload an audio recording in WAV format, extracts numerical features from the audio signal, and processes these features using a Random Forest classifier to generate a binary prediction.

The application is developed using Python and integrates several libraries, including Streamlit for the user interface, Librosa for audio processing, NumPy for numerical computations, Pandas for data management, and Scikit-learn for machine learning.

The current prototype analyzes three features: voice stress, pause rate, and an estimated speech-related indicator. These features are passed to the classification model, which produces a predicted class displayed as either “LIE” or “TRUTH.” The application also provides a basic rule-based explanation based on the extracted features.

The primary objective of this project is to demonstrate the integration of audio signal processing, machine learning, and interactive web application development. However, the current implementation uses a very small synthetic dataset, and one of its features is artificially calculated. Therefore, its predictions are experimental and cannot be considered scientifically reliable evidence of deception or truthfulness.

**Keywords:** Artificial Intelligence, Machine Learning, Lie Detection, Audio Signal Processing, Random Forest, Python, Streamlit, Voice Analysis.


2. Introduction

   Artificial Intelligence has become an important technology in the development of intelligent systems capable of processing data, identifying patterns, and generating predictions. One of its applications is speech analysis, which involves examining acoustic characteristics of human speech through digital signal processing and machine learning techniques.

Human speech contains several measurable characteristics, including amplitude, pitch, speaking rate, pauses, and variations in vocal intensity. These characteristics may change depending on a person's emotional state, environment, or speaking conditions. Analyzing these variations provides an opportunity to explore how machine learning can be applied to speech-related data.

The Lie Detection AI project was developed as an educational prototype to demonstrate how an artificial intelligence pipeline can process an audio recording, extract numerical features, and generate a classification result through a trained machine learning model.

The system combines Python-based audio processing with a simple interactive interface, allowing users to upload audio files and view the extracted features and predicted class. The project was also presented in a university competition in collaboration with the Wamidh Club.

Although the application uses the terminology of lie detection, its current capabilities are limited to experimental feature analysis and classification. It does not establish whether a speaker is actually lying. Instead, it demonstrates the technical workflow required to build an audio-based machine learning application and provides a foundation for future improvements.

3. Project Description

The Lie Detection AI system is a web-based application that processes uploaded audio recordings and generates a machine learning classification result.

The application follows a sequence of operations. First, the user uploads an audio file in WAV format. The application temporarily stores the file so that it can be processed. Next, the audio signal is loaded using Librosa, and selected numerical characteristics are calculated.

The extracted features are then passed to a Random Forest classifier that has been trained using a small predefined dataset. The model predicts one of two classes, represented by the labels 0 and 1. The application maps these labels to the displayed categories “TRUTH” and “LIE.”

Finally, the interface presents the audio recording, the calculated feature values, the predicted class, and a simple explanation based on predefined thresholds.

The application is designed to be simple and interactive, making it suitable for demonstrating the integration of data processing, machine learning, and web development in a single project. 
