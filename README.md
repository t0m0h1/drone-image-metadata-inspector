# AI Image Metadata & Insight Tool


A web-based AI application that allows users to upload images (such as drone photographs) and automatically extract metadata, analyse visual content using computer vision, and generate human-readable insights. The tool is designed for use cases such as drone surveying, construction inspections, real estate analysis, and infrastructure monitoring.

---

## Project Overview

This application processes uploaded images to:

* Extract EXIF metadata (GPS location, altitude, camera information, timestamps)
* Visualise image locations on an interactive map
* Detect objects and features within images using AI
* Generate automated insights based on detected features and metadata

The project combines web development, data processing, and applied AI into a single, extensible system.

---

## Core Features (Roadmap)

### 1. Image Upload & Validation

Users can upload one or more images through a web interface. The backend validates file types and securely stores uploaded images for processing.

Planned enhancements include drag-and-drop uploads and batch processing.

---

### 2. EXIF Metadata Extraction

The system extracts and displays available metadata from images, including:

* Latitude and longitude
* Altitude
* Camera make and model
* Date and time the image was captured

This metadata forms the foundation for mapping, filtering, and insight generation.

---

### 3. Map Visualisation

Extracted GPS coordinates are plotted on an interactive map. Each marker corresponds to an uploaded image and allows users to view:

* Image preview
* Location details
* Associated metadata and insights

This feature enables spatial context and easy navigation between images.

---

### 4. AI Object Detection

Images are analysed using computer vision models to detect relevant objects and features, such as:

* Buildings and roofs
* Roads and vehicles
* Vegetation
* General structures

Detections include labels, confidence scores, and bounding box data, providing a basis for further inspection and reporting.

---

### 5. Automated Insight Generation

The application generates plain-English insights based on:

* Detected objects
* Confidence levels
* Available metadata (e.g. altitude or GPS presence)

Examples include identifying structures, highlighting environmental features, or noting missing metadata. This logic starts rule-based and can later be extended with large language models.

---

## Technology Stack

### Frontend

* HTML and CSS for layout and styling
* JavaScript for interactivity and API communication
* Leaflet.js for map rendering

### Backend

* Python with Flask for API routes and processing
* Pillow and ExifRead for image and metadata handling
* OpenCV and optional YOLO models for computer vision

### Data Storage

* Local file storage for uploaded images
* SQLite for metadata, detections, and results (planned)

---

## Project Structure

```
ai-image-inspector/
│
├── app.py
├── requirements.txt
│
├── utils/
│   ├── exif_utils.py
│   ├── vision_utils.py
│   └── insight_engine.py
│
├── static/
│   └── uploads/
│
└── templates/
    └── index.html
```

---

## Future Enhancements

Planned future development includes:

* Real-time YOLO-based object detection
* Multi-image and batch uploads
* Historical comparison between image sets
* Exportable inspection reports (PDF)
* Role-specific insight modes (construction, agriculture, real estate)
* Public or paid API access

---

## Intended Use Cases

* Drone inspections and surveys
* Construction site progress tracking
* Property and roof inspections
* Infrastructure and asset monitoring

---

## Status

This project is under active development. The current implementation focuses on backend foundations, with frontend visualisation and advanced AI features planned next.
