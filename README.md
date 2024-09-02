
# 🎭 AI Face Recognition System
![image](https://github.com/user-attachments/assets/89fdbc11-3cfd-43d3-af03-c3c023083fad)

## 📸 Real-time Face Detection & Recognition with Email Notifications

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Dropbox](https://img.shields.io/badge/Dropbox-0061FF?style=for-the-badge&logo=dropbox&logoColor=white)
![SendGrid](https://img.shields.io/badge/SendGrid-1A82E2?style=for-the-badge&logo=sendgrid&logoColor=white)

This project integrates fast and accurate facial recognition with real-time monitoring and email notifications, using Raspberry Pi and IoT technology for enhanced security and user information protection.

### 🌟 Key Features

- 🚀 Real-time face detection and recognition
- 🔥 Firebase integration for instant logging
- 📦 Dropbox storage for captured images
- 🔄 Supports both Raspberry Pi Camera and webcams
- 🧠 Uses CNN model for accurate face recognition
- 📧 Automatic email notifications via SendGrid when faces are detected

### 🛠️ Technology Stack

- Python 3
- OpenCV
- face_recognition library
- Firebase Realtime Database
- Firebase Cloud Functions
- Dropbox API
- SendGrid Email API
- Raspberry Pi Camera / Standard Webcam
- Pickle for data serialization

## 📁 Project Structure

```
├── encoding.py      # Generate face encodings
├── face.py          # Main script for Raspberry Pi
├── test.py          # Alternative script for webcams
├── haarcascades/    # Contains Haar Cascade XML files
├── dataset/         # Your face image dataset
└── functions/
    └── index.js     # Firebase Cloud Function for email notifications
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

6. **Configure SendGrid and Firebase Cloud Functions**
   - Set up a SendGrid account and obtain an API key
   - Deploy the Firebase Cloud Function in `functions/index.js`
   - Update the SendGrid API key and email addresses in the Cloud Function

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

## 📧 Email Notifications

When a face is detected and recognized:
1. The system updates the Firebase Realtime Database
2. This triggers the Cloud Function
3. An email is sent via SendGrid with details of the detected face

## 🌟 Result
![image](https://github.com/user-attachments/assets/507c271c-0b36-4634-a804-0296a3ed16a3)

## 📝 Notes

- Dropbox token expires after 4 hours
- Use `test.py` for local testing without cloud features
- Adjust `frame_resolution` and `frame_rate` in `face.py` as needed
- Keep your SendGrid API key confidential
- Ensure your Firebase project is on a plan that supports Cloud Functions
- Test the email functionality in a controlled environment first



