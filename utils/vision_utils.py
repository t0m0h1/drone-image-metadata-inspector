from ultralytics import YOLO
import cv2

# Load model once (important for performance)
model = YOLO("yolov8n.pt")

# Classes useful for inspections / drone imagery
RELEVANT_CLASSES = {
    "person",
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle",
    "building",
    "roof",
    "house",
    "road",
    "tree"
}


def analyse_image(image_path, confidence_threshold=0.4):
    """
    Runs YOLOv8 object detection on an image.
    Returns structured detection results.
    """
    results = model(image_path, verbose=False)
    detections = []

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            if conf < confidence_threshold:
                continue

            class_id = int(box.cls[0])
            label = model.names[class_id]

            # Optional filtering
            # if label not in RELEVANT_CLASSES:
            #     continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "label": label,
                "confidence": round(conf, 3),
                "box": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                },
                "image_size": {
                    "width": width,
                    "height": height
                }
            })

    return detections
