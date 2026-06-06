# Real-Time Emotion Detection HUD

An optimized, real-time computer vision pipeline built with Python that detects human faces via webcam and performs deep-learning-based facial expression analysis to predict current emotional states. 

This project isolates the core visual computing intelligence layer from an emotion-based system to provide a clean, modular, and highly reusable standalone execution script.

---

## 🚀 Key Features

* **Real-Time Face Tracking:** Integrates OpenCV's Haar Cascade architecture for rapid, low-latency face detection and dynamic bounding box generation.
* **Deep Learning Inference:** Leverages pre-trained Convolutional Neural Networks (CNNs) via the DeepFace framework to classify facial matrices into 7 core human emotions.
* **Performance Matrix Optimization:** Implements a custom frame-skipping algorithm (processing neural net inference every 3rd frame) to ensure a fluid, high-FPS video feed without taxing CPU thresholds on consumer-grade hardware.
* **State Persistence HUD:** Prevents UI text flickering by caching the last successfully inferred emotion until the next computational cycle clears.

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.8+[cite: 1]
* **Computer Vision Framework:** OpenCV (`cv2`)
* **Deep Learning Interface:** DeepFace (TensorFlow backend)
* **Object Detection Engine:** Haar Cascade Classifiers (`haarcascade_frontalface_default.xml`)

---

## 📦 Directory Structure

Organize your workspace files as follows before running or pushing to GitHub:
```text
├── emotion_hud.py        # Main execution script containing the optimized vision loop[cite: 1, 2]
├── requirements.txt      # Text file managing python dependencies[cite: 1, 2]
└── README.md             # Project documentation[cite: 1, 2]
