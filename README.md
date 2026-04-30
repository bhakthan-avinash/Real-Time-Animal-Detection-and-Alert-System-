# 🚨 Real Time Animal Detection and Alert System

An AI-powered web application that detects wildlife from video input using YOLO and triggers real-time alerts with risk classification and location tracking.
## Overview
This project uses deep learning and computer vision to detect animals such as **tiger, elephant, and boar** from uploaded videos. It provides a dashboard-style interface with detection results, risk levels, live location mapping, and an automatic alarm system.

## 🎯 Features
- 🧠 YOLO-based wildlife detection (Ultralytics)
- 🎥 Video upload and frame-by-frame processing
- 🐾 Multi-animal detection (same frame supported)
- ⚠ Risk classification:
  - 🔴 High Risk → Tiger, Elephant  
  - 🟠 Medium Risk → Boar
- 🖼 Bounding box + confidence score display
- 🗺 Live location map (Leaflet.js + OpenStreetMap)
- 🚨 Automatic alarm system (loop until stopped)
- 🔄 Reset system functionality
- 🎨 Modern dashboard UI (dark theme)
## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **AI Model:** YOLO (Ultralytics)
- **Video Processing:** OpenCV
- **Frontend:** HTML, CSS, JavaScript
- **Map Integration:** Leaflet.js + OpenStreetMap
- **Geolocation:** Browser Geolocation API
Real-Time-Animal-Detection/
│
├── app.py
├── detector.py
├── requirements.txt
│
├── templates/
│ ├── index.html
│ └── result.html
│
├── static/
│ ├── style.css
│ ├── app.js
│ └── alarm.mp3
│
├── uploads/
└── README.md

# How to Run Locally
 1. Clone the repository
```bash
git clone https://github.com/bhakthan-avinash/Real-Time-Animal-Detection-and-Alert-System-.git
cd Real-Time-Animal-Detection-and-Alert-System-
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add YOLO model
Download best.pt and place it in root directory.
5. Run the app
python app.py
Open:
http://127.0.0.1:5000
🚨 System Workflow
Upload video
YOLO detects animals frame-by-frame
All valid detections are collected
Bounding boxes + risk levels displayed
Alarm triggers automatically
Location shown on map
---

## 📁 Project Structure
