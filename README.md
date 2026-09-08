# Emotion Detection Web Application

A web-based emotion detection system that analyzes facial expressions in real-time using your webcam.

## Features

- **Real-time emotion detection** using DeepFace AI
- **Web-based interface** - accessible from any browser
- **Optimized performance** - analyzes every 5th frame for better speed
- **Visual HUD** - displays emotion bars next to detected faces
- **Responsive design** - works on desktop and mobile browsers

## Supported Emotions

- Happy
- Sad
- Angry
- Surprise
- Neutral

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the web application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## How It Works

1. The application accesses your webcam through the browser
2. Faces are detected using OpenCV's Haar Cascade classifier
3. Every 5th frame, DeepFace AI analyzes the detected face for emotions
4. Results are displayed both on the video feed (as an overlay) and in a separate panel
5. The emotion bars update in real-time via AJAX requests

## Project Structure

```
/workspace
├── app.py              # Flask web application
├── emotion.py          # Original Python script (reference)
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Web interface
```

## Usage Tips

- Allow camera access when prompted by your browser
- Ensure good lighting for best face detection results
- Press 'q' in the original script or close the browser tab to stop
- Click "Fullscreen" for an immersive experience

## Technical Details

- **Backend**: Flask (Python web framework)
- **Computer Vision**: OpenCV
- **AI Model**: DeepFace
- **Frontend**: HTML5, CSS3, JavaScript
- **Video Streaming**: Multipart JPEG streaming

## Browser Compatibility

Works best on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

## License

Same as the original project license.
