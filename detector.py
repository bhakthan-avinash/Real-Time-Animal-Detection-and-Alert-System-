import cv2
from ultralytics import YOLO
import os

class AnimalDetector:
    def __init__(self, model_path='best.pt'):
        # Initialize YOLO model
        self.model = YOLO(model_path)
        self.target_classes = ['tiger', 'boar', 'elephant']
        self.risk_mapping = {
            'tiger': {'level': 'HIGH RISK', 'color': '🔴'},
            'elephant': {'level': 'HIGH RISK', 'color': '🔴'},
            'boar': {'level': 'MEDIUM RISK', 'color': '🟠'}
        }

    def process_video(self, video_path, output_path):
        """
        Processes video and returns the first frame's detections.
        Returns an empty list [] if no target animals are found.
        """
        cap = cv2.VideoCapture(video_path)
        first_detections = []
        
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Run YOLO detection (0.75 confidence threshold)
            results = self.model(frame, conf=0.75, verbose=False)[0]
            
            # Temporary storage for detections in the CURRENT frame
            current_frame_detections = []
            
            for box in results.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id].lower()
                conf = float(box.conf[0])

                if label in self.target_classes:
                    risk_info = self.risk_mapping[label]
                    coords = box.xyxy[0].tolist() # [x1, y1, x2, y2]
                    
                    det_data = {
                        'label': label.capitalize(),
                        'conf': f"{conf:.2f}",
                        'risk': risk_info['level'],
                        'emoji': risk_info['color']
                    }
                    current_frame_detections.append(det_data)
                    
                    # Draw visual cues on the frame to be saved
                    color = (0, 0, 255) if risk_info['level'] == 'HIGH RISK' else (0, 165, 255)
                    cv2.rectangle(frame, (int(coords[0]), int(coords[1])), 
                                  (int(coords[2]), int(coords[3])), color, 3)
                    cv2.putText(frame, f"{label.upper()} {conf:.2f}", (int(coords[0]), int(coords[1]-10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # ACTION: If we found one or more target animals in this specific frame
            if current_frame_detections:
                # Save this frame as the visual proof
                cv2.imwrite(output_path, frame)
                # Store the list of animals found in this frame
                first_detections = current_frame_detections
                # STOP looking further - we have our first detection
                break 

        cap.release()
        
        # Returns [] if the loop finished without finding anything
        return first_detections

# --- Example Usage ---
# detector = AnimalDetector('yolov8n.pt')
# results = detector.process_video('wildlife_clip.mp4', 'detections/alert_frame.jpg')
# 
# if not results:
#     print("No target animals detected.")
# else:
#     print(f"First Detection Found: {results}")