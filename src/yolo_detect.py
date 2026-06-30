from ultralytics import YOLO
import pandas as pd
import os

# Load YOLOv8 nano model
model = YOLO("yolov8n.pt")

IMAGE_FOLDER = "data/raw/images"
OUTPUT_FILE = "data/processed/detections.csv"

results_data = []

for channel in os.listdir(IMAGE_FOLDER):

    channel_path = os.path.join(IMAGE_FOLDER, channel)

    if not os.path.isdir(channel_path):
        continue

    for image in os.listdir(channel_path):

        if not image.endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(channel_path, image)

        message_id = os.path.splitext(image)[0]

        results = model(image_path)

        if len(results) == 0:
            continue

        for result in results:

            names = result.names

            for box in result.boxes:

                cls = int(box.cls[0])

                confidence = float(box.conf[0])

                detected_object = names[cls]

                # Classification logic
                if detected_object == "person":
                    category = "lifestyle"

                elif detected_object in [
                    "bottle",
                    "cup",
                    "cell phone"
                ]:
                    category = "product_display"

                else:
                    category = "other"

                results_data.append({
                    "message_id": message_id,
                    "channel_name": channel,
                    "detected_class": detected_object,
                    "confidence_score": confidence,
                    "image_category": category
                })

os.makedirs("data/processed", exist_ok=True)

df = pd.DataFrame(results_data)

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())
