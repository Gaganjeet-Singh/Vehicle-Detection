Vehicle Detection

This project uses YOLOv8 and OpenCV to detect and count vehicles in a video. It is designed to monitor traffic in real-time and provides a simple interface to visualize vehicle movement across a designated line.

Project Structure
Vehicle Detection/
│
├── main.py          # Main Python script to run the vehicle detection
├── video.mp4        # Sample video of moving vehicles
├── yolov8n.pt       # Pre-trained YOLOv8 model
└── README.md        # Project description and instructions

How It Works

The script reads the video video.mp4 frame by frame using OpenCV.

Each frame is passed to the YOLO model to detect objects.

Vehicles are identified based on their class (car, motorcycle, bus, truck).

Detected vehicles are highlighted with bounding boxes and labeled.

The script counts vehicles crossing a predefined horizontal line (count_line_y = 300).

The total vehicle count is displayed on the video in real-time.

Usage

Make sure you have Python installed along with the required libraries:

pip install ultralytics opencv-python


Run the main script:

python main.py


A window will open showing the video with vehicle detection.

Press q to quit the video window at any time.

Notes

The YOLO model file yolov8n.pt should be in the same folder as main.py.

You can replace video.mp4 with any other traffic video to test the detection.

The counting line (count_line_y) can be adjusted based on the video frame to match the road position.