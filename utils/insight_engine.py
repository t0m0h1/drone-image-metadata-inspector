def generate_insights(detections, exif):
    insights = []

    if not detections:
        insights.append("No significant objects detected in the image.")
        return insights

    labels = {}
    for d in detections:
        labels[d["label"]] = labels.get(d["label"], 0) + 1

    for label, count in labels.items():
        insights.append(
            f"Detected {count} instance(s) of '{label}'."
        )

    # Contextual metadata insights
    if "latitude" in exif and "longitude" in exif:
        insights.append("Image contains valid GPS location data.")

    if exif.get("altitude") not in (None, "Unknown"):
        insights.append("Altitude data is available for this image.")

    # Domain hints (simple but powerful)
    if "roof" in labels or "building" in labels:
        insights.append(
            "Structural elements detected. Image may be suitable for inspection analysis."
        )

    if "tree" in labels:
        insights.append(
            "Vegetation detected near structures. Maintenance review may be required."
        )

    return insights
