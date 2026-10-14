 <p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=250&color=0:020617,25:0B1535,55:312E81,80:075985,100:00F5FF&text=LIE%20DETECTION%20AI&fontColor=FFFFFF&fontSize=42&fontAlignY=40&animation=twinkling&stroke=00F5FF&strokeWidth=1" width="100%" alt="LIE DETECTION AI"/>
</p>

<p align="center">
  <b>A Machine Learning-Based Voice Analysis System</b>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=18&duration=2500&pause=800&color=00F5FF&center=true&vCenter=true&width=850&height=55&lines=VOICE+ANALYSIS+%7C+MACHINE+LEARNING;AUDIO+SIGNAL+PROCESSING;FEATURE+EXTRACTION+%7C+AI;EXPLORE+THE+SIGNAL.+EVALUATE+THE+EVIDENCE." alt="Animated project tagline"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ARTIFICIAL_INTELLIGENCE-00F5FF?style=for-the-badge&labelColor=020617" alt="Artificial Intelligence"/>
  <img src="https://img.shields.io/badge/MACHINE_LEARNING-7B2CFF?style=for-the-badge&labelColor=020617" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/VOICE_ANALYSIS-FF3CAC?style=for-the-badge&labelColor=020617" alt="Voice Analysis"/>
</p>

---

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


3. Project Description
   
The Lie Detection AI system is a web-based application that processes uploaded audio recordings and generates a machine learning classification result.
The application follows a sequence of operations. First, the user uploads an audio file in WAV format. The application temporarily stores the file so that it can be processed. Next, the audio signal is loaded using Librosa, and selected numerical characteristics are calculated.
The extracted features are then passed to a Random Forest classifier that has been trained using a small predefined dataset. The model predicts one of two classes, represented by the labels 0 and 1. The application maps these labels to the displayed categories “TRUTH” and “LIE.”
Finally, the interface presents the audio recording, the calculated feature values, the predicted class, and a simple explanation based on predefined thresholds.
The application is designed to be simple and interactive, making it suitable for demonstrating the integration of data processing, machine learning, and web development in a single project.




5. Problem Statement
   
Analyzing human speech computationally presents several challenges because vocal characteristics vary between individuals and across different situations. Changes in speaking patterns may be associated with stress, anxiety, fatigue, environmental noise, or other factors.
The main problem addressed by this project is how to develop a simple application that processes speech recordings, extracts measurable audio features, and applies a machine learning classifier to produce a structured prediction.
The project explores the following question:
How can audio signal processing and machine learning be integrated into an interactive application for experimental speech-feature classification?
The current prototype addresses this question by implementing a basic feature extraction process, a Random Forest classification model, and an interactive Streamlit interface. Determining whether the predictions correspond to actual deception would require a much larger, carefully labeled dataset and rigorous scientific validation.





6. Project Objectives
   
The main objective of the Lie Detection AI project is to develop an interactive machine learning application that demonstrates the processing and classification of audio data.
The specific objectives are:
1. To develop a user-friendly interface for uploading audio recordings.
2. To process audio files using Python-based audio processing tools.
3. To extract numerical features from the audio signal.
4. To implement a Random Forest classification algorithm.
5. To generate a binary prediction from the extracted features.
6. To display the extracted features and classification results.
7. To provide a simple rule-based explanation of selected feature values.
8. To demonstrate the practical integration of Artificial Intelligence and web application development.
9. To identify the limitations of the current prototype and propose future improvements.
10. To establish a foundation for more rigorous research into speech analysis and machine learning.




6. Project Scope
   
 The scope of the current project is limited to a proof-of-concept application that accepts WAV audio recordings and classifies extracted numerical features using a predefined Random Forest model.
The implementation includes audio file uploading, temporary file storage, audio signal loading, basic feature calculations, machine learning prediction, and result visualization.
The current version does not include a large-scale training dataset, speaker identification, facial analysis, real-time recording, advanced speech recognition, or a scientifically validated deception detection method. In particular, the eye-shift feature is simulated from the voice-stress feature and does not represent an actual measurement of eye movement.
Consequently, the system should be considered an educational demonstration rather than a reliable lie detection instrument.

7. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application interface |
| NumPy | Numerical calculations and signal analysis |
| Pandas | Dataset creation and feature organization |
| Librosa | Audio loading and processing |
| Scikit-learn | Machine learning and classification |
| Random Forest | Classification algorithm |
| Temporary Files | Intermediate storage of uploaded audio |
