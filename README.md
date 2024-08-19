# 🎭 AI Face Recognition System

## 📸 Real-time Face Detection & Recognition for Raspberry Pi and Webcams

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Dropbox](https://img.shields.io/badge/Dropbox-0061FF?style=for-the-badge&logo=dropbox&logoColor=white)

This project brings advanced face recognition capabilities to your Raspberry Pi or standard webcam setup, leveraging the power of AI and cloud technologies.

### 🌟 Key Features

- 🚀 Real-time face detection and recognition
- 🔥 Firebase integration for instant logging
- 📦 Dropbox storage for captured images
- 🔄 Supports both Raspberry Pi Camera and webcams
- 🧠 Uses CNN model for accurate face recognition

### 🛠️ Technologies Used

- Python 3
- OpenCV
- face_recognition library
- Firebase Realtime Database
- Dropbox API
- Raspberry Pi Camera / Standard Webcam
- Pickle for data serialization

## 📁 Project Structure

```
├── encoding.py      # Generate face encodings
├── face.py          # Main script for Raspberry Pi
├── test.py          # Alternative script for webcams
├── haarcascades/    # Contains Haar Cascade XML files
└── dataset/         # Your face image dataset
```

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install opencv-python face_recognition pickle firebase-admin dropbox
   ```

2. **Prepare Your Dataset**
   - Add face images to `dataset/` directory
   - Update `dataset_paths` and `names` in `encoding.py`

3. **Generate Encodings**
   ```bash
   python encoding.py
   ```

4. **Configure Firebase**
   - Set up a Firebase project
   - Download credentials JSON
   - Update Firebase config in `face.py`

5. **Set Up Dropbox**
   - Create a Dropbox app
   - Generate an access token
   - Update `dropbox_token` in `face.py`

## 🖥️ Usage

**For Raspberry Pi:**
```bash
python face.py
```

**For Webcam:**
```bash
python test.py
```

Press 'q' to exit the application.

## 📝 Notes

- Dropbox token expires after 4 hours
- Use `test.py` for local testing without cloud features
- Adjust `frame_resolution` and `frame_rate` in `face.py` as needed


