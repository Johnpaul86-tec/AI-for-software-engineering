# 🌾 Smart Agriculture Edge AI & IoT Project  
**Part 2: Practical Implementation — PLP Academy AI Development Workflow Assignment**

---

## 📘 Project Overview
This repository demonstrates how Edge AI and IoT technologies combine to build a smart agriculture system. It contains two complementary tasks:

- Task 1 — Edge AI Prototype: build, convert and run a lightweight image-classification model with TensorFlow Lite for edge devices (e.g., Raspberry Pi).  
- Task 2 — AI-Driven IoT Concept: simulate a smart-agriculture system where IoT sensor data is used to predict crop yield; train, evaluate and export a TFLite model for edge deployment.

Together, they illustrate real-time, privacy-preserving, offline-capable ML for agriculture.

---

## ⚙️ Folder Structure
Smart_Agriculture_AI/
├── edge_ai_prototype/  
│   ├── recyclable_classifier.py         # Training & conversion to TFLite  
│   ├── recyclable_classifier.tflite     # Converted lightweight model  
│   ├── results.txt                       # Test accuracy (example: 53.85%)  
│   └── edge_inference.py                 # Example script to run TFLite model on device  
├── smart_agriculture_iot/  
│   ├── smart_agriculture_simulation.py   # IoT data simulation + training + conversion  
│   └── smart_agri_yield_model.tflite     # Edge-deployable TFLite model  
└── README.md                             # Documentation (this file)

---

## 🧩 Task 1 — Edge AI Prototype

### 🎯 Goal
Train a lightweight CNN to recognize recyclable items, convert it to TensorFlow Lite, and simulate edge inference.

### 🧠 Model Summary
- Framework: TensorFlow / Keras  
- Dataset: CIFAR-10 (subset for demo)  
- Architecture: Lightweight CNN (2 Conv layers + Dense layers)  
- Test accuracy: ~53.85%  
- TFLite model size: ~1.3 MB  
- Typical inference time: < 50 ms per image (device-dependent)

### 🧰 Steps to run
1. Open `edge_ai_prototype/recyclable_classifier.py` (Colab or VS Code).
2. Install dependencies:
  ```
  pip install tensorflow
  ```
3. Run the training/evaluation script. The script will save a `.tflite` model.

Deployment on Raspberry Pi (example):
```
pip install tflite-runtime
python3 edge_inference.py
```
`edge_inference.py` demonstrates running the `.tflite` model for local classification.

### 🌍 Edge AI Benefits
- Low latency: real-time inference locally  
- Enhanced privacy: raw data remains on device  
- Offline capability: works without internet  
- Energy efficient: reduced network usage

---

## 🌾 Task 2 — AI-Driven IoT Concept

### 🎯 Goal
Simulate a smart-agriculture system: generate synthetic IoT sensor data (soil moisture, temperature, humidity, rainfall, sunlight, etc.), train a model to predict crop yield, evaluate it, and export a TFLite model for edge inference.

### 🧠 Simulation model (overview)
- Generates synthetic sensor readings  
- Trains a small neural network to predict yield (kg/ha)  
- Evaluates model performance and exports a TFLite model

### 📊 Example results
| Metric | Value |
|---|---:|
| Mean Absolute Error (MAE) | ~8–12 kg/ha (typical run) |
| TFLite model size | ~0.7 MB |

### 🧱 Suggested real sensors
- Soil moisture & soil temperature  
- Air temperature & humidity  
- Rainfall & sunlight (irradiance)  
- Soil pH & EC  

Optional: RGB/NDVI camera for crop health monitoring

### 🔄 Data flow (conceptual)
[ Sensors ] → [ Edge Gateway (Raspberry Pi) ] → [ Cloud (Model Training & Storage) ]  
      ↑                     ↓  
    (Actuators)         [ Edge Inference (TFLite) ]

### ⚙️ How to run the simulation
1. Open `smart_agriculture_iot/smart_agriculture_simulation.py`.
2. Install dependencies:
  ```
  pip install tensorflow pandas scikit-learn matplotlib
  ```
3. Run the script — it will:
  - Simulate sensor data  
  - Train and evaluate a model  
  - Plot training metrics  
  - Export a TFLite model

---

## 🔗 Integration (Edge–Cloud)
- Edge (Raspberry Pi): real-time inference, local control (e.g., irrigation actuators), low-latency decisions.  
- Cloud: heavy training, long-term storage, model updates and analytics.  
- Hybrid approach: train in cloud, deploy optimized TFLite models to edge gateways.

---

## 🧾 Key Takeaways
- Edge AI reduces latency and enhances privacy.  
- TensorFlow Lite enables efficient deployment on resource-constrained devices.  
- IoT sensors provide timely inputs for predictive models that can improve farm management.

---

## 🧑‍💻 Contributors
- Student: [Your Name Here]  
- Cohort: PLP Academy — July 2025 AI Development Workflow  
- Instructor: [Instructor Name or Placeholder]

---

## 🧠 Suggested future improvements
- Use real IoT streams via MQTT, AWS IoT Core or Azure IoT Hub.  
- Implement anomaly detection for early disease/water-stress alerts.  
- Add dashboard visualization (Streamlit, Dash, Grafana).  
- Expand datasets and hyperparameter tuning for improved accuracy.

---

If you want, I can:
- produce a stripped-down quickstart section, or  
- create example commands for Docker/MQTT integration, or  
- generate a short CONTRIBUTING.md template.