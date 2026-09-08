from flask import Flask, render_template, Response, request, jsonify
import cv2
import numpy as np
from deepface import DeepFace
import threading
import time

app = Flask(__name__)

# Global variables for emotion analysis
frame_count = 0
skip_frames = 5
emotions_dict = {}
last_analysis_time = 0
analysis_lock = threading.Lock()

# Load face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def analyze_emotion(frame):
    """Analyze emotion from a frame"""
    global emotions_dict, frame_count, last_analysis_time
    
    with analysis_lock:
        if frame_count % skip_frames != 0:
            return
        
        try:
            # Convert BGR to RGB for DeepFace
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
            if results:
                emotions_dict = results[0]['emotion']
            last_analysis_time = time.time()
        except Exception as e:
            print(f"Analysis error: {e}")

def generate_frames():
    """Generate video frames with emotion analysis"""
    global frame_count, emotions_dict
    
    cap = cv2.VideoCapture(0)
    
    # Set camera properties for better web streaming
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 5)
        
        # Analyze emotion in a separate thread to avoid blocking
        if frame_count % skip_frames == 0:
            thread = threading.Thread(target=analyze_emotion, args=(frame.copy(),))
            thread.daemon = True
            thread.start()
        
        # Draw rectangles and HUD for each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Draw HUD with emotions
            if emotions_dict:
                display_emotions = ['happy', 'sad', 'angry', 'surprise', 'neutral']
                for i, emo_name in enumerate(display_emotions):
                    score = emotions_dict.get(emo_name, 0)
                    bar_x, bar_y = x + w + 10, y + (i * 30)
                    bar_width = int(score * 1.5)
                    
                    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + 150, bar_y + 20), (50, 50, 50), -1)
                    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + 20), (255, 200, 0), -1)
                    cv2.putText(frame, f"{emo_name}: {int(score)}%", (bar_x, bar_y - 5), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if ret:
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes)
        
        # Small delay to control frame rate
        time.sleep(0.03)
    
    cap.release()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Stream video feed"""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_emotions')
def get_emotions():
    """Get current emotion data as JSON"""
    return jsonify(emotions_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
